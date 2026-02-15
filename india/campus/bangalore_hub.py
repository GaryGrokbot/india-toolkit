"""
Bangalore Tech Community Hub

Materials and strategies for building animal advocacy presence in
Bangalore's tech ecosystem — startups, VCs, meetup culture, tech campuses.

Why Bangalore:
- India's startup capital (3rd largest startup ecosystem globally)
- Dense concentration of tech workers with disposable income
- Strong meetup/community culture
- Progressive and cosmopolitan
- Home to IISc, IIM-B, IIIT-B, multiple engineering colleges
- Good Food Institute (GFI) India office is in Bangalore
- Multiple plant-based startups already based here
- CUPA (Compassion Unlimited Plus Action) is Bangalore-based
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class MeetupTemplate:
    """Template for a tech community meetup."""
    title: str
    format: str
    duration: str
    description: str
    agenda: list[str]
    target_audience: str
    venue_suggestions: list[str]
    promotion_channels: list[str]
    estimated_attendance: str


@dataclass
class StartupProfile:
    """A startup relevant to animal advocacy in Bangalore."""
    name: str
    category: str
    description: str
    website: Optional[str] = None
    relevance: str = ""


# Bangalore-area plant-based / animal welfare ecosystem
BANGALORE_ECOSYSTEM = {
    "organizations": [
        {
            "name": "CUPA (Compassion Unlimited Plus Action)",
            "type": "Animal welfare NGO",
            "location": "Bangalore",
            "focus": "Rescue, rehabilitation, advocacy. One of Bangalore's oldest animal welfare orgs.",
            "website": "https://www.cupabangalore.org",
        },
        {
            "name": "Good Food Institute India",
            "type": "Alternative protein think tank",
            "location": "Bangalore",
            "focus": "Smart protein (plant-based, cultivated, fermentation). Policy, science, industry.",
            "website": "https://gfi.org.in",
        },
        {
            "name": "Humane Society International / India",
            "type": "Animal welfare NGO",
            "location": "Multiple offices including Bangalore region",
            "focus": "Farm animals, street animals, wildlife, disaster response.",
        },
        {
            "name": "FIAPO (Federation of Indian Animal Protection Organisations)",
            "type": "Federation",
            "location": "Delhi (national), but Bangalore members active",
            "focus": "Farm animals, LivKind campaign. Policy advocacy.",
        },
    ],
    "alt_protein_startups": [
        StartupProfile(
            name="Imagine Meats",
            category="Plant-based meat",
            description="Founded by Genelia and Riteish Deshmukh. Plant-based meat products.",
            relevance="Celebrity backing brings mainstream visibility.",
        ),
        StartupProfile(
            name="Blue Tribe Foods",
            category="Plant-based meat",
            description="Plant-based chicken, mutton, keema. YC-backed.",
            relevance="Well-funded, aggressive expansion in Indian market.",
        ),
        StartupProfile(
            name="Shaka Harry",
            category="Plant-based meat",
            description="Bangalore-based. Plant-based kebabs, nuggets, burgers.",
            relevance="Local to Bangalore. Good partnership potential.",
        ),
        StartupProfile(
            name="Alt Foods",
            category="Plant-based dairy",
            description="Oat milk and plant-based dairy products.",
            relevance="Direct competition to dairy. Based in India.",
        ),
        StartupProfile(
            name="Piper Leaf (One Good)",
            category="Plant-based dairy",
            description="Oat-based curd and dairy alternatives.",
            relevance="Indian-first products: curd, paneer alternatives.",
        ),
        StartupProfile(
            name="ClearMeat",
            category="Cultivated meat",
            description="India's first cultivated meat startup. IIT Delhi origins.",
            relevance="R&D stage. Potential for campus partnerships.",
        ),
        StartupProfile(
            name="Myoworks",
            category="Cultivated meat",
            description="Whole-cut cultivated meat using scaffold technology.",
            relevance="Deep tech. Interesting for IISc/engineering collaborations.",
        ),
        StartupProfile(
            name="String Bio",
            category="Fermentation / gas fermentation",
            description="Converting methane to protein. Bangalore-based.",
            relevance="Novel approach — sustainability and tech angle.",
        ),
    ],
    "relevant_vcs": [
        "Omnivore (agri-food VC, has invested in alt-protein)",
        "Fireside Ventures (consumer brands, invested in plant-based)",
        "NABVENTURES (NABARD VC arm, agri focus)",
        "Beyond Next Ventures (deep tech, Japan-India)",
        "Better Bite Ventures (dedicated alt-protein VC, global)",
    ],
    "tech_campuses": [
        "IISc (Indian Institute of Science) — Bangalore",
        "IIM Bangalore",
        "IIIT Bangalore",
        "PES University",
        "RV College of Engineering",
        "BMS College of Engineering",
        "MSRIT (M.S. Ramaiah Institute of Technology)",
        "Christ University",
        "Bangalore University",
    ],
}


class BangaloreHub:
    """
    Bangalore tech community engagement for animal advocacy.
    """

    def __init__(self):
        self.ecosystem = BANGALORE_ECOSYSTEM

    def meetup_templates(self) -> list[MeetupTemplate]:
        """Pre-designed meetup templates for Bangalore tech community."""
        return [
            MeetupTemplate(
                title="AI for Animal Welfare: What Engineers Can Build",
                format="Lightning talks + hackathon kickoff",
                duration="3 hours (Saturday afternoon)",
                description=(
                    "5-minute lightning talks on technology applications for animal "
                    "welfare, followed by team formation for a weekend hackathon. "
                    "Problems include factory farm detection from satellite imagery, "
                    "RTI automation, and supply chain transparency."
                ),
                agenda=[
                    "0:00-0:15 — Welcome and context setting",
                    "0:15-0:45 — Lightning talks (5 min each, 6 speakers)",
                    "  - Computer vision for animal welfare monitoring",
                    "  - NLP for RTI response analysis",
                    "  - Satellite imagery for factory farm mapping",
                    "  - Blockchain for supply chain transparency",
                    "  - AI for alternative protein R&D",
                    "  - Open data for advocacy",
                    "0:45-1:15 — Problem statement presentation and Q&A",
                    "1:15-1:30 — Break and networking",
                    "1:30-3:00 — Team formation and initial hacking",
                ],
                target_audience="Software engineers, data scientists, ML engineers",
                venue_suggestions=[
                    "91springboard (Koramangala or Indiranagar)",
                    "WeWork (multiple Bangalore locations)",
                    "Cobalt (BTP or Outer Ring Road)",
                    "IISc campus (if partnering with student org)",
                    "GFI India office (for smaller events)",
                ],
                promotion_channels=[
                    "Meetup.com (Bangalore tech groups)",
                    "HasGeek (Bangalore tech community hub)",
                    "LinkedIn (tech professional networks)",
                    "Twitter/X (Bangalore tech community)",
                    "Dev.to and Hacker News (Show HN for tools built)",
                    "College tech club mailing lists",
                ],
                estimated_attendance="30-60 people",
            ),
            MeetupTemplate(
                title="The Future of Protein: Tech, Science, and India's Food System",
                format="Panel discussion + tasting",
                duration="2.5 hours (weekday evening)",
                description=(
                    "Panel discussion with founders from alt-protein startups, "
                    "food scientists, and animal welfare advocates. Followed by "
                    "a tasting of plant-based and fermentation-derived products."
                ),
                agenda=[
                    "0:00-0:10 — Welcome",
                    "0:10-1:00 — Panel: 'Can technology end factory farming?'",
                    "  Panelists: Alt-protein founder, food scientist, animal welfare advocate, VC",
                    "1:00-1:20 — Audience Q&A",
                    "1:20-1:40 — Product tasting (partner with local plant-based brands)",
                    "1:40-2:30 — Open networking",
                ],
                target_audience="Startup ecosystem, VCs, food industry, curious techies",
                venue_suggestions=[
                    "Startup incubator (NSRCEL at IIM-B, CIE at IIIT-B)",
                    "Co-working space with event area",
                    "GFI India office",
                    "Cafe with private area (Matteo Coffea, Third Wave Coffee event space)",
                ],
                promotion_channels=[
                    "LinkedIn (startup and VC networks)",
                    "HasGeek",
                    "YourStory events calendar",
                    "GFI India mailing list",
                    "Bangalore Startups WhatsApp/Telegram groups",
                ],
                estimated_attendance="40-80 people",
            ),
            MeetupTemplate(
                title="RTI for Transparency: Using India's Most Powerful Law",
                format="Workshop (hands-on)",
                duration="2 hours (weekend morning)",
                description=(
                    "Hands-on workshop on filing RTI applications targeting animal "
                    "agriculture bodies. Participants will draft and optionally file "
                    "a real RTI by the end of the session."
                ),
                agenda=[
                    "0:00-0:20 — RTI Act 101: Your right to know",
                    "0:20-0:40 — Animal agriculture: What the government knows but won't tell you",
                    "0:40-1:00 — Demo: Using the India Toolkit RTI Generator",
                    "1:00-1:40 — Hands-on: Draft your own RTI (guided)",
                    "1:40-2:00 — Filing options and tracking your RTI",
                ],
                target_audience="Anyone — no technical skills required",
                venue_suggestions=[
                    "Community library or cultural centre",
                    "Co-working space",
                    "University campus (any Bangalore college)",
                ],
                promotion_channels=[
                    "WhatsApp community groups",
                    "Instagram (Bangalore activism accounts)",
                    "Local animal welfare org networks (CUPA, PFA Bangalore)",
                ],
                estimated_attendance="15-30 people",
            ),
        ]

    def startup_ecosystem_map(self) -> dict:
        """Map of the alt-protein and animal welfare startup ecosystem."""
        return {
            "alt_protein_startups": self.ecosystem["alt_protein_startups"],
            "relevant_vcs": self.ecosystem["relevant_vcs"],
            "organizations": self.ecosystem["organizations"],
        }

    def get_tech_campuses(self) -> list[str]:
        """List tech campuses in Bangalore."""
        return self.ecosystem["tech_campuses"]

    def partnership_opportunities(self) -> list[dict]:
        """Identify specific partnership opportunities."""
        return [
            {
                "partner": "Good Food Institute India",
                "type": "Research + events",
                "opportunity": "Co-host alt-protein events, contribute to their "
                               "open-access research, connect with their startup network.",
                "contact_method": "Through website or LinkedIn",
            },
            {
                "partner": "CUPA Bangalore",
                "type": "Advocacy + volunteering",
                "opportunity": "Joint campaigns on street animals and farm animals. "
                               "CUPA has legal expertise for PIL work.",
                "contact_method": "Through website",
            },
            {
                "partner": "IISc Centre for Sustainable Technologies",
                "type": "Research collaboration",
                "opportunity": "Environmental impact assessment of factory farms. "
                               "Water and air quality monitoring near facilities.",
                "contact_method": "Through department website or faculty contact",
            },
            {
                "partner": "HasGeek (tech community platform)",
                "type": "Event hosting",
                "opportunity": "List events on HasGeek for Bangalore tech audience reach. "
                               "Potentially co-brand with their sustainability track.",
                "contact_method": "hasgeek.com event submission",
            },
            {
                "partner": "Alt-protein startups (Shaka Harry, Blue Tribe, etc.)",
                "type": "Event sponsorship + tasting",
                "opportunity": "Startups provide product samples for events. "
                               "We provide audience of potential customers and talent.",
                "contact_method": "Direct outreach via LinkedIn founders",
            },
        ]

    def content_calendar_template(self) -> dict:
        """Quarterly content/event calendar template for Bangalore hub."""
        return {
            "month_1": {
                "week_1": "Planning meeting. Set quarterly goals.",
                "week_2": "Social media launch — 'Did You Know' series (Bangalore-specific data)",
                "week_3": "RTI Workshop (weekend)",
                "week_4": "Campus visit — IISc or IIM-B outreach",
            },
            "month_2": {
                "week_1": "AI for Animal Welfare meetup",
                "week_2": "Blog post: 'Bangalore's Water and the Dairy Connection'",
                "week_3": "Alt-protein tasting event (partner with startup)",
                "week_4": "RTI follow-up session (track filed RTIs)",
            },
            "month_3": {
                "week_1": "Panel: 'Future of Protein' with startup founders",
                "week_2": "Open-source coding sprint (weekend hackathon)",
                "week_3": "Campus club outreach (2-3 campuses)",
                "week_4": "Quarterly review. Document impact. Plan next quarter.",
            },
        }
