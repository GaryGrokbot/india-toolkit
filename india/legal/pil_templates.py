"""
Public Interest Litigation (PIL) Templates for Animal Welfare

Generate PIL drafts for filing in High Courts and the Supreme Court of India.
Targets: dairy expansion, unlicensed slaughterhouses, transport violations,
CAFO (Concentrated Animal Feeding Operation) pollution.

PILs are filed under Article 226 (High Court) or Article 32 (Supreme Court).
Standing requirements are relaxed for genuine public interest matters.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class PILDraft:
    """A draft PIL petition."""
    title: str
    court: str
    petitioner: str
    respondents: list[str]
    grounds: list[str]
    prayers: list[str]
    constitutional_provisions: list[str]
    statutory_provisions: list[str]
    case_citations: list[str]
    facts: str
    urgency_note: Optional[str] = None
    generated_text: str = field(default="", repr=False)


class PILTemplateGenerator:
    """
    Generate PIL templates for animal welfare litigation in India.

    Templates are starting points — they MUST be reviewed and customized
    by a qualified advocate before filing.
    """

    def against_dairy_expansion(
        self,
        petitioner_name: str,
        petitioner_description: str,
        state: str,
        district: str,
        facility_details: str,
        environmental_data: str,
        animal_welfare_concerns: str,
        high_court: Optional[str] = None,
    ) -> PILDraft:
        """
        PIL against expansion of industrial dairy operations.

        Grounds: Environmental pollution, animal cruelty, violation of
        transport rules, water contamination, public health.
        """
        court = high_court or f"High Court of {state}"

        respondents = [
            f"State of {state}, through its Chief Secretary",
            "Union of India, through Secretary, Ministry of Environment, Forest and Climate Change",
            "Union of India, through Secretary, Department of Animal Husbandry and Dairying",
            f"State Pollution Control Board, {state}",
            f"District Collector, {district}",
            f"Animal Welfare Board of India, Chennai",
        ]

        grounds = [
            (
                "That the impugned dairy expansion violates the fundamental rights "
                "of animals to live with dignity as recognized by the Hon'ble Supreme "
                "Court in Animal Welfare Board of India v. A. Nagaraja, (2014) 7 SCC 547, "
                "which held that the five freedoms are to be read into the PCA Act, 1960."
            ),
            (
                "That industrial dairy operations involve systematic cruelty including "
                "continuous forced impregnation, separation of calves from mothers within "
                "hours of birth, confinement in spaces inadequate for natural behaviour, "
                "and abandonment or sale of male calves — all violating Section 11 of "
                "the Prevention of Cruelty to Animals Act, 1960."
            ),
            (
                "That the expansion will cause environmental pollution in violation of "
                "the Water (Prevention and Control of Pollution) Act, 1974, the Air "
                "(Prevention and Control of Pollution) Act, 1981, and Article 48A of "
                "the Constitution of India."
            ),
            (
                "That the State Pollution Control Board has failed to enforce "
                "environmental standards, including Consent to Operate conditions, "
                "effluent treatment requirements, and groundwater protection norms."
            ),
            (
                "That the expansion threatens the right to clean environment of "
                "residents under Article 21 of the Constitution, as recognized in "
                "M.C. Mehta v. Union of India, (1987) 1 SCC 395."
            ),
            (
                "That transport of cattle to and from the facility violates the "
                "Prevention of Cruelty to Animals (Transport of Livestock) Rules, 1978 "
                "and the Transport of Animals on Foot Rules, 2001."
            ),
            (
                "That the fundamental duty of compassion for living creatures under "
                "Article 51A(g) of the Constitution requires the State to prevent the "
                "industrialization of animal suffering for commercial profit."
            ),
        ]

        prayers = [
            (
                "Direct the Respondent State to conduct an independent environmental "
                "and animal welfare assessment of the impugned dairy expansion before "
                "granting any further approvals."
            ),
            (
                "Direct the State Pollution Control Board to strictly enforce "
                "environmental standards at all dairy operations in the district "
                "and take action against violators."
            ),
            (
                f"Direct the AWBI to conduct inspections of all commercial dairy "
                f"operations in {district} and report on compliance with animal "
                f"welfare standards including the five freedoms."
            ),
            (
                "Direct the Respondent State to formulate guidelines for maximum "
                "herd size, minimum space per animal, veterinary care standards, "
                "and calf welfare in commercial dairy operations."
            ),
            (
                "Pass any other order or direction as this Hon'ble Court may "
                "deem fit and proper in the facts and circumstances of the case."
            ),
        ]

        facts = (
            f"1. The Petitioner is {petitioner_description}.\n\n"
            f"2. The present Petition is being filed in public interest concerning "
            f"the welfare of animals and the environment in {district}, {state}.\n\n"
            f"3. Facility details: {facility_details}\n\n"
            f"4. Environmental data: {environmental_data}\n\n"
            f"5. Animal welfare concerns: {animal_welfare_concerns}\n\n"
            f"6. The Petitioner has no personal interest in the present matter and "
            f"is filing this Petition solely in the interest of animal welfare and "
            f"environmental protection."
        )

        draft = PILDraft(
            title=f"PIL Against Industrial Dairy Expansion in {district}, {state}",
            court=court,
            petitioner=petitioner_name,
            respondents=respondents,
            grounds=grounds,
            prayers=prayers,
            constitutional_provisions=[
                "Article 21 — Right to Life (extended to animals, Nagaraja)",
                "Article 48 — Protection of cows and cattle",
                "Article 48A — Protection of environment",
                "Article 51A(g) — Duty of compassion for living creatures",
            ],
            statutory_provisions=[
                "Prevention of Cruelty to Animals Act, 1960 — Sections 3, 11",
                "Water (Prevention and Control of Pollution) Act, 1974",
                "Air (Prevention and Control of Pollution) Act, 1981",
                "Environment (Protection) Act, 1986",
                "PCA (Transport of Livestock) Rules, 1978",
                "PCA (Slaughter House) Rules, 2001",
            ],
            case_citations=[
                "AWBI v. A. Nagaraja, (2014) 7 SCC 547",
                "M.C. Mehta v. Union of India, (1987) 1 SCC 395",
                "N.R. Nair v. Union of India, (2001) 6 SCC 84",
            ],
            facts=facts,
        )

        draft.generated_text = self._format_pil(draft)
        return draft

    def against_unlicensed_slaughterhouses(
        self,
        petitioner_name: str,
        petitioner_description: str,
        state: str,
        district: str,
        evidence_summary: str,
        rti_data: Optional[str] = None,
        high_court: Optional[str] = None,
    ) -> PILDraft:
        """
        PIL against operation of unlicensed slaughterhouses.

        Based on Laxmi Narain Modi v. Union of India (2013) which directed
        closure of all unlicensed slaughterhouses.
        """
        court = high_court or f"High Court of {state}"

        respondents = [
            f"State of {state}, through its Chief Secretary",
            f"District Collector / District Magistrate, {district}",
            f"Commissioner, Municipal Corporation / Nagar Palika, {district}",
            f"State Food Safety Commissioner, {state}",
            f"Member Secretary, State Pollution Control Board, {state}",
            "Animal Welfare Board of India, Chennai",
        ]

        grounds = [
            (
                "That the Hon'ble Supreme Court in Laxmi Narain Modi v. Union of India, "
                "SLP (Criminal) No. 5765/2008 (2013), directed all state governments to "
                "ensure closure of unlicensed slaughterhouses and compliance with "
                "Slaughter House Rules, 2001. The Respondent State has failed to comply."
            ),
            (
                "That unlicensed slaughterhouses violate Section 31 of the Food Safety "
                "and Standards Act, 2006, which mandates licensing of all food business "
                "operators, with penalty of up to Rs. 5 lakhs under Section 63."
            ),
            (
                "That unlicensed slaughterhouses routinely violate the Prevention of "
                "Cruelty to Animals (Slaughter House) Rules, 2001, including mandatory "
                "ante-mortem inspection (Rule 4), humane stunning (Rule 6), and prohibition "
                "on slaughter in sight of other animals (Rule 6(2))."
            ),
            (
                "That the absence of proper effluent treatment at unlicensed "
                "slaughterhouses causes pollution of water bodies and groundwater "
                "in violation of the Water Act, 1974 and Environment Protection Act, 1986."
            ),
            (
                "That the right to life of animals under Article 21, as recognized in "
                "AWBI v. Nagaraja (2014) 7 SCC 547, includes the right to be free from "
                "unnecessary suffering during slaughter."
            ),
        ]

        rti_ground = ""
        if rti_data:
            rti_ground = (
                f"That RTI responses reveal: {rti_data}. This data demonstrates "
                f"systemic failure of the Respondent authorities to enforce slaughter "
                f"regulations."
            )
            grounds.append(rti_ground)

        prayers = [
            (
                f"Direct the Respondent State to conduct an immediate survey of all "
                f"slaughterhouses in {district} and identify those operating without "
                f"valid licenses under the FSS Act, 2006 and municipal laws."
            ),
            (
                "Direct closure of all unlicensed slaughterhouses in compliance with "
                "the Supreme Court's direction in Laxmi Narain Modi (2013)."
            ),
            (
                "Direct the State Food Safety Commissioner to take action under "
                "Section 63 of the FSS Act, 2006 against all unlicensed operators."
            ),
            (
                "Direct the AWBI to inspect all operational slaughterhouses for "
                "compliance with the PCA (Slaughter House) Rules, 2001."
            ),
            (
                "Direct the State Pollution Control Board to assess and address "
                "pollution from slaughterhouse operations in the district."
            ),
            (
                "Pass any other order as this Hon'ble Court deems fit."
            ),
        ]

        facts = (
            f"1. The Petitioner is {petitioner_description}.\n\n"
            f"2. This Petition concerns the operation of unlicensed slaughterhouses "
            f"in {district}, {state}, in violation of food safety, environmental, "
            f"and animal welfare laws.\n\n"
            f"3. Evidence summary: {evidence_summary}\n\n"
        )
        if rti_data:
            facts += f"4. RTI data obtained: {rti_data}\n\n"
        facts += (
            f"5. Despite the clear mandate of the Supreme Court in Laxmi Narain Modi "
            f"(2013), the Respondent authorities have failed to enforce slaughter "
            f"regulations in {district}."
        )

        draft = PILDraft(
            title=f"PIL Against Unlicensed Slaughterhouses in {district}, {state}",
            court=court,
            petitioner=petitioner_name,
            respondents=respondents,
            grounds=grounds,
            prayers=prayers,
            constitutional_provisions=[
                "Article 21 — Right to Life (animals and humans)",
                "Article 48 — Protection of cattle",
                "Article 51A(g) — Duty of compassion for living creatures",
            ],
            statutory_provisions=[
                "Prevention of Cruelty to Animals Act, 1960 — Section 11",
                "PCA (Slaughter House) Rules, 2001 — Rules 3, 4, 5, 6",
                "Food Safety and Standards Act, 2006 — Sections 31, 59, 63",
                "Water (Prevention and Control of Pollution) Act, 1974",
                "Environment (Protection) Act, 1986",
            ],
            case_citations=[
                "Laxmi Narain Modi v. Union of India, SLP (Crl) No. 5765/2008 (2013)",
                "AWBI v. A. Nagaraja, (2014) 7 SCC 547",
                "Akhil Bharat Goseva Sangh v. State of A.P., (2006) 4 SCC 162",
            ],
            facts=facts,
        )

        draft.generated_text = self._format_pil(draft)
        return draft

    def against_transport_violations(
        self,
        petitioner_name: str,
        petitioner_description: str,
        state: str,
        evidence_summary: str,
        species: str = "cattle",
        high_court: Optional[str] = None,
    ) -> PILDraft:
        """
        PIL against systematic violations of livestock transport rules.
        """
        court = high_court or f"High Court of {state}"

        respondents = [
            f"State of {state}, through its Chief Secretary",
            f"Director General of Police, {state}",
            f"Transport Commissioner, {state}",
            "Union of India, through Secretary, DAHD",
            "Animal Welfare Board of India, Chennai",
        ]

        grounds = [
            (
                f"That the transport of {species} in {state} routinely violates the "
                f"Prevention of Cruelty to Animals (Transport of Livestock) Rules, 1978 "
                f"including Rule 4 (fitness certificate), Rule 6 (prohibition on "
                f"transporting unfit animals), Rule 7 (vehicle standards), Rule 8 "
                f"(maximum numbers), and Rule 9 (36-hour rest requirement)."
            ),
            (
                "That the Hon'ble Supreme Court in Gauri Maulekhi v. Union of India, "
                "W.P.(C) No. 881/2014, directed strict enforcement of transport rules. "
                "The Respondent State has failed to implement these directions."
            ),
            (
                f"That transport violations cause immense suffering to {species}, "
                f"violating their right to live with dignity as recognized in "
                f"AWBI v. Nagaraja, (2014) 7 SCC 547."
            ),
            (
                "That the failure to enforce transport rules constitutes a violation "
                "of Section 11(1)(d) of the PCA Act, 1960 (conveying or carrying an "
                "animal in a manner that subjects it to unnecessary suffering)."
            ),
        ]

        prayers = [
            (
                f"Direct the Respondent State to establish checkpoints at major "
                f"livestock transport routes to ensure compliance with Transport Rules."
            ),
            (
                "Direct the DGP to issue standing orders to all police stations "
                "for enforcement of livestock transport rules."
            ),
            (
                "Direct the Transport Commissioner to cancel registrations of "
                "vehicles found repeatedly violating transport rules."
            ),
            (
                "Direct installation of CCTV cameras at major livestock markets "
                f"(mandis) in {state} to monitor loading and transport practices."
            ),
            "Pass any other order as this Hon'ble Court deems fit.",
        ]

        draft = PILDraft(
            title=f"PIL Against Livestock Transport Violations in {state}",
            court=court,
            petitioner=petitioner_name,
            respondents=respondents,
            grounds=grounds,
            prayers=prayers,
            constitutional_provisions=[
                "Article 21 — Right to Life (animals)",
                "Article 51A(g) — Duty of compassion for living creatures",
            ],
            statutory_provisions=[
                "PCA Act, 1960 — Section 11(1)(d)",
                "PCA (Transport of Livestock) Rules, 1978 — Rules 4-9, 47",
                "PCA (Transport of Animals on Foot) Rules, 2001",
                "Motor Vehicles Act, 1988 — Section 177 (general violations)",
            ],
            case_citations=[
                "Gauri Maulekhi v. Union of India, W.P.(C) No. 881/2014",
                "AWBI v. A. Nagaraja, (2014) 7 SCC 547",
            ],
            facts=(
                f"1. The Petitioner is {petitioner_description}.\n\n"
                f"2. Evidence of transport violations: {evidence_summary}\n\n"
                f"3. The Petitioner has documented systematic violations affecting "
                f"{species} across {state}."
            ),
        )

        draft.generated_text = self._format_pil(draft)
        return draft

    def against_cafo_pollution(
        self,
        petitioner_name: str,
        petitioner_description: str,
        state: str,
        district: str,
        facility_name: str,
        facility_type: str,  # "poultry", "dairy", "piggery"
        pollution_data: str,
        affected_communities: str,
        high_court: Optional[str] = None,
    ) -> PILDraft:
        """
        PIL against pollution from Concentrated Animal Feeding Operations (CAFOs).
        """
        court = high_court or f"High Court of {state}"

        respondents = [
            f"State of {state}, through its Chief Secretary",
            f"Member Secretary, State Pollution Control Board, {state}",
            f"District Collector, {district}",
            f"{facility_name}, through its Managing Director/Proprietor",
            "Central Pollution Control Board, Delhi",
            "Union of India, through Secretary, MoEFCC",
        ]

        grounds = [
            (
                f"That the {facility_type} operation at {facility_name} in {district} "
                f"is causing severe environmental pollution affecting air, water, and "
                f"soil quality in the surrounding area, violating the fundamental right "
                f"to clean environment under Article 21 of the Constitution."
            ),
            (
                f"That the facility is operating in violation of the Water (Prevention "
                f"and Control of Pollution) Act, 1974 and the Air (Prevention and "
                f"Control of Pollution) Act, 1981, specifically: {pollution_data}"
            ),
            (
                f"That {affected_communities} are directly impacted by the pollution, "
                f"suffering from contaminated water, respiratory issues from ammonia "
                f"and particulate matter, and unbearable odour."
            ),
            (
                f"That the CPCB classifies slaughterhouses as 'Red' category and "
                f"large poultry operations (>5000 birds) as 'Orange' category "
                f"industries, requiring strict pollution control measures."
            ),
            (
                "That the Respondent Pollution Control Board has failed in its "
                "statutory duty to enforce environmental standards and protect "
                "the health of communities near the facility."
            ),
            (
                "That the Precautionary Principle and Polluter Pays Principle, "
                "recognized by the Supreme Court as part of Indian environmental "
                "law (Vellore Citizens Welfare Forum v. UoI, AIR 1996 SC 2715), "
                "require immediate action."
            ),
        ]

        prayers = [
            (
                f"Direct the State Pollution Control Board to conduct a comprehensive "
                f"environmental assessment of {facility_name} and all similar operations "
                f"within {district}."
            ),
            (
                f"Direct immediate remedial measures to prevent further pollution "
                f"of water bodies and groundwater from {facility_name}."
            ),
            (
                "Direct the Respondent facility to install and operate adequate "
                "effluent treatment, solid waste management, and air pollution "
                "control systems within a specified timeframe, failing which "
                "operations should be suspended."
            ),
            (
                f"Direct compensation to affected communities under the Polluter "
                f"Pays Principle."
            ),
            (
                f"Direct the State to formulate setback/buffer zone regulations "
                f"for {facility_type} operations near residential areas and water bodies."
            ),
            "Pass any other order as this Hon'ble Court deems fit.",
        ]

        draft = PILDraft(
            title=f"PIL Against Pollution from {facility_type.title()} CAFO in {district}, {state}",
            court=court,
            petitioner=petitioner_name,
            respondents=respondents,
            grounds=grounds,
            prayers=prayers,
            constitutional_provisions=[
                "Article 21 — Right to Life (clean environment)",
                "Article 48A — Protection of environment",
                "Article 51A(g) — Compassion for living creatures",
            ],
            statutory_provisions=[
                "Water (Prevention and Control of Pollution) Act, 1974",
                "Air (Prevention and Control of Pollution) Act, 1981",
                "Environment (Protection) Act, 1986",
                "PCA Act, 1960 — Sections 3, 11",
                "EIA Notification, 2006",
            ],
            case_citations=[
                "Vellore Citizens Welfare Forum v. Union of India, AIR 1996 SC 2715",
                "M.C. Mehta v. Union of India, (1987) 1 SCC 395",
                "AWBI v. A. Nagaraja, (2014) 7 SCC 547",
                "Indian Council for Enviro-Legal Action v. UoI, (1996) 3 SCC 212",
            ],
            facts=(
                f"1. The Petitioner is {petitioner_description}.\n\n"
                f"2. {facility_name} operates a {facility_type} facility in "
                f"{district}, {state}.\n\n"
                f"3. Pollution data: {pollution_data}\n\n"
                f"4. Affected communities: {affected_communities}\n\n"
                f"5. The Petitioner seeks intervention of this Hon'ble Court to "
                f"protect both the environment and the welfare of animals confined "
                f"in the facility."
            ),
        )

        draft.generated_text = self._format_pil(draft)
        return draft

    def _format_pil(self, draft: PILDraft) -> str:
        """Format a PIL draft as text."""
        lines = [
            f"IN THE {draft.court.upper()}",
            "",
            "WRIT PETITION (CIVIL) NO. _____ OF ______",
            "(PUBLIC INTEREST LITIGATION)",
            "",
            "IN THE MATTER OF:",
            "",
            f"{draft.petitioner}",
            f"{'.' * 50} PETITIONER",
            "",
            "VERSUS",
            "",
        ]

        for i, resp in enumerate(draft.respondents, 1):
            lines.append(f"{i}. {resp}")
        lines.append(f"{'.' * 50} RESPONDENTS")
        lines.append("")

        lines.extend([
            "PETITION UNDER ARTICLE 226 OF THE CONSTITUTION OF INDIA",
            "",
            "TO,",
            f"THE HON'BLE CHIEF JUSTICE AND OTHER COMPANION JUDGES OF THE {draft.court.upper()}",
            "",
            "THE HUMBLE PETITION OF THE PETITIONER ABOVE-NAMED",
            "",
            "MOST RESPECTFULLY SHOWETH:",
            "",
            "=" * 70,
            "FACTS",
            "=" * 70,
            "",
            draft.facts,
            "",
            "=" * 70,
            "GROUNDS",
            "=" * 70,
            "",
        ])

        for i, ground in enumerate(draft.grounds, 1):
            lines.append(f"{i}. {ground}")
            lines.append("")

        lines.extend([
            "=" * 70,
            "LEGAL PROVISIONS RELIED UPON",
            "=" * 70,
            "",
            "Constitutional Provisions:",
        ])
        for prov in draft.constitutional_provisions:
            lines.append(f"  - {prov}")

        lines.append("")
        lines.append("Statutory Provisions:")
        for stat in draft.statutory_provisions:
            lines.append(f"  - {stat}")

        lines.append("")
        lines.append("Case Law Relied Upon:")
        for case in draft.case_citations:
            lines.append(f"  - {case}")

        lines.extend([
            "",
            "=" * 70,
            "PRAYER",
            "=" * 70,
            "",
            "In the light of the facts and circumstances set out above, it is "
            "most respectfully prayed that this Hon'ble Court may be pleased to:",
            "",
        ])

        for i, prayer in enumerate(draft.prayers, 1):
            lines.append(f"({chr(96 + i)}) {prayer}")
            lines.append("")

        lines.extend([
            "AND FOR THIS ACT OF KINDNESS, THE PETITIONER SHALL EVER PRAY.",
            "",
            f"PETITIONER: {draft.petitioner}",
            f"DATE: {datetime.now().strftime('%d/%m/%Y')}",
            f"PLACE: ________________",
            "",
            "THROUGH ADVOCATE: ________________",
            "(Name, Enrolment No.)",
            "",
            "---",
            "DISCLAIMER: This is a template for educational and advocacy purposes.",
            "It must be reviewed, customized, and signed by an Advocate-on-Record",
            "before filing. PIL procedures vary between High Courts.",
        ])

        return "\n".join(lines)
