"""
RTI Act 2005 Request Generator

Generates properly formatted RTI applications under Section 6 of the
Right to Information Act, 2005. Supports requests to:
- Animal Welfare Board of India (AWBI), Chennai
- Food Safety and Standards Authority of India (FSSAI)
- State Pollution Control Boards (SPCBs) / Central Pollution Control Board (CPCB)
- National Livestock Mission (NLM) / Department of Animal Husbandry & Dairying
- Rashtriya Gokul Mission (RGM)
- District Collectors / District Magistrates

Fee: Rs. 10 (IPO/DD/Court Fee Stamp) for Central Government
State fees vary: Rs. 10 (most states), Rs. 2 (BPL exempt)

Format: Section 6(1) application with correct salutation, subject, questions,
fee declaration, and BPL exemption handling.
"""

import json
import os
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = Path(__file__).parent / "rti_templates"

# Standard RTI fee structure
FEES = {
    "central": 10,  # Rs. 10 for central government bodies
    "andhra_pradesh": 10,
    "bihar": 10,
    "chhattisgarh": 10,
    "delhi": 10,
    "goa": 10,
    "gujarat": 20,
    "haryana": 10,
    "himachal_pradesh": 10,
    "jharkhand": 10,
    "karnataka": 10,
    "kerala": 10,
    "madhya_pradesh": 10,
    "maharashtra": 10,
    "odisha": 10,
    "punjab": 10,
    "rajasthan": 10,
    "tamil_nadu": 10,
    "telangana": 10,
    "uttar_pradesh": 10,
    "uttarakhand": 10,
    "west_bengal": 10,
}

# PIO directory for key agencies
AGENCY_DIRECTORY = {
    "awbi": {
        "name": "Animal Welfare Board of India",
        "name_hi": "भारतीय पशु कल्याण बोर्ड",
        "pio_designation": "Public Information Officer",
        "address": "13/1, Third Seaward Road, Valmiki Nagar, Thiruvanmiyur, Chennai - 600041",
        "parent_ministry": "Ministry of Fisheries, Animal Husbandry and Dairying",
        "fee_category": "central",
        "appellate_authority": "First Appellate Authority, AWBI",
        "second_appeal": "Central Information Commission, New Delhi",
    },
    "fssai": {
        "name": "Food Safety and Standards Authority of India",
        "name_hi": "भारतीय खाद्य सुरक्षा और मानक प्राधिकरण",
        "pio_designation": "Central Public Information Officer",
        "address": "FDA Bhawan, Kotla Road, New Delhi - 110002",
        "parent_ministry": "Ministry of Health and Family Welfare",
        "fee_category": "central",
        "appellate_authority": "First Appellate Authority, FSSAI",
        "second_appeal": "Central Information Commission, New Delhi",
    },
    "cpcb": {
        "name": "Central Pollution Control Board",
        "name_hi": "केंद्रीय प्रदूषण नियंत्रण बोर्ड",
        "pio_designation": "Central Public Information Officer",
        "address": "Parivesh Bhawan, East Arjun Nagar, Delhi - 110032",
        "parent_ministry": "Ministry of Environment, Forest and Climate Change",
        "fee_category": "central",
        "appellate_authority": "First Appellate Authority, CPCB",
        "second_appeal": "Central Information Commission, New Delhi",
    },
    "dahd": {
        "name": "Department of Animal Husbandry and Dairying",
        "name_hi": "पशुपालन और डेयरी विभाग",
        "pio_designation": "Central Public Information Officer",
        "address": "Krishi Bhawan, Dr. Rajendra Prasad Road, New Delhi - 110001",
        "parent_ministry": "Ministry of Fisheries, Animal Husbandry and Dairying",
        "fee_category": "central",
        "appellate_authority": "First Appellate Authority, DAHD",
        "second_appeal": "Central Information Commission, New Delhi",
    },
    "nlm": {
        "name": "National Livestock Mission",
        "name_hi": "राष्ट्रीय पशुधन मिशन",
        "pio_designation": "Central Public Information Officer",
        "address": "Department of Animal Husbandry and Dairying, Krishi Bhawan, New Delhi - 110001",
        "parent_ministry": "Ministry of Fisheries, Animal Husbandry and Dairying",
        "fee_category": "central",
        "appellate_authority": "First Appellate Authority, DAHD",
        "second_appeal": "Central Information Commission, New Delhi",
    },
    "rgm": {
        "name": "Rashtriya Gokul Mission",
        "name_hi": "राष्ट्रीय गोकुल मिशन",
        "pio_designation": "Central Public Information Officer",
        "address": "Department of Animal Husbandry and Dairying, Krishi Bhawan, New Delhi - 110001",
        "parent_ministry": "Ministry of Fisheries, Animal Husbandry and Dairying",
        "fee_category": "central",
        "appellate_authority": "First Appellate Authority, DAHD",
        "second_appeal": "Central Information Commission, New Delhi",
    },
}


