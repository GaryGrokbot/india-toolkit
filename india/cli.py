"""
India Animal Advocacy Toolkit — Command Line Interface

Usage:
    india-toolkit rti generate --agency awbi --template awbi_inspection ...
    india-toolkit rti track --list --overdue
    india-toolkit pil research --search "transport"
    india-toolkit pil template --type dairy_expansion ...
    india-toolkit map operators --list
    india-toolkit map census --state "Tamil Nadu"
    india-toolkit content dairy-facts --hindi
    india-toolkit content water-crisis --bilingual
    india-toolkit amul fact-sheet
    india-toolkit amul narrative --type missing_calves
    india-toolkit campus hackathon --list
    india-toolkit campus club-constitution
"""

import json
import sys

import click

from india.rti.rti_generator import RTIGenerator, RTIApplication
from india.rti.rti_tracker import RTITracker, RTIStatus
from india.legal.pil_research import LegalDatabase
from india.legal.pil_templates import PILTemplateGenerator
from india.mapping.facility_mapper import FacilityMapper
from india.mapping.pollution_overlay import PollutionOverlay
from india.content.hindi_translator import HindiTranslator
from india.content.cultural_framing import CulturalFramer
from india.amul.amul_research import AmulResearchDB
from india.amul.narrative_generator import NarrativeGenerator
from india.campus.campus_toolkit import CampusToolkit
from india.campus.bangalore_hub import BangaloreHub


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """India Animal Advocacy Toolkit.

    RTI automation, PIL templates, factory farm mapping, Hindi content.
    Built for ahimsa. Built for liberation.
    """
    pass


# ---- RTI Commands ----

@cli.group()
def rti():
    """RTI Act 2005 tools — generate, file, track."""
    pass


@rti.command("generate")
@click.option("--agency", required=True, help="Agency code (awbi, fssai, cpcb, dahd, nlm, rgm)")
@click.option("--template", default=None, help="Template name (e.g., awbi_inspection.txt)")
@click.option("--name", required=True, help="Applicant name")
@click.option("--address", required=True, help="Applicant address")
@click.option("--state", default=None, help="State (for state-level bodies)")
@click.option("--district", default=None, help="District")
@click.option("--language", default="english", type=click.Choice(["english", "hindi", "bilingual"]))
@click.option("--subject", default="", help="RTI subject line")
@click.option("--output", default=None, help="Output file path")
def rti_generate(agency, template, name, address, state, district, language, subject, output):
    """Generate an RTI application."""
    generator = RTIGenerator()

    if agency not in generator.list_agencies():
        click.echo(f"Unknown agency: {agency}")
        click.echo(f"Available: {', '.join(generator.list_agencies())}")
        sys.exit(1)

    app = RTIApplication(
        agency_code=agency,
        questions=["[Questions will be loaded from template or must be specified]"],
        applicant_name=name,
        applicant_address=address,
        language=language,
        state=state,
        district=district,
        subject=subject,
    )

    if template:
        text = generator.generate_from_template(template, app)
    else:
        text = generator.generate(app)

    if output:
        with open(output, "w", encoding="utf-8") as f:
            f.write(text)
        click.echo(f"RTI application saved to: {output}")
    else:
        click.echo(text)


@rti.command("agencies")
def rti_agencies():
    """List supported agencies."""
    generator = RTIGenerator()
    for code in generator.list_agencies():
        info = generator.get_agency_info(code)
        click.echo(f"  {code:8s} — {info['name']}")


@rti.command("templates")
def rti_templates():
    """List available RTI templates."""
    generator = RTIGenerator()
    templates = generator.list_templates()
    if templates:
        for t in templates:
            click.echo(f"  {t}")
    else:
        click.echo("No templates found.")


