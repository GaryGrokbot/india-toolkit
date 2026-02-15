"""
Campus Advocacy Toolkit

Materials for building animal advocacy presence at Indian institutes of
technology (IITs), management (IIMs), and other premier campuses.

Strategy: Meet students where they are — AI ethics, sustainability,
entrepreneurship, social impact. Frame animal advocacy as a
technology and innovation challenge, not just a moral argument.

Target campuses:
- IITs: Delhi, Bombay, Madras, Kanpur, Kharagpur, Bangalore, Hyderabad, Roorkee
- IIMs: Ahmedabad, Bangalore, Calcutta, Lucknow, Indore
- IISC Bangalore
- BITS Pilani, NIT system
- Delhi University, JNU, Jawaharlal Nehru University
- Ashoka University, OP Jindal, FLAME
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class HackathonProblem:
    """A hackathon problem statement for campus events."""
    title: str
    description: str
    background: str
    data_sources: list[str]
    evaluation_criteria: list[str]
    tech_stack_suggestions: list[str]
    impact_metric: str
    difficulty: str  # "beginner", "intermediate", "advanced"


@dataclass
class ClubConstitution:
    """Template for a campus animal advocacy club."""
    name_suggestions: list[str]
    mission: str
    objectives: list[str]
    activities: list[str]
    organizational_structure: str
    membership_criteria: str
    affiliation_notes: str


@dataclass
class CSRProposal:
    """CSR proposal template for campus placement companies."""
    title: str
    executive_summary: str
    problem_statement: str
    proposed_solution: str
    budget_outline: str
    impact_metrics: list[str]
    alignment_with_csr_act: str


class CampusToolkit:
    """
    Campus advocacy materials for Indian higher education institutions.
    """

    def ai_ethics_workshop(self) -> dict:
        """
        Workshop module: AI Ethics and Animal Sentience.

        Frame: If we're building AI systems that might be sentient,
        we should care about beings we KNOW are sentient — animals.
        This connects to active CS/AI research interests.
        """
        return {
            "title": "AI Ethics Workshop: Sentience, Rights, and the Beings We Overlook",
            "duration": "3 hours (2 sessions)",
            "target": "CS/AI students, ethics course participants",
            "session_1": {
                "title": "Machine Sentience and Animal Sentience",
                "outline": [
                    "The sentience debate in AI: What would make an AI 'sentient'?",
                    "Scientific consensus on animal sentience: Cambridge Declaration on "
                    "Consciousness (2012), New York Declaration on Animal Consciousness (2024, ~480 signatories)",
                    "Neuroscience of animal cognition: pain, emotions, social bonds",
                    "The inconsistency: We debate whether future AI needs rights while "
                    "ignoring beings we know are sentient",
                    "Case study: India's AWBI v. Nagaraja (2014) — Supreme Court recognized "
                    "animal right to life with dignity",
                ],
                "readings": [
                    "Cambridge Declaration on Consciousness (2012)",
                    "New York Declaration on Animal Consciousness (2024)",
                    "Butlin et al., 'Consciousness in Artificial Intelligence: Insights from the Science of Consciousness' (November 2025)",
                    "AWBI v. A. Nagaraja, (2014) 7 SCC 547 — full text",
                ],
            },
            "session_2": {
                "title": "Technology for Animal Welfare: What Can Engineers Build?",
                "outline": [
                    "Computer vision for monitoring factory farm conditions",
                    "NLP for analyzing corporate disclosures and greenwashing",
                    "Satellite imagery for mapping factory farms",
                    "Blockchain for supply chain transparency",
                    "AI for accelerating alternative protein R&D",
                    "Open-source tools for advocacy (RTI automation, legal research)",
                ],
                "hands_on": "RTI Generator demo — file an RTI for your district's "
                            "poultry farm data using the India Toolkit CLI",
            },
            "resources_needed": [
                "Projector and laptop",
                "WiFi for live demos",
                "Printed copies of Cambridge and New York Declarations",
                "India Toolkit installed for demo",
            ],
        }

    def hackathon_problems(self) -> list[HackathonProblem]:
        """
        Hackathon problem statements for campus tech events.
        """
        return [
            HackathonProblem(
                title="Factory Farm Finder: Satellite-Based Detection",
                description=(
                    "Build a system that identifies potential factory farm locations "
                    "from satellite imagery. Use Sentinel-2 or Landsat data to detect "
                    "large poultry sheds, dairy operations, and aquaculture ponds."
                ),
                background=(
                    "India has no public registry of factory farms. Pollution Control "
                    "Boards maintain Consent to Operate records but these are not "
                    "digitized or public. Satellite imagery can fill this data gap."
                ),
                data_sources=[
                    "Sentinel-2 (Copernicus Open Access Hub — free)",
                    "Google Earth Engine (free for research)",
                    "OpenStreetMap building footprints",
                    "20th Livestock Census district-level data (for ground truth)",
                ],
                evaluation_criteria=[
                    "Detection accuracy (precision/recall)",
                    "Scalability to state/national level",
                    "User interface for non-technical advocates",
                    "Integration with existing mapping tools",
                ],
                tech_stack_suggestions=[
                    "Python, TensorFlow/PyTorch for image classification",
                    "Google Earth Engine API",
                    "Leaflet.js or Mapbox for visualization",
                    "PostGIS for spatial data",
                ],
                impact_metric="Number of previously unknown facilities identified",
                difficulty="advanced",
            ),
            HackathonProblem(
                title="RTI Auto-Tracker: Deadline Management System",
                description=(
                    "Build a web/mobile app that helps advocates track multiple "
                    "RTI applications, sends deadline reminders, auto-generates "
                    "first appeal drafts when response deadlines pass, and "
                    "aggregates response data for analysis."
                ),
                background=(
                    "Animal advocacy organizations file hundreds of RTIs annually. "
                    "Tracking deadlines (30-day response, appeal windows) across "
                    "multiple agencies is error-prone. Missed deadlines = lost data."
                ),
                data_sources=[
                    "RTI Act, 2005 (deadline rules)",
                    "PIO directory (available in this toolkit)",
                    "Previous RTI responses (for training NLP models)",
                ],
                evaluation_criteria=[
                    "User experience (simplicity for non-technical users)",
                    "Notification reliability",
                    "Auto-generation quality for appeal drafts",
                    "Data visualization (trends, response rates)",
                ],
                tech_stack_suggestions=[
                    "React Native or Flutter for mobile",
                    "FastAPI or Django backend",
                    "PostgreSQL database",
                    "Twilio/WhatsApp API for notifications",
                ],
                impact_metric="Percentage reduction in missed RTI deadlines",
                difficulty="intermediate",
            ),
            HackathonProblem(
                title="Milk Adulteration Citizen Reporter",
                description=(
                    "Build a platform where citizens can report suspected milk "
                    "adulteration, upload test results, and see a heatmap of "
                    "adulteration reports in their area. Include simple at-home "
                    "testing guides."
                ),
                background=(
                    "FSSAI's 2018 survey found 41% of milk samples failed quality "
                    "standards. Most consumers have no way to know if their milk "
                    "is adulterated. Simple tests (lactometer, starch test) can be "
                    "done at home."
                ),
                data_sources=[
                    "FSSAI National Milk Quality Survey data",
                    "At-home milk testing protocols (FSSAI published)",
                    "User-submitted reports",
                ],
                evaluation_criteria=[
                    "Ease of reporting",
                    "Accuracy of testing guides",
                    "Visualization quality",
                    "Privacy protection for reporters",
                ],
                tech_stack_suggestions=[
                    "Progressive Web App (works on low-end phones)",
                    "Firebase or Supabase backend",
                    "Mapbox for heatmap",
                    "Hindi/English bilingual UI",
                ],
                impact_metric="Number of reports leading to FSSAI action",
                difficulty="beginner",
            ),
            HackathonProblem(
                title="Supply Chain Transparency: Farm to Table Tracker",
                description=(
                    "Build a system that traces animal products from farm to "
                    "retail. Use FSSAI license numbers, transport permits, and "
                    "company filings to map supply chains of major operators."
                ),
                background=(
                    "Consumers cannot trace where their dairy/poultry comes from. "
                    "Major integrators (Suguna, Venky's) operate complex supply "
                    "chains through contract farmers. Traceability = accountability."
                ),
                data_sources=[
                    "FSSAI license registry",
                    "MCA company filings (CIN lookup)",
                    "Company annual reports",
                    "RTI data on transport permits",
                ],
                evaluation_criteria=[
                    "Supply chain mapping depth",
                    "Data accuracy and sourcing",
                    "User-facing visualization",
                    "Scalability",
                ],
                tech_stack_suggestions=[
                    "Neo4j or graph database for supply chain mapping",
                    "Python scrapers for public data",
                    "D3.js for visualization",
                    "OCR for processing RTI response documents",
                ],
                impact_metric="Number of supply chains fully mapped",
                difficulty="advanced",
            ),
        ]

    def club_constitution(self) -> ClubConstitution:
        """
        Template for a campus animal advocacy club constitution.
        """
        return ClubConstitution(
            name_suggestions=[
                "Ahimsa Tech Collective",
                "Sentient Rights Forum",
                "Students for Animal Welfare",
                "The Compassion Project",
                "Zero Cruelty Initiative",
            ],
            mission=(
                "To advance animal welfare and rights through technology, research, "
                "and education, using evidence-based advocacy and cross-disciplinary "
                "collaboration."
            ),
            objectives=[
                "Research: Investigate animal agriculture practices in India using "
                "RTI, data analysis, and field documentation.",
                "Technology: Build open-source tools for animal advocacy (mapping, "
                "tracking, content generation).",
                "Education: Host workshops on animal sentience, AI ethics, food "
                "systems, and environmental impact of animal agriculture.",
                "Outreach: Create accessible content in Hindi and English for "
                "campus and public audiences.",
                "Policy: Engage with campus administration on food procurement, "
                "lab animal policies, and sustainability goals.",
                "Solidarity: Partner with environmental, labor, and social justice "
                "groups on campus. Never work in isolation.",
            ],
            activities=[
                "Weekly meetings / reading group",
                "Monthly film screenings (documentaries on animal agriculture)",
                "Semester hackathon with animal welfare problem statements",
                "RTI filing workshops",
                "Guest lectures (animal welfare lawyers, scientists, activists)",
                "Plant-based food tastings and cooking workshops",
                "Campus sustainability audits (food procurement analysis)",
                "Open-source coding sprints (contributing to advocacy tools)",
                "Annual report: 'State of Animals' for your campus district",
            ],
            organizational_structure=(
                "President, Vice-President, Secretary, Treasurer, and up to 5 "
                "coordinators (Research, Tech, Content, Outreach, Events). "
                "All positions elected annually. Decisions by simple majority. "
                "No single-person veto."
            ),
            membership_criteria=(
                "Open to all students regardless of dietary choices, religious "
                "background, or caste. We do not police personal food choices. "
                "We focus on systemic change, not individual guilt. "
                "Members must agree to the cultural sensitivity guidelines "
                "(no casteist framing, no communal rhetoric, no diet-shaming)."
            ),
            affiliation_notes=(
                "Potential affiliations: FIAPO (Federation of Indian Animal Protection "
                "Organisations), HSI/India, PFA (People for Animals — research local "
                "chapter reputation first), CUPA (Compassion Unlimited Plus Action, Bangalore).\n"
                "International: The Good Food Institute India (GFI India) for alt-protein, "
                "Animal Equality India, Mercy for Animals India."
            ),
        )

    def csr_proposal_template(
        self,
        company_name: str = "[COMPANY]",
        focus_area: str = "food_safety",
    ) -> CSRProposal:
        """
        CSR proposal template for campus placement companies.

        Under Companies Act 2013 Section 135, companies with net worth >= Rs. 500 crore
        or turnover >= Rs. 1000 crore or net profit >= Rs. 5 crore must spend 2% of
        average net profits on CSR.

        Schedule VII eligible activities include: environmental sustainability,
        animal welfare, rural development, health.
        """
        proposals = {
            "food_safety": CSRProposal(
                title=f"Proposal to {company_name}: Community Food Safety and Animal Welfare Initiative",
                executive_summary=(
                    f"We propose that {company_name} fund a community food safety "
                    f"monitoring programme combined with animal welfare auditing "
                    f"in [DISTRICT]. This addresses Schedule VII items (i) health, "
                    f"(iv) environmental sustainability, and animal welfare."
                ),
                problem_statement=(
                    "FSSAI's 2018 National Milk Quality Survey found 41% of samples "
                    "failed quality standards. Consumers in tier-2/3 cities have no "
                    "access to food quality information. Simultaneously, animals in "
                    "the dairy supply chain face welfare violations with no monitoring."
                ),
                proposed_solution=(
                    "1. Establish a community milk testing lab (capital cost: Rs. 5-10 lakh)\n"
                    "2. Train 10 community food safety monitors\n"
                    "3. Quarterly testing and public reporting\n"
                    "4. Animal welfare auditing at supply chain level\n"
                    "5. Open-source data dashboard for community access"
                ),
                budget_outline=(
                    "Year 1: Rs. 20-30 lakh\n"
                    "- Lab equipment: Rs. 8 lakh\n"
                    "- Training: Rs. 3 lakh\n"
                    "- Operations (12 months): Rs. 10 lakh\n"
                    "- Technology platform: Rs. 5 lakh\n"
                    "- Documentation and reporting: Rs. 4 lakh"
                ),
                impact_metrics=[
                    "Number of milk samples tested",
                    "Adulteration incidents detected and reported",
                    "Community members with access to food safety data",
                    "Animal welfare improvements documented",
                    "FSSAI actions triggered by community monitoring",
                ],
                alignment_with_csr_act=(
                    "Eligible under Companies Act 2013, Section 135, Schedule VII:\n"
                    "- Item (i): Promoting health care including preventive health care\n"
                    "- Item (iv): Ensuring environmental sustainability\n"
                    "- Animal welfare: Explicitly mentioned in Schedule VII\n"
                    "- Item (x): Rural development projects"
                ),
            ),
            "tech_for_good": CSRProposal(
                title=f"Proposal to {company_name}: Open-Source Technology for Animal Welfare",
                executive_summary=(
                    f"We propose that {company_name} sponsor development of open-source "
                    f"technology tools for animal welfare monitoring and advocacy in India."
                ),
                problem_statement=(
                    "India has 535 million livestock and 851 million poultry (Livestock "
                    "Census 2019) but minimal technology infrastructure for monitoring "
                    "animal welfare, tracking regulatory compliance, or enabling "
                    "citizen reporting."
                ),
                proposed_solution=(
                    "1. Fund a team of 3-5 developers for 12 months\n"
                    "2. Build and deploy: factory farm mapping tool, RTI automation "
                    "system, citizen reporting platform\n"
                    "3. All code open-source (MIT license)\n"
                    "4. Partner with animal welfare NGOs for deployment\n"
                    "5. Campus ambassador programme for ongoing development"
                ),
                budget_outline=(
                    "Year 1: Rs. 40-50 lakh\n"
                    "- Developer salaries (3-5 people, 12 months): Rs. 30 lakh\n"
                    "- Cloud infrastructure: Rs. 5 lakh\n"
                    "- Data acquisition and RTI filing: Rs. 3 lakh\n"
                    "- Campus events and outreach: Rs. 5 lakh\n"
                    "- Administration: Rs. 5 lakh"
                ),
                impact_metrics=[
                    "Number of tools deployed",
                    "GitHub stars and community contributors",
                    "RTIs filed using the system",
                    "Facilities mapped",
                    "Citizen reports processed",
                ],
                alignment_with_csr_act=(
                    "Eligible under Companies Act 2013, Section 135, Schedule VII:\n"
                    "- Item (iv): Environmental sustainability (factory farm monitoring)\n"
                    "- Item (ix): Technology incubation (open-source development)\n"
                    "- Animal welfare: Explicitly mentioned in Schedule VII\n"
                    "- Item (ii): Education (campus programme)"
                ),
            ),
        }

        return proposals.get(focus_area, proposals["food_safety"])

    def talking_points_for_campus_meetings(self) -> dict:
        """Key talking points for meeting with campus administration."""
        return {
            "mess_committee": [
                "Request transparent sourcing information for dairy and eggs in campus mess",
                "Propose weekly plant-based menu options (not 'vegan day' — that's alienating)",
                "Request FSSAI test reports for milk supplied to campus",
                "Cite IIT Bombay, IIT Delhi examples of expanded plant-based options",
                "Cost argument: plant protein (dal, soy) is CHEAPER than animal protein",
            ],
            "research_ethics_board": [
                "Review of animal testing protocols in research labs",
                "Propose alignment with CPCSEA (Committee for the Purpose of Control and "
                "Supervision of Experiments on Animals) guidelines",
                "Advocate for 3Rs: Replacement, Reduction, Refinement",
                "Highlight computational alternatives available in 2026",
            ],
            "sustainability_cell": [
                "Carbon footprint audit of campus food procurement",
                "Water footprint analysis: dairy vs. plant-based in campus kitchen",
                "Align with campus sustainability goals (most IITs have these)",
                "Propose pilot: one semester tracking environmental impact of food choices",
            ],
            "placement_cell": [
                "CSR proposal templates for visiting companies (see csr_proposal_template)",
                "Frame animal welfare tech as a career opportunity (GFI India, alt-protein startups)",
                "Highlight companies with animal welfare commitments for placement talks",
            ],
        }