@dataclass
class RTIApplication:
    """Represents a single RTI application."""

    agency_code: str
    questions: list[str]
    applicant_name: str
    applicant_address: str
    applicant_phone: Optional[str] = None
    applicant_email: Optional[str] = None
    is_bpl: bool = False
    bpl_certificate_number: Optional[str] = None
    language: str = "english"  # "english", "hindi", "bilingual"
    state: Optional[str] = None  # for state-level bodies
    district: Optional[str] = None  # for district-level bodies
    subject: str = ""
    filing_date: Optional[datetime] = None
    custom_pio_name: Optional[str] = None
    custom_pio_address: Optional[str] = None
    generated_text: str = field(default="", repr=False)

    def __post_init__(self):
        if self.filing_date is None:
            self.filing_date = datetime.now()

    @property
    def fee_amount(self) -> int:
        if self.is_bpl:
            return 0
        if self.state and self.state.lower().replace(" ", "_") in FEES:
            return FEES[self.state.lower().replace(" ", "_")]
        agency = AGENCY_DIRECTORY.get(self.agency_code, {})
        return FEES.get(agency.get("fee_category", "central"), 10)

    @property
    def response_deadline(self) -> datetime:
        """30 days from filing under Section 7(1)."""
        return self.filing_date + timedelta(days=30)

    @property
    def first_appeal_deadline(self) -> datetime:
        """30 days after response deadline under Section 19(1)."""
        return self.response_deadline + timedelta(days=30)

    @property
    def second_appeal_deadline(self) -> datetime:
        """90 days after first appeal decision under Section 19(3)."""
        return self.first_appeal_deadline + timedelta(days=90)