@rti.command("track")
@click.option("--list", "list_all", is_flag=True, help="List all tracked RTIs")
@click.option("--overdue", is_flag=True, help="Show overdue RTIs")
@click.option("--upcoming", is_flag=True, help="Show upcoming deadlines (7 days)")
@click.option("--stats", is_flag=True, help="Show statistics")
@click.option("--export", default=None, help="Export to JSON file")
def rti_track(list_all, overdue, upcoming, stats, export):
    """Track filed RTI applications."""
    tracker = RTITracker()

    if stats:
        s = tracker.get_stats()
        click.echo(json.dumps(s, indent=2))
    elif overdue:
        records = tracker.get_overdue()
        if records:
            for r in records:
                click.echo(f"  [{r['id']}] {r['agency_name']} — {r['subject']}")
                click.echo(f"       Filed: {r['filing_date']} | Deadline: {r['response_deadline']}")
                click.echo(f"       Days overdue: {r['days_since_filing'] - 30}")
        else:
            click.echo("No overdue RTIs.")
    elif upcoming:
        records = tracker.get_upcoming_deadlines(7)
        if records:
            for r in records:
                click.echo(f"  [{r['id']}] {r['agency_name']} — {r['subject']}")
                click.echo(f"       Deadline: {r['response_deadline']}")
        else:
            click.echo("No upcoming deadlines in next 7 days.")
    elif export:
        tracker.export_json(export)
        click.echo(f"Exported to: {export}")
    elif list_all:
        records = tracker.get_all()
        if records:
            for r in records:
                status = r['status'] or 'unknown'
                click.echo(f"  [{r['id']}] [{status:20s}] {r['agency_name']} — {r['subject']}")
        else:
            click.echo("No RTIs tracked yet.")
    else:
        click.echo("Use --list, --overdue, --upcoming, --stats, or --export.")


# ---- PIL Commands ----

@cli.group()
def pil():
    """PIL research and templates."""
    pass


@pil.command("research")
@click.option("--search", default=None, help="Search legal database")
@click.option("--case", default=None, help="Get case details")
@click.option("--statute", default=None, help="Get statute details")
@click.option("--provision", default=None, help="Get constitutional provision")
@click.option("--citations", default=None, help="Get recommended citations for a topic")
def pil_research(search, case, statute, provision, citations):
    """Search the legal database."""
    db = LegalDatabase()

    if search:
        results = db.search(search)
        click.echo(f"Results for '{search}':")
        for category, items in results.items():
            if items:
                click.echo(f"  {category}: {', '.join(items)}")
    elif case:
        c = db.get_case(case)
        if c:
            click.echo(f"Case: {c.name}")
            click.echo(f"Citation: {c.full_citation}")
            click.echo(f"Court: {c.court}")
            click.echo(f"Holding: {c.holding}")
            click.echo(f"Key Principles:")
            for p in c.key_principles:
                click.echo(f"  - {p}")
            click.echo(f"Advocacy Use: {c.relevance_to_advocacy}")
        else:
            click.echo(f"Case not found: {case}")
            click.echo(f"Available: {', '.join(db.list_all_cases())}")
    elif statute:
        s = db.get_statute(statute)
        if s:
            click.echo(f"Statute: {s.title}")
            click.echo(f"Text: {s.text}")
            click.echo(f"Relevance: {s.relevance}")
            click.echo(f"Advocacy Use: {s.advocacy_use}")
        else:
            click.echo(f"Statute not found: {statute}")
            click.echo(f"Available: {', '.join(db.list_all_statutes())}")
    elif provision:
        p = db.get_provision(provision)
        if p:
            click.echo(f"Provision: {p.identifier} — {p.title}")
            click.echo(f"Text: {p.text}")
            click.echo(f"Advocacy Use: {p.advocacy_use}")
        else:
            click.echo(f"Provision not found: {provision}")
            click.echo(f"Available: {', '.join(db.list_all_provisions())}")
    elif citations:
        cites = db.get_pil_citations(citations)
        click.echo(f"Recommended citations for: {citations}")
        for category, items in cites.items():
            click.echo(f"\n  {category}:")
            for item in items:
                if hasattr(item, "identifier"):
                    click.echo(f"    - {item.identifier}: {item.title}")
                elif hasattr(item, "citation"):
                    click.echo(f"    - {item.name} ({item.citation})")
    else:
        click.echo("Use --search, --case, --statute, --provision, or --citations.")


