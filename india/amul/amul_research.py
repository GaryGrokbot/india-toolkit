"""
Amul/GCMMF Counter-Narrative Research Database

The Gujarat Cooperative Milk Marketing Federation (GCMMF), which markets
under the Amul brand, is the world's largest dairy cooperative and India's
most powerful dairy institution. Revenue: ~Rs. 72,000 crore (FY2023-24).

Amul's public narrative: "By the farmers, for the farmers."
The reality: Industrial-scale dairy with cooperative branding.

This database provides factual counter-narratives to Amul's marketing,
grounded in data from GCMMF's own reports, government data, and
independent research.

IMPORTANT: All claims must be sourced and verifiable. Do not overstate.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ResearchPoint:
    """A single research finding with source."""
    claim: str
    evidence: str
    source: str
    source_year: Optional[int] = None
    counter_narrative: str = ""
    amul_response: str = ""  # What Amul would likely say in response
    rebuttal: str = ""  # Rebuttal to Amul's likely response


AMUL_PROFILE = {
    "full_name": "Gujarat Cooperative Milk Marketing Federation Ltd (GCMMF)",
    "brand": "Amul (Anand Milk Union Limited)",
    "headquarters": "Amul Dairy Road, Anand - 388001, Gujarat",
    "managing_director": "Jayen Mehta (as of 2024)",
    "chairman": "Shamalbhai Patel (as of 2024)",  # Verify current
    "founded": 1946,  # Kaira District Cooperative
    "gcmmf_formed": 1973,
    "member_unions": 18,  # Gujarat district unions
    "village_cooperatives": 18_700,  # approximate
    "farmer_members": 3_600_000,  # 3.6 million
    "daily_milk_collection_litres": 26_000_000,  # ~26 million litres/day
    "revenue_fy2024_crore": 72_000,  # approximate
    "products": 90,  # 90+ dairy products
    "plants": 90,  # processing and packaging plants
    "operation_flood": "Amul model was replicated nationally through Operation Flood (1970-1996), "
                       "funded by World Bank and European dairy surplus. Dr. Verghese Kurien led this.",
}


RESEARCH_DATABASE = {
    "cooperative_vs_industrial": ResearchPoint(
        claim=(
            "Amul markets itself as a small-farmer cooperative but operates at "
            "industrial scale with 3.6 million members, 26 million litres/day "
            "collection, and Rs. 72,000 crore annual revenue."
        ),
        evidence=(
            "GCMMF Annual Report and press releases consistently cite these figures. "
            "This makes Amul larger than many Fortune 500 companies. The cooperative "
            "structure does not mean the operations are small-scale — milk collection, "
            "chilling, processing, and distribution are fully industrialized."
        ),
        source="GCMMF Annual Report, FY2023-24",
        source_year=2024,
        counter_narrative=(
            "Amul is not your grandmother's gaushala. It's a Rs. 72,000 crore "
            "industrial operation with 26 million litres of milk flowing through "
            "its system every single day. The cooperative label is real — but the "
            "scale is industrial."
        ),
        amul_response="We are a cooperative owned by 3.6 million farmers. Every paisa goes back to them.",
        rebuttal=(
            "The cooperative structure means profits are distributed, yes. But the "
            "production model — continuous impregnation cycles, high-yield crossbreeds, "
            "intensive feeding regimes — is no different from any industrial dairy. "
            "The animals don't experience 'cooperative' differently from 'corporate.'"
        ),
    ),
    "male_calf_crisis": ResearchPoint(
        claim=(
            "The Amul dairy system produces millions of male calves annually who "
            "cannot produce milk and are economically unviable. These calves are "
            "abandoned, sold to informal slaughter, or left to starve."
        ),
        evidence=(
            "With 3.6 million member farmers and continuous breeding cycles, the "
            "Amul system generates an estimated 4-5 million calves per year in "
            "Gujarat alone. Male calves (roughly 50%) have no economic value in a "
            "dairy system. AWBI and animal welfare organizations have documented "
            "widespread male calf abandonment in Gujarat's dairy belt. "
            "The 20th Livestock Census (2019) shows Gujarat has 10.4 million cattle "
            "but the male:female ratio in dairy breeds is severely skewed — "
            "indicating systematic removal of males."
        ),
        source="20th Livestock Census 2019; AWBI reports; field investigations by animal welfare groups",
        source_year=2019,
        counter_narrative=(
            "For every litre of Amul milk, a calf was separated from its mother. "
            "Half of those calves are male. Where do millions of male calves go "
            "in a system that has no use for them? Amul's marketing shows happy "
            "cows. It never shows the missing calves."
        ),
        amul_response=(
            "We encourage farmers to raise male calves for draught purposes. "
            "Rashtriya Gokul Mission supports indigenous breed conservation."
        ),
        rebuttal=(
            "Draught animal use has collapsed with mechanization. Male crossbred calves "
            "(HF/Jersey crosses that Amul's AI programme produces) have no draught value. "
            "RGM's own data (available via RTI) would show what happens to these calves. "
            "The economics are clear: feeding a male calf costs Rs. 50-80/day, and the "
            "farmer earns nothing from it. The calf disappears."
        ),
    ),
    "artificial_insemination": ResearchPoint(
        claim=(
            "Amul's model depends on artificial insemination (AI) to continuously "
            "impregnate cows and buffaloes, often with imported Holstein-Friesian "
            "or Jersey semen to increase milk yield."
        ),
        evidence=(
            "GCMMF actively promotes AI through its village cooperatives. Gujarat "
            "has one of the highest AI coverage rates in India. The Rashtriya Gokul "
            "Mission subsidizes AI infrastructure. DAHD data shows Gujarat performs "
            "millions of AIs annually. Crossbreeding with exotic breeds (HF, Jersey) "
            "is explicitly promoted for higher milk yield."
        ),
        source="DAHD Annual Report; RGM progress reports; GCMMF promotional materials",
        counter_narrative=(
            "Amul's 'Taste of India' runs on artificial insemination — forcibly "
            "impregnating cows and buffaloes on a schedule dictated by milk demand, "
            "not animal welfare. The cows are breeding machines."
        ),
        amul_response="AI is a scientific advancement that benefits farmers by improving breed quality.",
        rebuttal=(
            "AI eliminates the cow's choice entirely. It serves milk production targets, "
            "not animal welfare. Combined with crossbreeding, it creates animals optimized "
            "for yield but prone to health issues — lameness, mastitis, metabolic disorders. "
            "The animal pays the price for human efficiency."
        ),
    ),
    "antibiotic_use": ResearchPoint(
        claim=(
            "The intensive dairy system that Amul depends on involves significant "
            "antibiotic use, particularly for treating mastitis, a painful udder "
            "infection caused by intensive milking."
        ),
        evidence=(
            "Mastitis is the most common disease in Indian dairy cattle. Studies "
            "in Gujarat dairy farms have found antibiotic residues in milk samples. "
            "The Indian Network for Surveillance of Antimicrobial Resistance (INSAR) "
            "has flagged agricultural antibiotic use as a contributor to AMR. "
            "FSSAI has set MRLs (Maximum Residue Limits) for antibiotics in milk, "
            "implicitly acknowledging the problem."
        ),
        source="INSAR reports; FSSAI regulations on antibiotic MRLs; published veterinary studies in Indian Journal of Animal Sciences",
        counter_narrative=(
            "India's dairy cows are pumped with antibiotics to keep producing milk "
            "despite infections caused by the production system itself. These "
            "antibiotics end up in your glass. WHO calls antibiotic resistance "
            "'one of the biggest threats to global health.'"
        ),
    ),
    "water_footprint": ResearchPoint(
        claim=(
            "The Amul dairy system in Gujarat contributes significantly to "
            "groundwater depletion in one of India's most water-stressed states."
        ),
        evidence=(
            "Gujarat's Banaskantha district (largest Amul union, Banas Dairy) "
            "shows severe groundwater depletion. CGWB data indicates falling water "
            "tables across dairy-intensive districts. Fodder production (lucerne, "
            "maize, bajra) for dairy is water-intensive. Processing plants (Amul "
            "has 90+) also consume significant water."
        ),
        source="CGWB monitoring data; Gujarat State Water Data Centre; NITI Aayog Composite Water Management Index",
        counter_narrative=(
            "Banaskantha is Gujarat's biggest milk district and also one of its "
            "most water-stressed. The water that goes into growing fodder, feeding "
            "cattle, and running Amul's 90+ plants is water that communities need "
            "for drinking. At 1000+ litres per litre of milk, is this sustainable?"
        ),
    ),
    "oxytocin_use": ResearchPoint(
        claim=(
            "Oxytocin injection for milk let-down has been widespread in Indian "
            "dairy, causing health issues in animals and potential residues in milk."
        ),
        evidence=(
            "Government of India banned retail sale of oxytocin in 2018 "
            "(restricted to registered hospitals and vet clinics) specifically "
            "because of widespread misuse in dairy. Prior to the ban, oxytocin "
            "was freely available and routinely injected to force milk let-down. "
            "Enforcement of the ban remains weak, per FSSAI and CDSCO reports."
        ),
        source="CDSCO notification 2018; Parliamentary Committee on Agriculture reports; investigative journalism (various)",
        source_year=2018,
        counter_narrative=(
            "The government had to ban oxytocin retail sales because dairy farmers "
            "were injecting it into cows to force milk production. The ban exists — "
            "but enforcement is minimal. The practice continues."
        ),
    ),
    "operation_flood_legacy": ResearchPoint(
        claim=(
            "Operation Flood (1970-1996), which replicated the Amul model nationally, "
            "was funded by European dairy surplus (donated milk powder and butter oil) "
            "and World Bank loans. It created India's dairy dependency."
        ),
        evidence=(
            "Operation Flood received EEC (European Economic Community) dairy surplus "
            "worth hundreds of crores, monetized through domestic sale to fund "
            "cooperative infrastructure. World Bank provided loans of $150 million+ "
            "across three phases. Critics (Shanti George, Claude Alvares) argued it "
            "made India dependent on dairy, undermined traditional food systems, and "
            "primarily benefited middle-to-large farmers."
        ),
        source="World Bank project documents; Shanti George, 'Operation Flood' (1985); Claude Alvares critiques",
        counter_narrative=(
            "India's dairy revolution wasn't organic — it was engineered by European "
            "dairy surplus and World Bank loans. Operation Flood took Europe's excess "
            "butter and created India's dairy dependency. It was an export of the "
            "European production model, not a grassroots movement."
        ),
    ),
}


class AmulResearchDB:
    """
    Research database for Amul/GCMMF counter-narratives.

    All claims are sourced and designed to withstand scrutiny.
    The goal is factual counter-narrative, not propaganda.
    """

    def __init__(self):
        self.profile = AMUL_PROFILE
        self.research = RESEARCH_DATABASE

    def get_profile(self) -> dict:
        """Get Amul/GCMMF corporate profile."""
        return self.profile

    def get_research_point(self, key: str) -> Optional[ResearchPoint]:
        """Get a specific research point."""
        return self.research.get(key)

    def list_research_topics(self) -> list[str]:
        """List all research topic keys."""
        return list(self.research.keys())

    def search(self, query: str) -> list[str]:
        """Search research database for a keyword."""
        query_lower = query.lower()
        results = []
        for key, point in self.research.items():
            if (query_lower in point.claim.lower() or
                    query_lower in point.evidence.lower() or
                    query_lower in point.counter_narrative.lower()):
                results.append(key)
        return results

    def get_all_counter_narratives(self) -> dict[str, str]:
        """Get all counter-narratives as a dict."""
        return {
            key: point.counter_narrative
            for key, point in self.research.items()
            if point.counter_narrative
        }

    def get_all_with_rebuttals(self) -> list[dict]:
        """Get all research points that have rebuttals to Amul's likely responses."""
        results = []
        for key, point in self.research.items():
            if point.amul_response and point.rebuttal:
                results.append({
                    "topic": key,
                    "claim": point.claim,
                    "amul_likely_response": point.amul_response,
                    "our_rebuttal": point.rebuttal,
                    "source": point.source,
                })
        return results

    def fact_sheet(self) -> str:
        """Generate a text fact sheet about Amul for advocacy use."""
        lines = [
            "AMUL / GCMMF FACT SHEET",
            "=" * 50,
            "",
            f"Full Name: {self.profile['full_name']}",
            f"Brand: {self.profile['brand']}",
            f"HQ: {self.profile['headquarters']}",
            f"Founded: {self.profile['founded']}",
            f"GCMMF Formed: {self.profile['gcmmf_formed']}",
            f"Revenue (FY24): Rs. {self.profile['revenue_fy2024_crore']:,} crore",
            f"Member Unions: {self.profile['member_unions']}",
            f"Farmer Members: {self.profile['farmer_members']:,}",
            f"Daily Collection: {self.profile['daily_milk_collection_litres']:,} litres",
            f"Processing Plants: {self.profile['plants']}+",
            f"Products: {self.profile['products']}+",
            "",
            "KEY ISSUES:",
            "",
        ]

        for key, point in self.research.items():
            lines.append(f"--- {key.replace('_', ' ').title()} ---")
            lines.append(f"Claim: {point.claim}")
            lines.append(f"Source: {point.source}")
            if point.counter_narrative:
                lines.append(f"Narrative: {point.counter_narrative}")
            lines.append("")

        return "\n".join(lines)
