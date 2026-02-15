"""
Legal Database for Indian Animal Advocacy

Comprehensive database of constitutional provisions, statutes, rules, and
landmark judicial decisions relevant to animal welfare litigation in India.

Key legal instruments:
- Constitution: Articles 48, 48A, 51A(g), 21 (expanded to animal right to life)
- Prevention of Cruelty to Animals Act, 1960 (PCA Act)
- Transport of Livestock Rules, 1978 & 2001
- Slaughter House Rules, 2001
- Food Safety and Standards Act, 2006
- Environment Protection Act, 1986
- Wildlife Protection Act, 1972
- State-specific cattle preservation/anti-slaughter laws
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LegalProvision:
    """A constitutional provision, statute section, or rule."""
    identifier: str
    title: str
    source: str
    text: str
    relevance: str
    advocacy_use: str
    related_cases: list[str] = field(default_factory=list)


@dataclass
class LandmarkCase:
    """A landmark judicial decision."""
    citation: str
    name: str
    court: str
    year: int
    judges: list[str]
    facts_summary: str
    holding: str
    key_principles: list[str]
    relevance_to_advocacy: str
    full_citation: str


CONSTITUTIONAL_PROVISIONS = {
    "article_48": LegalProvision(
        identifier="Article 48",
        title="Organisation of Agriculture and Animal Husbandry",
        source="Constitution of India, Part IV (Directive Principles)",
        text=(
            "The State shall endeavour to organise agriculture and animal husbandry "
            "on modern and scientific lines and shall, in particular, take steps for "
            "preserving and improving the breeds, and prohibiting the slaughter, of "
            "cows and calves and other milch and draught cattle."
        ),
        relevance=(
            "Directive Principle. Not directly enforceable but guides state policy. "
            "Used in conjunction with Article 51A(g) to establish constitutional "
            "concern for animal welfare. Supreme Court has increasingly given "
            "weight to DPSPs in animal welfare matters."
        ),
        advocacy_use=(
            "Cite in PILs to establish constitutional mandate for animal protection. "
            "Useful for challenging inadequate implementation of welfare standards. "
            "Note: This article has been used both by animal welfare advocates AND "
            "by cow protection movements — frame carefully to avoid entanglement "
            "with communal politics."
        ),
        related_cases=[
            "State of Gujarat v. Mirzapur Moti Kureshi Kassab Jamat (2005) 8 SCC 534",
            "AWBI v. A. Nagaraja (2014) 7 SCC 547",
        ],
    ),
    "article_48a": LegalProvision(
        identifier="Article 48A",
        title="Protection and Improvement of Environment",
        source="Constitution of India, Part IV (Directive Principles)",
        text=(
            "The State shall endeavour to protect and improve the environment and "
            "to safeguard the forests and wild life of the country."
        ),
        relevance=(
            "Environmental DPSP. Basis for challenging pollution from factory farms "
            "and industrial animal agriculture operations."
        ),
        advocacy_use=(
            "Pair with Article 21 (right to clean environment) in PILs against "
            "polluting poultry farms, dairy operations, and slaughterhouses. "
            "Especially effective when combined with PCB data from RTI responses."
        ),
        related_cases=[
            "M.C. Mehta v. Union of India (1987) 1 SCC 395",
        ],
    ),
    "article_51a_g": LegalProvision(
        identifier="Article 51A(g)",
        title="Fundamental Duty — Compassion for Living Creatures",
        source="Constitution of India, Part IVA (Fundamental Duties)",
        text=(
            "It shall be the duty of every citizen of India to protect and improve "
            "the natural environment including forests, lakes, rivers and wild life, "
            "and to have compassion for living creatures."
        ),
        relevance=(
            "The only explicit constitutional reference to compassion for animals. "
            "Supreme Court in AWBI v. Nagaraja elevated this from mere duty to a "
            "source of animal rights. 'Compassion for living creatures' has been "
            "interpreted to include a duty to prevent unnecessary suffering."
        ),
        advocacy_use=(
            "CRITICAL provision. The Nagaraja court used this to derive animal "
            "rights from the Constitution. Cite in every PIL. This is the "
            "constitutional anchor for the argument that animals have rights "
            "under Indian law, not merely that humans have duties toward them."
        ),
        related_cases=[
            "AWBI v. A. Nagaraja (2014) 7 SCC 547",
            "People for Animals v. State of Goa (1997)",
        ],
    ),
    "article_21": LegalProvision(
        identifier="Article 21",
        title="Right to Life and Personal Liberty",
        source="Constitution of India, Part III (Fundamental Rights)",
        text=(
            "No person shall be deprived of his life or personal liberty except "
            "according to procedure established by law."
        ),
        relevance=(
            "The Supreme Court in Nagaraja expanded 'life' under Article 21 to "
            "include animal life, holding that animals have a right to live with "
            "dignity. Also relevant for human right to clean environment (pollution "
            "from factory farms) and right to safe food (adulteration)."
        ),
        advocacy_use=(
            "Use for dual-track arguments: (1) animals' own right to life with "
            "dignity, and (2) human communities' right to clean environment "
            "impacted by factory farm pollution."
        ),
        related_cases=[
            "AWBI v. A. Nagaraja (2014) 7 SCC 547",
            "M.C. Mehta v. Union of India (1987) 1 SCC 395",
        ],
    ),
}


STATUTES = {
    "pca_act_1960": LegalProvision(
        identifier="Prevention of Cruelty to Animals Act, 1960",
        title="PCA Act, 1960",
        source="Act No. 59 of 1960, Parliament of India",
        text=(
            "Primary animal welfare legislation. Defines cruelty (Section 11), "
            "establishes AWBI (Section 4), regulates experimentation (Chapter IV), "
            "and provides for penalties. Key sections:\n"
            "- Section 3: Duty of persons having charge of animals\n"
            "- Section 11: Treating animals cruelly (defines 12 forms of cruelty)\n"
            "- Section 11(1)(a): Beating, kicking, overloading, torturing\n"
            "- Section 11(1)(d): Carrying in a vehicle causing unnecessary suffering\n"
            "- Section 11(1)(e): Keeping in a cage not adequate in size\n"
            "- Section 11(1)(h): Neglecting to provide food, water, shelter\n"
            "- Section 38: Power to make rules (basis for Transport Rules, Slaughter Rules)\n"
            "- Penalty: First offence Rs. 10-50, subsequent Rs. 25-100 (woefully inadequate)"
        ),
        relevance=(
            "Primary statute. Penalties are pathetically low (max Rs. 100 for repeat "
            "offence). Amendment bills to increase penalties have been pending for years. "
            "The inadequacy of penalties is itself an advocacy point. However, the Act "
            "combined with IPC Sections 428/429 (mischief by killing/maiming animals, "
            "up to 5 years imprisonment) provides stronger enforcement tools."
        ),
        advocacy_use=(
            "File FIRs under Section 11 read with IPC 428/429 for serious cruelty. "
            "Use Section 11(1)(d) and (e) for transport and housing conditions. "
            "Challenge the Rs. 50/100 penalty ceiling in PIL as violating Article 21 "
            "rights of animals. Cite Nagaraja for constitutional backing."
        ),
        related_cases=[
            "AWBI v. A. Nagaraja (2014) 7 SCC 547",
            "N.R. Nair v. Union of India (2001) 6 SCC 84",
        ],
    ),
    "transport_rules_1978": LegalProvision(
        identifier="Prevention of Cruelty to Animals (Transport of Livestock) Rules, 1978",
        title="Livestock Transport Rules, 1978",
        source="Notified under Section 38 of PCA Act, 1960",
        text=(
            "Regulates transport of cattle, sheep, goats, and poultry. Key rules:\n"
            "- Rule 4: Certificate of fitness from veterinary doctor required\n"
            "- Rule 5: Animals must be provided with adequate food and water\n"
            "- Rule 6: Diseased/blind/emaciated/about-to-give-birth animals cannot be transported\n"
            "- Rule 7: Vehicle specifications — adequate ventilation, non-slip flooring\n"
            "- Rule 8: Maximum number of animals per vehicle\n"
            "- Rule 9: Animals not to be transported for more than 36 hours without rest/feed\n"
            "- Rule 47: Poultry specific — max 4 birds per coop of 60x45x30 cm"
        ),
        relevance=(
            "Widely violated across India. Transport conditions for poultry (legs tied, "
            "crammed in baskets, driven in open trucks) and cattle (overcrowded, no water) "
            "routinely violate these rules. Key enforcement tool."
        ),
        advocacy_use=(
            "Document transport violations with video/photo evidence. File complaints "
            "under PCA Act Section 11(1)(d). RTI for enforcement data. PIL for "
            "systemic non-compliance."
        ),
    ),
    "transport_rules_2001": LegalProvision(
        identifier="Prevention of Cruelty to Animals (Transport of Animals on Foot) Rules, 2001",
        title="Transport on Foot Rules, 2001",
        source="Notified under Section 38 of PCA Act, 1960",
        text=(
            "Regulates transport of animals on foot (drove/walking). Key rules:\n"
            "- Rule 3: Animals must be fit for transport, certified by veterinarian\n"
            "- Rule 5: Maximum distance 25 km per day\n"
            "- Rule 6: Rest at intervals not exceeding 5 hours\n"
            "- Rule 7: Adequate feed, water, and rest at halting places\n"
            "- Rule 9: Animals not to be tied with nose ropes that cause pain\n"
            "- Rule 11: Branding prohibited (only ear-tagging permitted)"
        ),
        relevance=(
            "Still relevant for rural livestock markets (haats) and transport "
            "from markets to slaughterhouses. Violations common at weekly cattle "
            "markets across India."
        ),
        advocacy_use=(
            "Monitor weekly cattle/livestock markets for violations. Document "
            "and file complaints. Useful for challenging the claim that "
            "traditional markets are 'humane.'"
        ),
    ),
    "slaughter_house_rules_2001": LegalProvision(
        identifier="Prevention of Cruelty to Animals (Slaughter House) Rules, 2001",
        title="Slaughter House Rules, 2001",
        source="Notified under Section 38 of PCA Act, 1960",
        text=(
            "Regulates conditions at slaughterhouses. Key rules:\n"
            "- Rule 3: Registration/license mandatory from local authority\n"
            "- Rule 3(2): Space, ventilation, water, drainage requirements\n"
            "- Rule 3(3): Separate areas for stunning, bleeding, dressing\n"
            "- Rule 4: Ante-mortem inspection by qualified veterinarian\n"
            "- Rule 5: Post-mortem examination of each carcass\n"
            "- Rule 6: Animals must be stunned before slaughter (humane killing)\n"
            "- Rule 6(2): No animal should be slaughtered in sight of another\n"
            "- Rule 7: Sick/pregnant/animals under 3 months not to be slaughtered\n"
            "- Rule 8: No slaughter between sunset and sunrise"
        ),
        relevance=(
            "Massively non-compliant. Most slaughterhouses in India, particularly "
            "in smaller towns, do not meet even basic requirements. Stunning is "
            "rarely practiced. Ante-mortem inspection is often absent."
        ),
        advocacy_use=(
            "RTI for compliance data. PIL for enforcement. Document conditions "
            "at specific facilities. Push for modernization and consolidation "
            "of illegal slaughter facilities into compliant ones."
        ),
    ),
    "fss_act_2006": LegalProvision(
        identifier="Food Safety and Standards Act, 2006",
        title="FSS Act, 2006",
        source="Act No. 34 of 2006, Parliament of India",
        text=(
            "Consolidated food safety law. Relevant sections:\n"
            "- Section 3(1)(n): Defines 'food safety' — assurance that food is acceptable\n"
            "- Section 26: Standards for articles of food (includes meat, dairy)\n"
            "- Section 31: Licensing and registration of food business operators\n"
            "- Section 32: Improvement notices\n"
            "- Section 38: Power of Food Safety Officers to inspect\n"
            "- Section 59: Punishment for unsafe food (6 months to life imprisonment)\n"
            "- Section 63: Operating without license — Rs. 5 lakhs fine\n"
            "- Schedule 4, Part V: Specific standards for slaughterhouses"
        ),
        relevance=(
            "Provides stronger penalties than PCA Act. Unlicensed operation alone "
            "carries Rs. 5 lakh fine. Unsafe food can mean life imprisonment. "
            "Powerful tool for meat and dairy advocacy."
        ),
        advocacy_use=(
            "Use food safety angle to access facilities that resist welfare "
            "inspections. RTI for FSSAI inspection and violation data. "
            "File complaints about unlicensed meat/dairy operations."
        ),
    ),
    "environment_protection_act_1986": LegalProvision(
        identifier="Environment (Protection) Act, 1986",
        title="EPA, 1986",
        source="Act No. 29 of 1986, Parliament of India",
        text=(
            "Umbrella environmental legislation. Relevant provisions:\n"
            "- Section 3: Power to take measures for environmental protection\n"
            "- Section 5: Power to issue directions (closure, prohibition)\n"
            "- Section 7: No person shall carry on industry causing environmental pollution\n"
            "- Section 15: Penalty — imprisonment up to 5 years and fine up to Rs. 1 lakh,\n"
            "  continuing offence Rs. 5,000 per day\n"
            "- EIA Notification, 2006: Environmental clearance requirements"
        ),
        relevance=(
            "Factory farms and slaughterhouses are industrial operations with "
            "significant environmental impact. CPCB classifies slaughterhouses as "
            "'Red' category and large poultry farms as 'Orange' category."
        ),
        advocacy_use=(
            "File complaints with NGT (National Green Tribunal) for polluting "
            "animal agriculture. Use EIA requirements to challenge new factory "
            "farm approvals. Combine with RTI pollution data."
        ),
    ),
}


LANDMARK_CASES = {
    "nagaraja_2014": LandmarkCase(
        citation="(2014) 7 SCC 547",
        name="Animal Welfare Board of India v. A. Nagaraja & Ors.",
        court="Supreme Court of India",
        year=2014,
        judges=["K.S. Radhakrishnan", "Pinaki Chandra Ghose"],
        facts_summary=(
            "Challenge to jallikattu (bull-taming) in Tamil Nadu and bullock-cart "
            "races in Maharashtra. AWBI argued these practices cause suffering "
            "and violate the PCA Act."
        ),
        holding=(
            "Banned jallikattu and bullock-cart races. Held that animals have "
            "constitutional rights — the right to live with dignity, a right "
            "to their lives, and the right not to be tortured. This is the "
            "most significant animal rights judgment in Indian legal history."
        ),
        key_principles=[
            "Animals are not merely property; they have intrinsic worth.",
            "Article 51A(g) casts a duty on every citizen to have compassion for living creatures.",
            "The five freedoms (from hunger, discomfort, pain, fear, and to express normal behaviour) "
            "are to be read into the PCA Act.",
            "Article 21 protection of life extends to animal life.",
            "Every species has a right to life and security, subject to the law of the land.",
            "Parliament must consider amending PCA Act penalties (currently too low).",
        ],
        relevance_to_advocacy=(
            "THE foundational case. Every PIL should cite Nagaraja. It establishes "
            "that animals have constitutional rights under Articles 21 and 51A(g). "
            "Use the five freedoms framework from this judgment as the standard "
            "against which all animal agriculture practices should be measured."
        ),
        full_citation=(
            "Animal Welfare Board of India v. A. Nagaraja & Ors., "
            "(2014) 7 SCC 547, decided on 07.05.2014"
        ),
    ),
    "people_for_animals_goa": LandmarkCase(
        citation="1997 (unreported), Bombay High Court (Goa Bench)",
        name="People for Animals v. State of Goa",
        court="Bombay High Court, Goa Bench",
        year=1997,
        judges=[],
        facts_summary=(
            "Challenge to bull fights (dhirio) organized in Goa. People for Animals "
            "filed petition arguing the practice violated PCA Act."
        ),
        holding=(
            "Banned bull fights in Goa, holding that the practice constituted "
            "cruelty under the PCA Act and violated Article 51A(g)."
        ),
        key_principles=[
            "Traditional/cultural practices do not override statutory prohibition of cruelty.",
            "Article 51A(g) duty of compassion applies to all entertainment involving animals.",
        ],
        relevance_to_advocacy=(
            "Establishes that cultural/traditional framing does not excuse cruelty. "
            "Applicable to arguments that dairy farming is 'traditional' or 'Indian culture.'"
        ),
        full_citation="People for Animals v. State of Goa, Bombay High Court (Goa Bench), 1997",
    ),
    "nr_nair_2001": LandmarkCase(
        citation="(2001) 6 SCC 84",
        name="N.R. Nair & Ors v. Union of India & Ors",
        court="Supreme Court of India (Kerala High Court affirmed)",
        year=2001,
        judges=[],
        facts_summary=(
            "Challenge to use of animals in circuses. AWBI and animal welfare "
            "organizations argued circus conditions violated PCA Act."
        ),
        holding=(
            "Upheld restrictions on use of certain animals in circuses. Held that "
            "animals performing in circuses suffer cruelty and the state has duty "
            "to protect them. Led to eventual prohibition of wild animals in circuses."
        ),
        key_principles=[
            "Animals are entitled to be treated with dignity even in captivity.",
            "State has positive obligation to prevent animal cruelty.",
            "Commercial use of animals must comply with welfare standards.",
        ],
        relevance_to_advocacy=(
            "Establishes state's positive obligation to prevent cruelty. Applicable "
            "to factory farming — if the state must protect circus animals, it must "
            "protect farm animals."
        ),
        full_citation="N.R. Nair & Ors v. Union of India & Ors, (2001) 6 SCC 84",
    ),
    "gauri_maulekhi_2016": LandmarkCase(
        citation="W.P.(C) No. 881/2014",
        name="Gauri Maulekhi v. Union of India",
        court="Supreme Court of India",
        year=2016,
        judges=[],
        facts_summary=(
            "PIL challenging illegal cattle transport from India to Nepal for "
            "Gadhimai festival sacrifice. Sought enforcement of Transport Rules."
        ),
        holding=(
            "Directed strict enforcement of Transport of Livestock Rules, 1978 "
            "and 2001. Directed state governments to ensure no illegal transport "
            "of cattle across the India-Nepal border."
        ),
        key_principles=[
            "Transport of livestock rules must be strictly enforced at border checkpoints.",
            "State governments bear responsibility for preventing illegal cattle transport.",
            "Inter-state movement of cattle requires compliance with transport rules.",
        ],
        relevance_to_advocacy=(
            "Key case for transport enforcement. Use to argue for stricter "
            "enforcement of transport rules for all livestock, not just cross-border."
        ),
        full_citation=(
            "Gauri Maulekhi v. Union of India & Ors, W.P.(C) No. 881/2014, "
            "Supreme Court of India"
        ),
    ),
    "laxmi_narain_modi_2013": LandmarkCase(
        citation="SLP (Criminal) No. 5765 of 2008",
        name="Laxmi Narain Modi v. Union of India",
        court="Supreme Court of India",
        year=2013,
        judges=[],
        facts_summary=(
            "Challenge to slaughter of animals for food, specifically the "
            "practice at slaughterhouses operating without proper licenses."
        ),
        holding=(
            "Directed all state governments to ensure that slaughterhouses "
            "comply with the Food Safety and Standards Act, 2006 and PCA "
            "Slaughter House Rules, 2001. Directed closure of illegal/unlicensed "
            "slaughterhouses."
        ),
        key_principles=[
            "All slaughterhouses must be licensed under both FSS Act and municipal laws.",
            "State governments must take action against illegal slaughterhouses.",
            "Compliance with Slaughter House Rules 2001 is mandatory, not advisory.",
        ],
        relevance_to_advocacy=(
            "Direct authority for demanding closure of unlicensed slaughterhouses. "
            "Use RTI data on licensing to file enforcement petitions citing this case."
        ),
        full_citation=(
            "Laxmi Narain Modi v. Union of India, SLP (Criminal) No. 5765/2008, "
            "Supreme Court of India, 2013"
        ),
    ),
    "mirzapur_2005": LandmarkCase(
        citation="(2005) 8 SCC 534",
        name="State of Gujarat v. Mirzapur Moti Kureshi Kassab Jamat & Ors",
        court="Supreme Court of India",
        year=2005,
        judges=["R.C. Lahoti (CJI)", "B.N. Agrawal", "A.R. Lakshmanan",
                "Arijit Pasayat", "S.H. Kapadia", "C.K. Thakker", "P.K. Balasubramanyan"],
        facts_summary=(
            "Constitutional challenge to Gujarat's total ban on cow slaughter "
            "(including bulls and bullocks). Seven-judge bench."
        ),
        holding=(
            "Upheld the total ban on slaughter of cows, bulls, and bullocks. "
            "Held that Article 48 read with Articles 48A and 51A(g) provides "
            "sufficient constitutional basis. Overruled the earlier 1958 "
            "Mohd. Hanif Quareshi decision (which allowed slaughter of "
            "economically useless cattle)."
        ),
        key_principles=[
            "Total ban on cow/bull/bullock slaughter is constitutionally valid.",
            "DPSPs (Article 48) have become increasingly significant and can restrict fundamental rights.",
            "Cattle have economic utility throughout their lives (dung, biogas, etc.).",
        ],
        relevance_to_advocacy=(
            "CAUTION: This case has been heavily used by cow vigilante groups. "
            "Animal welfare advocates should cite it carefully and always distinguish "
            "genuine animal welfare from communal violence. The welfare principles are "
            "sound; the political weaponization is dangerous. Best used for its DPSP "
            "analysis rather than its specific slaughter ban holding."
        ),
        full_citation=(
            "State of Gujarat v. Mirzapur Moti Kureshi Kassab Jamat & Ors, "
            "(2005) 8 SCC 534, decided on 26.10.2005"
        ),
    ),
}


class LegalDatabase:
    """
    Searchable database of Indian animal welfare law.

    Provides access to constitutional provisions, statutes, rules,
    and landmark cases for PIL research and advocacy.
    """

    def __init__(self):
        self.provisions = CONSTITUTIONAL_PROVISIONS
        self.statutes = STATUTES
        self.cases = LANDMARK_CASES

    def get_provision(self, key: str) -> Optional[LegalProvision]:
        """Get a constitutional provision by key."""
        return self.provisions.get(key)

    def get_statute(self, key: str) -> Optional[LegalProvision]:
        """Get a statute by key."""
        return self.statutes.get(key)

    def get_case(self, key: str) -> Optional[LandmarkCase]:
        """Get a landmark case by key."""
        return self.cases.get(key)

    def search(self, query: str) -> dict:
        """Search across all legal materials for a keyword."""
        query_lower = query.lower()
        results = {"provisions": [], "statutes": [], "cases": []}

        for key, prov in self.provisions.items():
            if (query_lower in prov.text.lower() or
                    query_lower in prov.relevance.lower() or
                    query_lower in prov.title.lower()):
                results["provisions"].append(key)

        for key, stat in self.statutes.items():
            if (query_lower in stat.text.lower() or
                    query_lower in stat.relevance.lower() or
                    query_lower in stat.title.lower()):
                results["statutes"].append(key)

        for key, case in self.cases.items():
            if (query_lower in case.holding.lower() or
                    query_lower in case.facts_summary.lower() or
                    query_lower in case.name.lower() or
                    any(query_lower in p.lower() for p in case.key_principles)):
                results["cases"].append(key)

        return results

    def get_pil_citations(self, topic: str) -> dict:
        """Get recommended citations for a PIL topic."""
        topic_lower = topic.lower()

        citations = {
            "constitutional": [],
            "statutory": [],
            "case_law": [],
        }

        # Always include core provisions
        citations["constitutional"].append(self.provisions["article_51a_g"])
        citations["constitutional"].append(self.provisions["article_21"])

        if any(w in topic_lower for w in ["transport", "vehicle", "road"]):
            citations["statutory"].append(self.statutes["transport_rules_1978"])
            citations["statutory"].append(self.statutes["transport_rules_2001"])
            citations["case_law"].append(self.cases["gauri_maulekhi_2016"])

        if any(w in topic_lower for w in ["slaughter", "meat", "killing"]):
            citations["statutory"].append(self.statutes["slaughter_house_rules_2001"])
            citations["statutory"].append(self.statutes["fss_act_2006"])
            citations["case_law"].append(self.cases["laxmi_narain_modi_2013"])

        if any(w in topic_lower for w in ["pollution", "environment", "water", "effluent"]):
            citations["constitutional"].append(self.provisions["article_48a"])
            citations["statutory"].append(self.statutes["environment_protection_act_1986"])

        if any(w in topic_lower for w in ["cruelty", "welfare", "suffering", "dairy", "poultry"]):
            citations["statutory"].append(self.statutes["pca_act_1960"])

        # Always include Nagaraja
        citations["case_law"].append(self.cases["nagaraja_2014"])

        return citations

    def list_all_cases(self) -> list[str]:
        """List all case keys."""
        return list(self.cases.keys())

    def list_all_statutes(self) -> list[str]:
        """List all statute keys."""
        return list(self.statutes.keys())

    def list_all_provisions(self) -> list[str]:
        """List all constitutional provision keys."""
        return list(self.provisions.keys())