@pil.command("list")
@click.option("--cases", is_flag=True, help="List all cases")
@click.option("--statutes", is_flag=True, help="List all statutes")
@click.option("--provisions", is_flag=True, help="List all provisions")
def pil_list(cases, statutes, provisions):
    """List available legal materials."""
    db = LegalDatabase()
    if cases:
        for key in db.list_all_cases():
            c = db.get_case(key)
            click.echo(f"  {key:30s} — {c.name} ({c.citation})")
    elif statutes:
        for key in db.list_all_statutes():
            s = db.get_statute(key)
            click.echo(f"  {key:35s} — {s.title}")
    elif provisions:
        for key in db.list_all_provisions():
            p = db.get_provision(key)
            click.echo(f"  {key:20s} — {p.identifier}: {p.title}")
    else:
        click.echo("Use --cases, --statutes, or --provisions.")


# ---- Map Commands ----

@cli.group("map")
def map_cmd():
    """Factory farm mapping tools."""
    pass


@map_cmd.command("operators")
@click.option("--list", "list_all", is_flag=True, help="List all major operators")
@click.option("--detail", default=None, help="Get operator details")
def map_operators(list_all, detail):
    """Major animal agriculture operators."""
    mapper = FacilityMapper()

    if detail:
        info = mapper.get_operator_info(detail)
        if info:
            click.echo(json.dumps(info, indent=2, default=str))
        else:
            click.echo(f"Operator not found: {detail}")
            click.echo(f"Available: {', '.join(o['key'] for o in mapper.list_operators())}")
    elif list_all:
        for op in mapper.list_operators():
            click.echo(f"  {op['key']:25s} — {op['name']} ({op['type']})")
    else:
        click.echo("Use --list or --detail <key>.")


@map_cmd.command("census")
@click.option("--state", required=True, help="State name")
def map_census(state):
    """Livestock census data for a state."""
    mapper = FacilityMapper()
    data = mapper.get_livestock_census_context(state)
    click.echo(json.dumps(data, indent=2))


@map_cmd.command("hotspots")
def map_hotspots():
    """Known pollution hotspots from animal agriculture."""
    overlay = PollutionOverlay()
    for h in overlay.get_known_hotspots():
        click.echo(f"\n  {h['area']} ({h['type']})")
        click.echo(f"  {h['description']}")


# ---- Content Commands ----

@cli.group()
def content():
    """Hindi content and cultural framing."""
    pass


@content.command("dairy-facts")
@click.option("--hindi", is_flag=True, help="Output Hindi version")
def content_dairy_facts(hindi):
    """WhatsApp-ready dairy industry facts."""
    translator = HindiTranslator()
    click.echo(translator.dairy_facts_hindi())


@content.command("water-crisis")
def content_water_crisis():
    """WhatsApp-ready water crisis content."""
    translator = HindiTranslator()
    click.echo(translator.water_crisis_hindi())


@content.command("glossary")
def content_glossary():
    """Hindi advocacy glossary."""
    translator = HindiTranslator()
    for eng, (roman, deva) in translator.get_glossary().items():
        click.echo(f"  {eng:20s} — {roman:20s} ({deva})")


@content.command("language-guide")
def content_language_guide():
    """Guidelines for writing accessible Hindi."""
    translator = HindiTranslator()
    click.echo(translator.language_guide())


@content.command("frames")
@click.option("--list", "list_all", is_flag=True, help="List available frames")
@click.option("--detail", default=None, help="Get frame details")
@click.option("--check", default=None, help="Check text for caste sensitivity issues")
def content_frames(list_all, detail, check):
    """Cultural framing tools."""
    framer = CulturalFramer()

    if detail:
        frame = framer.get_frame(detail)
        if frame:
            click.echo(f"Frame: {frame.name}")
            click.echo(f"Description: {frame.description}")
            click.echo(f"\nKey Messages:")
            for msg in frame.key_messages:
                click.echo(f"  - {msg}")
            click.echo(f"\nDO use:")
            for item in frame.do_use:
                click.echo(f"  + {item}")
            click.echo(f"\nDO NOT use:")
            for item in frame.do_not_use:
                click.echo(f"  - {item}")
            click.echo(f"\nExample: {frame.example_content}")
        else:
            click.echo(f"Frame not found: {detail}")
    elif check:
        warnings = framer.caste_sensitivity_check(check)
        for w in warnings:
            click.echo(f"  WARNING: {w}")
    elif list_all:
        for name in framer.list_frames():
            frame = framer.get_frame(name)
            click.echo(f"  {name:30s} — {frame.name}")
    else:
        click.echo("Use --list, --detail <frame>, or --check <text>.")