class RTIGenerator:
    """
    Generate RTI applications under the Right to Information Act, 2005.

    Produces properly formatted Section 6(1) applications in English,
    Hindi, or bilingual format targeting animal agriculture oversight bodies.
    """

    def __init__(self, template_dir: Optional[Path] = None):
        self.template_dir = template_dir or TEMPLATE_DIR
        self.env = Environment(
            loader=FileSystemLoader(str(self.template_dir)),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def generate(self, application: RTIApplication) -> str:
        """Generate complete RTI application text."""
        agency = AGENCY_DIRECTORY.get(application.agency_code, {})

        context = {
            "app": application,
            "agency": agency,
            "fee": application.fee_amount,
            "date": application.filing_date.strftime("%d/%m/%Y"),
            "date_hi": self._format_date_hindi(application.filing_date),
            "response_deadline": application.response_deadline.strftime("%d/%m/%Y"),
            "first_appeal_deadline": application.first_appeal_deadline.strftime("%d/%m/%Y"),
        }

        if application.language == "hindi":
            text = self._generate_hindi(context)
        elif application.language == "bilingual":
            text = self._generate_bilingual(context)
        else:
            text = self._generate_english(context)

        application.generated_text = text
        return text

    def generate_from_template(
        self, template_name: str, application: RTIApplication
    ) -> str:
        """Generate RTI using a pre-built template file."""
        template_path = self.template_dir / template_name
        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_name}")

        template_text = template_path.read_text(encoding="utf-8")
        agency = AGENCY_DIRECTORY.get(application.agency_code, {})

        # Parse template for questions
        questions = self._extract_template_questions(template_text)
        if questions:
            application.questions = questions

        return self.generate(application)

    def _generate_english(self, context: dict) -> str:
        """Generate English-language RTI application."""
        app = context["app"]
        agency = context["agency"]

        pio_address = app.custom_pio_address or agency.get("address", "[ADDRESS]")
        pio_designation = agency.get("pio_designation", "Public Information Officer")

        lines = [
            "APPLICATION UNDER SECTION 6(1) OF THE RIGHT TO INFORMATION ACT, 2005",
            "",
            f"Date: {context['date']}",
            "",
            "To,",
            f"The {pio_designation},",
            agency.get("name", "[AGENCY NAME]") + ",",
            pio_address,
            "",
            f"Subject: {app.subject or 'Request for Information under RTI Act, 2005'}",
            "",
            "Respected Sir/Madam,",
            "",
            "I, the undersigned, am a citizen of India and wish to seek information",
            "under Section 6(1) of the Right to Information Act, 2005. The details",
            "of the information sought are as follows:",
            "",
        ]

        for i, question in enumerate(app.questions, 1):
            lines.append(f"{i}. {question}")
            lines.append("")

        fee_text = (
            f"I am enclosing an Indian Postal Order / Demand Draft / Court Fee Stamp "
            f"of Rs. {context['fee']}/- (Rupees {self._number_to_words(context['fee'])} only) "
            f"as the prescribed fee under the RTI Act, 2005."
        )
        if app.is_bpl:
            fee_text = (
                f"I belong to Below Poverty Line (BPL) category and am exempt from "
                f"payment of fee under Section 7(5) of the RTI Act, 2005. "
                f"My BPL Certificate Number is: {app.bpl_certificate_number or '[BPL NUMBER]'}."
            )

        lines.extend([
            fee_text,
            "",
            "I request that the above information be provided within 30 days as",
            "stipulated under Section 7(1) of the RTI Act, 2005.",
            "",
            "If the information sought or any part thereof concerns the life or",
            "liberty of a person, it shall be provided within 48 hours of receipt",
            "of this request as per Section 7(1) of the Act.",
            "",
            "If this application is transferred to another public authority under",
            "Section 6(3), I request to be informed of the same.",
            "",
            "Yours faithfully,",
            "",
            f"Name: {app.applicant_name}",
            f"Address: {app.applicant_address}",
        ])

        if app.applicant_phone:
            lines.append(f"Phone: {app.applicant_phone}")
        if app.applicant_email:
            lines.append(f"Email: {app.applicant_email}")

        lines.extend([
            "",
            "---",
            f"NOTE: Response deadline under Section 7(1): {context['response_deadline']}",
            f"First Appeal deadline under Section 19(1): {context['first_appeal_deadline']}",
            f"Appellate Authority: {agency.get('appellate_authority', 'First Appellate Authority')}",
            f"Second Appeal: {agency.get('second_appeal', 'Central/State Information Commission')}",
        ])

        return "\n".join(lines)

    def _generate_hindi(self, context: dict) -> str:
        """Generate Hindi-language RTI application (accessible Hindustani)."""
        app = context["app"]
        agency = context["agency"]

        pio_address = app.custom_pio_address or agency.get("address", "[पता]")
        agency_name_hi = agency.get("name_hi", agency.get("name", "[विभाग का नाम]"))

        lines = [
            "सूचना का अधिकार अधिनियम, 2005 की धारा 6(1) के तहत आवेदन",
            "",
            f"दिनांक: {context['date_hi']}",
            "",
            "सेवा में,",
            "जन सूचना अधिकारी,",
            f"{agency_name_hi},",
            pio_address,
            "",
            f"विषय: {app.subject or 'सूचना का अधिकार अधिनियम, 2005 के तहत सूचना प्राप्त करने का आवेदन'}",
            "",
            "महोदय/महोदया,",
            "",
            "मैं, नीचे हस्ताक्षरकर्ता, भारत का नागरिक हूं और सूचना का अधिकार",
            "अधिनियम, 2005 की धारा 6(1) के तहत निम्नलिखित सूचना प्राप्त करना चाहता/चाहती हूं:",
            "",
        ]

        for i, question in enumerate(app.questions, 1):
            lines.append(f"{i}. {question}")
            lines.append("")

        if app.is_bpl:
            lines.extend([
                f"मैं गरीबी रेखा से नीचे (BPL) की श्रेणी में आता/आती हूं और RTI अधिनियम, 2005",
                f"की धारा 7(5) के तहत शुल्क से मुक्त हूं।",
                f"BPL प्रमाणपत्र संख्या: {app.bpl_certificate_number or '[BPL संख्या]'}",
            ])
        else:
            lines.extend([
                f"मैं RTI अधिनियम, 2005 के तहत निर्धारित शुल्क के रूप में",
                f"₹{context['fee']}/- का भारतीय पोस्टल ऑर्डर / डिमांड ड्राफ्ट संलग्न कर रहा/रही हूं।",
            ])

        lines.extend([
            "",
            "कृपया उपरोक्त सूचना RTI अधिनियम, 2005 की धारा 7(1) के तहत",
            "निर्धारित 30 दिनों के भीतर उपलब्ध कराएं।",
            "",
            "भवदीय/भवदीया,",
            "",
            f"नाम: {app.applicant_name}",
            f"पता: {app.applicant_address}",
        ])

        if app.applicant_phone:
            lines.append(f"फोन: {app.applicant_phone}")
        if app.applicant_email:
            lines.append(f"ईमेल: {app.applicant_email}")

        return "\n".join(lines)

    def _generate_bilingual(self, context: dict) -> str:
        """Generate bilingual (English + Hindi) RTI application."""
        english = self._generate_english(context)
        hindi = self._generate_hindi(context)
        return (
            "=" * 70 + "\n"
            "ENGLISH VERSION / अंग्रेज़ी संस्करण\n"
            + "=" * 70 + "\n\n"
            + english + "\n\n"
            + "=" * 70 + "\n"
            "हिंदी संस्करण / HINDI VERSION\n"
            + "=" * 70 + "\n\n"
            + hindi
        )

    def _extract_template_questions(self, template_text: str) -> list[str]:
        """Extract numbered questions from template text."""
        questions = []
        for line in template_text.strip().split("\n"):
            line = line.strip()
            if line and line[0].isdigit() and "." in line[:4]:
                question = line.split(".", 1)[1].strip()
                if question:
                    questions.append(question)
        return questions

    def _format_date_hindi(self, dt: datetime) -> str:
        """Format date in Hindi."""
        months_hi = {
            1: "जनवरी", 2: "फरवरी", 3: "मार्च", 4: "अप्रैल",
            5: "मई", 6: "जून", 7: "जुलाई", 8: "अगस्त",
            9: "सितंबर", 10: "अक्टूबर", 11: "नवंबर", 12: "दिसंबर",
        }
        return f"{dt.day} {months_hi[dt.month]} {dt.year}"

    def _number_to_words(self, n: int) -> str:
        """Convert number to English words (for fee amounts)."""
        words = {
            0: "Zero", 2: "Two", 5: "Five", 10: "Ten",
            20: "Twenty", 50: "Fifty", 100: "One Hundred",
        }
        return words.get(n, str(n))

    def get_agency_info(self, agency_code: str) -> dict:
        """Get agency details."""
        return AGENCY_DIRECTORY.get(agency_code, {})

    def list_agencies(self) -> list[str]:
        """List all supported agency codes."""
        return list(AGENCY_DIRECTORY.keys())

    def list_templates(self) -> list[str]:
        """List available RTI templates."""
        if self.template_dir.exists():
            return [f.name for f in self.template_dir.glob("*.txt")]
        return []

    # ----- Convenience factory methods for common RTI types -----

    def awbi_inspection_request(
        self,
        facility_name: str,
        facility_location: str,
        applicant_name: str,
        applicant_address: str,
        **kwargs,
    ) -> RTIApplication:
        """Generate RTI for AWBI inspection reports on a specific facility."""
        questions = [
            f"Please provide copies of all inspection reports for {facility_name} "
            f"located at {facility_location} conducted by AWBI or its representatives "
            f"in the last 3 years.",
            f"What is the current registration/recognition status of {facility_name} "
            f"under the Prevention of Cruelty to Animals Act, 1960?",
            "How many complaints have been received against the said facility in the "
            "last 3 years, and what action was taken on each complaint?",
            "Please provide the latest compliance report for the facility with respect "
            "to the Animal Welfare Board of India guidelines.",
            "What is the animal capacity approved for this facility, and what is the "
            "current animal population as per the last inspection?",
        ]
        return RTIApplication(
            agency_code="awbi",
            questions=questions,
            applicant_name=applicant_name,
            applicant_address=applicant_address,
            subject=f"Inspection reports and compliance status of {facility_name}",
            **kwargs,
        )

    def fssai_violations_request(
        self,
        state: str,
        district: str,
        applicant_name: str,
        applicant_address: str,
        year: int = 2025,
        **kwargs,
    ) -> RTIApplication:
        """Generate RTI for FSSAI food safety violations in meat/dairy."""
        questions = [
            f"How many food safety inspections were conducted at slaughterhouses, "
            f"meat processing plants, and dairy processing units in {district} district, "
            f"{state} during the year {year}?",
            f"How many violations of the Food Safety and Standards (Licensing and "
            f"Registration of Food Businesses) Regulations, 2011 were detected at "
            f"meat and dairy establishments in {district}, {state} during {year}?",
            "Please provide details of all penalties, fines, and license suspensions "
            f"imposed on meat and dairy establishments in {district} during {year}.",
            "How many meat and dairy establishments in the district currently hold "
            "valid FSSAI licenses, and how many are operating without licenses?",
            "What testing has been done for antibiotic residues, aflatoxin M1, "
            "adulterants (urea, detergent, starch), and pesticide residues in "
            f"milk and dairy products in {district} during {year}?",
        ]
        return RTIApplication(
            agency_code="fssai",
            questions=questions,
            applicant_name=applicant_name,
            applicant_address=applicant_address,
            subject=f"Food safety violations at meat/dairy units in {district}, {state}",
            state=state,
            district=district,
            **kwargs,
        )

    def pollution_board_request(
        self,
        state: str,
        district: str,
        applicant_name: str,
        applicant_address: str,
        **kwargs,
    ) -> RTIApplication:
        """Generate RTI for state PCB pollution data from animal agriculture."""
        questions = [
            f"How many poultry farms, dairy farms, piggeries, and slaughterhouses "
            f"in {district} district, {state} hold valid Consent to Operate (CTO) "
            f"from the State Pollution Control Board?",
            "Please provide data on effluent discharge, BOD levels, COD levels, "
            f"and solid waste generation from all animal agriculture operations in "
            f"{district} for the last 2 years.",
            "How many complaints regarding pollution from poultry farms, dairy farms, "
            f"piggeries, and slaughterhouses have been received in {district} in the "
            f"last 3 years? What action was taken?",
            "Please provide details of all Consent to Operate applications received "
            f"from animal agriculture operations in {district}, and how many were "
            f"approved, rejected, or are pending.",
            "What is the groundwater quality data for areas within 1 km of large "
            f"poultry and dairy operations in {district}? Please provide nitrate, "
            "ammonia, and coliform levels.",
        ]
        return RTIApplication(
            agency_code="cpcb",
            questions=questions,
            applicant_name=applicant_name,
            applicant_address=applicant_address,
            subject=f"Pollution data from animal agriculture in {district}, {state}",
            state=state,
            district=district,
            **kwargs,
        )

    def subsidy_data_request(
        self,
        state: str,
        applicant_name: str,
        applicant_address: str,
        scheme: str = "both",  # "nlm", "rgm", or "both"
        **kwargs,
    ) -> RTIApplication:
        """Generate RTI for NLM/Rashtriya Gokul Mission spending data."""
        agency = "nlm" if scheme == "nlm" else "rgm" if scheme == "rgm" else "dahd"

        questions = []
        if scheme in ("nlm", "both"):
            questions.extend([
                f"What is the total funds allocated and disbursed under the National "
                f"Livestock Mission (NLM) to {state} for each year from 2019-20 to "
                f"2024-25? Please provide scheme-wise and component-wise breakup.",
                f"How many beneficiaries have received subsidies under NLM in {state} "
                f"for poultry, dairy, piggery, and goat rearing? Provide year-wise data.",
                f"What is the total subsidy amount disbursed for establishment of new "
                f"commercial poultry farms and dairy units in {state} under NLM?",
            ])
        if scheme in ("rgm", "both"):
            questions.extend([
                f"What is the total expenditure under the Rashtriya Gokul Mission (RGM) "
                f"in {state} from 2019-20 to 2024-25? Provide component-wise breakup "
                f"including Gokul Grams, IVF centres, and AI coverage.",
                f"How many Gokul Grams have been established in {state} and what is "
                f"the animal housing capacity and current occupancy of each?",
                f"What is the total expenditure on artificial insemination under RGM "
                f"in {state}, and what are the conception success rates reported?",
            ])

        questions.append(
            "Please provide copies of any audit reports, utilization certificates, "
            f"or evaluation studies for the above schemes in {state}."
        )

        return RTIApplication(
            agency_code=agency,
            questions=questions,
            applicant_name=applicant_name,
            applicant_address=applicant_address,
            subject=f"Expenditure and outcomes under NLM/RGM in {state}",
            state=state,
            **kwargs,
        )

    def slaughterhouse_license_request(
        self,
        district: str,
        state: str,
        applicant_name: str,
        applicant_address: str,
        **kwargs,
    ) -> RTIApplication:
        """Generate RTI for district slaughterhouse licensing data."""
        questions = [
            f"How many slaughterhouses are licensed/registered in {district} district, "
            f"{state} as of date? Provide name, location, and license validity.",
            f"How many slaughterhouses in {district} comply with the Slaughter House "
            f"and Meat Inspection Rules (Food Safety and Standards Authority of India), "
            f"and the Slaughtering Rules, 2001?",
            f"How many unlicensed/unregistered slaughterhouses have been identified "
            f"in {district} in the last 3 years, and what action was taken?",
            f"What is the approved daily slaughter capacity of each licensed "
            f"slaughterhouse in {district}, and what are the actual daily slaughter numbers?",
            f"Please provide inspection reports for all slaughterhouses in {district} "
            f"for the last 2 years, including veterinary inspection records.",
            f"Do the slaughterhouses in {district} have operational effluent treatment "
            f"plants as required under environmental regulations? Provide status.",
        ]
        return RTIApplication(
            agency_code="fssai",
            questions=questions,
            applicant_name=applicant_name,
            applicant_address=applicant_address,
            subject=f"Slaughterhouse licensing and compliance in {district}, {state}",
            state=state,
            district=district,
            **kwargs,
        )