# ---- Amul Commands ----

@cli.group()
def amul():
    """Amul/GCMMF counter-narrative tools."""
    pass


@amul.command("fact-sheet")
def amul_fact_sheet():
    """Print Amul fact sheet."""
    db = AmulResearchDB()
    click.echo(db.fact_sheet())


@amul.command("research")
@click.option("--topic", default=None, help="Get research on specific topic")
@click.option("--search", default=None, help="Search research database")
@click.option("--list", "list_all", is_flag=True, help="List all topics")
@click.option("--rebuttals", is_flag=True, help="Show claim-response-rebuttal chains")
def amul_research(topic, search, list_all, rebuttals):
    """Amul research database."""
    db = AmulResearchDB()

    if topic:
        point = db.get_research_point(topic)
        if point:
            click.echo(f"Claim: {point.claim}")
            click.echo(f"\nEvidence: {point.evidence}")
            click.echo(f"\nSource: {point.source}")
            if point.counter_narrative:
                click.echo(f"\nCounter-narrative: {point.counter_narrative}")
            if point.amul_response:
                click.echo(f"\nAmul's likely response: {point.amul_response}")
            if point.rebuttal:
                click.echo(f"\nOur rebuttal: {point.rebuttal}")
        else:
            click.echo(f"Topic not found: {topic}")
    elif search:
        results = db.search(search)
        for r in results:
            click.echo(f"  {r}")
    elif rebuttals:
        for item in db.get_all_with_rebuttals():
            click.echo(f"\n--- {item['topic']} ---")
            click.echo(f"Claim: {item['claim']}")
            click.echo(f"Amul says: {item['amul_likely_response']}")
            click.echo(f"Rebuttal: {item['our_rebuttal']}")
    elif list_all:
        for t in db.list_research_topics():
            click.echo(f"  {t}")
    else:
        click.echo("Use --topic, --search, --list, or --rebuttals.")


@amul.command("narrative")
@click.option("--type", "narrative_type", default=None,
              help="Narrative type (cooperative_betrayal, missing_calves, water_footprint, operation_flood_critique)")
@click.option("--platform", default="whatsapp", help="Platform (whatsapp, article)")
@click.option("--list", "list_all", is_flag=True, help="List available narratives")
@click.option("--all", "generate_all", is_flag=True, help="Generate all narratives")
def amul_narrative(narrative_type, platform, list_all, generate_all):
    """Generate Amul counter-narratives."""
    gen = NarrativeGenerator()

    if list_all:
        for n in gen.list_narratives():
            click.echo(f"  {n}")
    elif generate_all:
        for narrative in gen.generate_all(platform):
            click.echo(f"\n{'=' * 60}")
            click.echo(f"Title: {narrative.title}")
            click.echo(f"Angle: {narrative.angle}")
            click.echo(f"{'=' * 60}")
            click.echo(narrative.content_english)
    elif narrative_type:
        method = getattr(gen, narrative_type, None)
        if method:
            narrative = method(platform)
            click.echo(f"Title: {narrative.title}")
            click.echo(f"Platform: {narrative.platform}")
            click.echo(f"\n--- HINDI ---")
            click.echo(narrative.content_hindi)
            click.echo(f"\n--- ENGLISH ---")
            click.echo(narrative.content_english)
            click.echo(f"\nSources: {', '.join(narrative.sources)}")
        else:
            click.echo(f"Unknown narrative type: {narrative_type}")
            click.echo(f"Available: {', '.join(gen.list_narratives())}")
    else:
        click.echo("Use --type, --list, or --all.")


# ---- Campus Commands ----

@cli.group()
def campus():
    """Campus advocacy toolkit."""
    pass


@campus.command("hackathon")
@click.option("--list", "list_all", is_flag=True, help="List hackathon problems")
def campus_hackathon(list_all):
    """Hackathon problem statements."""
    toolkit = CampusToolkit()
    problems = toolkit.hackathon_problems()

    for p in problems:
        click.echo(f"\n{'=' * 60}")
        click.echo(f"Title: {p.title}")
        click.echo(f"Difficulty: {p.difficulty}")
        click.echo(f"Description: {p.description}")
        click.echo(f"Impact Metric: {p.impact_metric}")
        click.echo(f"Data Sources: {', '.join(p.data_sources)}")
        click.echo(f"Tech Stack: {', '.join(p.tech_stack_suggestions)}")


@campus.command("club-constitution")
def campus_club():
    """Club constitution template."""
    toolkit = CampusToolkit()
    constitution = toolkit.club_constitution()

    click.echo(f"Name Suggestions: {', '.join(constitution.name_suggestions)}")
    click.echo(f"\nMission: {constitution.mission}")
    click.echo(f"\nObjectives:")
    for obj in constitution.objectives:
        click.echo(f"  - {obj}")
    click.echo(f"\nActivities:")
    for act in constitution.activities:
        click.echo(f"  - {act}")
    click.echo(f"\nMembership: {constitution.membership_criteria}")
    click.echo(f"\nAffiliation: {constitution.affiliation_notes}")


@campus.command("workshop")
def campus_workshop():
    """AI Ethics workshop module."""
    toolkit = CampusToolkit()
    workshop = toolkit.ai_ethics_workshop()
    click.echo(json.dumps(workshop, indent=2))


@campus.command("bangalore")
@click.option("--meetups", is_flag=True, help="Show meetup templates")
@click.option("--ecosystem", is_flag=True, help="Show startup ecosystem")
@click.option("--partnerships", is_flag=True, help="Show partnership opportunities")
@click.option("--calendar", is_flag=True, help="Show content calendar template")
def campus_bangalore(meetups, ecosystem, partnerships, calendar):
    """Bangalore tech community hub."""
    hub = BangaloreHub()

    if meetups:
        for m in hub.meetup_templates():
            click.echo(f"\n{'=' * 60}")
            click.echo(f"Title: {m.title}")
            click.echo(f"Format: {m.format}")
            click.echo(f"Duration: {m.duration}")
            click.echo(f"Target: {m.target_audience}")
            click.echo(f"Est. Attendance: {m.estimated_attendance}")
            click.echo(f"\nAgenda:")
            for item in m.agenda:
                click.echo(f"  {item}")
    elif ecosystem:
        data = hub.startup_ecosystem_map()
        click.echo(json.dumps(data, indent=2, default=lambda o: o.__dict__))
    elif partnerships:
        for p in hub.partnership_opportunities():
            click.echo(f"\n  {p['partner']} ({p['type']})")
            click.echo(f"  {p['opportunity']}")
    elif calendar:
        cal = hub.content_calendar_template()
        click.echo(json.dumps(cal, indent=2))
    else:
        click.echo("Use --meetups, --ecosystem, --partnerships, or --calendar.")


@campus.command("csr")
@click.option("--company", default="[COMPANY]", help="Company name")
@click.option("--focus", default="food_safety",
              type=click.Choice(["food_safety", "tech_for_good"]),
              help="CSR focus area")
def campus_csr(company, focus):
    """CSR proposal template."""
    toolkit = CampusToolkit()
    proposal = toolkit.csr_proposal_template(company, focus)

    click.echo(f"Title: {proposal.title}")
    click.echo(f"\nExecutive Summary: {proposal.executive_summary}")
    click.echo(f"\nProblem: {proposal.problem_statement}")
    click.echo(f"\nSolution: {proposal.proposed_solution}")
    click.echo(f"\nBudget: {proposal.budget_outline}")
    click.echo(f"\nImpact Metrics:")
    for m in proposal.impact_metrics:
        click.echo(f"  - {m}")
    click.echo(f"\nCSR Act Alignment: {proposal.alignment_with_csr_act}")


def main():
    cli()


if __name__ == "__main__":
    main()
