"""
Amul Counter-Narrative Generator

Generate counter-narratives that frame Amul/GCMMF as betraying the cooperative
values it claims to represent. Target the gap between Amul's marketing image
(small farmer, white revolution, Taste of India) and the industrial reality.

Strategy: Do NOT attack the cooperative model itself (it's better than purely
corporate dairy). Instead, show how Amul has industrialized beyond what the
cooperative model was supposed to do, and how the animals and environment
pay the price.
"""

from dataclasses import dataclass
from typing import Optional

from india.amul.amul_research import AmulResearchDB


@dataclass
class Narrative:
    """A generated counter-narrative piece."""
    title: str
    angle: str
    target_audience: str
    platform: str
    content_hindi: str
    content_english: str
    sources: list[str]
    caste_check_notes: str = ""


class NarrativeGenerator:
    """
    Generate counter-narratives about Amul/GCMMF.

    Approach: Amul betrayed its own cooperative values by industrializing.
    The original promise (farmer empowerment) has been subordinated to
    production volume and revenue targets.
    """

    def __init__(self):
        self.research = AmulResearchDB()

    def cooperative_betrayal(self, platform: str = "whatsapp") -> Narrative:
        """
        Narrative: Amul betrayed cooperative values.

        Frame: Amul started as a movement for farmer dignity. It has become
        a Rs. 72,000 crore industrial machine where the animals and
        environment are sacrificed for production targets.
        """
        hindi = (
            "*Amul: सहकारिता या industry?* 🐄\n"
            "\n"
            "Amul की शुरुआत 1946 में हुई — Kaira के किसानों ने बिचौलियों से "
            "आज़ादी के लिए। Dr. Kurien ने इसे White Revolution बनाया।\n"
            "\n"
            "आज Amul:\n"
            "💰 Revenue: Rs 72,000 करोड़\n"
            "🏭 90+ processing plants\n"
            "📊 2.6 करोड़ लीटर दूध/दिन\n"
            "\n"
            "ये cooperative है या MNC?\n"
            "\n"
            "किसान को दूध का Rs 30-40/लीटर मिलता है।\n"
            "Amul उसे Rs 60-80 में बेचता है।\n"
            "Processing, packaging, marketing — सब में cooperative का margin।\n"
            "\n"
            "और जानवर? वो तो बस production unit हैं।\n"
            "बार-बार गर्भवती। AI से cross-breeding। नर बछड़े ग़ायब।\n"
            "दूध कम हुआ तो बाहर। कुदरती उम्र 20 साल — use 5-6 साल।\n"
            "\n"
            "*Amul की Taste of India एक illusion है।*\n"
            "*असली taste — exploitation का है।*\n"
        )

        english = (
            "Amul: Cooperative or Corporation?\n\n"
            "Amul began in 1946 as a farmers' revolt against middlemen in Kaira, "
            "Gujarat. Dr. Verghese Kurien turned it into the White Revolution.\n\n"
            "Today's Amul:\n"
            "- Revenue: Rs 72,000 crore (~$8.6 billion)\n"
            "- 90+ processing plants\n"
            "- 26 million litres/day collection\n"
            "- 3.6 million farmer members\n\n"
            "Is this a cooperative or a multinational?\n\n"
            "The farmer receives Rs 30-40/litre. Amul sells at Rs 60-80/litre. "
            "The gap funds an industrial machine.\n\n"
            "And the animals? They're production units.\n"
            "Repeatedly impregnated. Crossbred for yield. Male calves disappeared. "
            "Discarded when production drops. Natural lifespan 20 years; used for 5-6.\n\n"
            "Amul's 'Taste of India' is branding.\n"
            "The real taste is exploitation."
        )

        return Narrative(
            title="Amul: Cooperative Betrayed",
            angle="cooperative_vs_industrial",
            target_audience="Urban consumers, students, socially conscious",
            platform=platform,
            content_hindi=hindi,
            content_english=english,
            sources=[
                "GCMMF Annual Report FY2023-24",
                "20th Livestock Census, 2019",
                "FSSAI milk procurement pricing data",
            ],
        )

    def missing_calves(self, platform: str = "whatsapp") -> Narrative:
        """
        Narrative: Where are the male calves?

        Frame: The math doesn't work. Millions of calves born, half male,
        no economic value in dairy. Where do they go? Amul never answers.
        """
        hindi = (
            "*ग़ायब बछड़े: Amul का अनकहा सच* 🐄\n"
            "\n"
            "Amul system में 36 लाख किसान हैं।\n"
            "हर गाय/भैंस को हर साल गर्भवती किया जाता है।\n"
            "50% बछड़े नर होते हैं।\n"
            "\n"
            "तो हर साल लाखों नर बछड़े कहाँ जाते हैं?\n"
            "\n"
            "📊 20th Livestock Census (2019): Gujarat में cattle का male:female ratio "
            "बहुत skewed है — females ज़्यादा, males ग़ायब।\n"
            "\n"
            "नर बछड़ों का कोई economic value नहीं dairy system में:\n"
            "❌ दूध नहीं देते\n"
            "❌ Cross-breed हैं तो draught work नहीं कर सकते\n"
            "❌ Feed cost Rs 50-80/दिन — किसान afford नहीं कर सकता\n"
            "\n"
            "तो?\n"
            "\n"
            "→ छोड़ दिए जाते हैं सड़कों पर (stray cattle crisis)\n"
            "→ बेच दिए जाते हैं कसाई को\n"
            "→ भूख से मर जाते हैं\n"
            "\n"
            "Amul इस बारे में कभी बात नहीं करता।\n"
            "Amul Girl की तस्वीर में बछड़ा कभी नहीं दिखता।\n"
            "\n"
            "*RTI file करें: Rashtriya Gokul Mission से पूछें — "
            "Gujarat में नर बछड़ों का क्या होता है?*\n"
        )

        english = (
            "The Missing Calves: Amul's Untold Truth\n\n"
            "The Amul system has 3.6 million farmer members.\n"
            "Every cow/buffalo is impregnated annually.\n"
            "50% of calves are male.\n\n"
            "Where do millions of male calves go every year?\n\n"
            "The 20th Livestock Census (2019) shows Gujarat's cattle sex ratio "
            "is heavily skewed — far more females than males. The males vanish.\n\n"
            "Male calves have zero economic value in dairy:\n"
            "- Can't produce milk\n"
            "- Crossbreeds can't do draught work\n"
            "- Feed costs Rs 50-80/day — farmers can't afford it\n\n"
            "So they are:\n"
            "- Abandoned on roads (Gujarat's stray cattle crisis)\n"
            "- Sold to informal slaughter\n"
            "- Left to starve\n\n"
            "Amul never talks about this.\n"
            "The Amul Girl never appears next to a calf.\n\n"
            "File RTI: Ask Rashtriya Gokul Mission what happens to "
            "male calves in Gujarat."
        )

        return Narrative(
            title="The Missing Calves",
            angle="male_calf_crisis",
            target_audience="General public, cow protection advocates (challenge their assumptions)",
            platform=platform,
            content_hindi=hindi,
            content_english=english,
            sources=[
                "20th Livestock Census, 2019 (DAHD)",
                "AWBI reports on calf abandonment",
                "Field investigations by HSI/India, FIAPO",
            ],
            caste_check_notes=(
                "This narrative avoids cow slaughter framing. It focuses on "
                "abandonment and starvation, not slaughter. This is deliberate — "
                "slaughter framing risks being co-opted by cow vigilantes."
            ),
        )

    def water_footprint(self, platform: str = "whatsapp") -> Narrative:
        """
        Narrative: Amul's water footprint in water-scarce Gujarat.
        """
        hindi = (
            "*Amul और पानी: Gujarat का छुपा संकट* 💧\n"
            "\n"
            "Gujarat भारत के सबसे water-stressed राज्यों में से एक है।\n"
            "और Gujarat India का सबसे बड़ा दूध उत्पादक है।\n"
            "\n"
            "Connection? बिल्कुल।\n"
            "\n"
            "Amul 2.6 करोड़ लीटर दूध/दिन collect करता है।\n"
            "1 लीटर दूध = 1000+ लीटर पानी।\n"
            "मतलब Amul system रोज़ 2600 करोड़ लीटर पानी consume करता है।\n"
            "\n"
            "📍 बनासकांठा — Amul का सबसे बड़ा union (Banas Dairy):\n"
            "→ Groundwater table हर साल गिर रहा है\n"
            "→ Bore wells 300+ feet गहरे\n"
            "→ किसानों को fodder के लिए पानी चाहिए\n"
            "→ लोगों को पीने के लिए पानी नहीं\n"
            "\n"
            "Amul कहता है: 'दूध भारत की ताक़त है।'\n"
            "लेकिन ये ताक़त पानी की बर्बादी पर टिकी है।\n"
            "\n"
            "🌱 Plant-based दूध: 300 लीटर पानी/लीटर\n"
            "🐄 गाय का दूध: 1000+ लीटर पानी/लीटर\n"
            "\n"
            "*पानी ख़त्म हो रहा है। विकल्प हैं।*\n"
        )

        english = (
            "Amul and Water: Gujarat's Hidden Crisis\n\n"
            "Gujarat is one of India's most water-stressed states.\n"
            "Gujarat is also India's largest milk producer.\n\n"
            "Amul collects 26 million litres/day.\n"
            "1 litre of milk = 1000+ litres of water.\n"
            "That's 26 billion litres of water consumed daily by the Amul system.\n\n"
            "Banaskantha — Amul's largest union (Banas Dairy):\n"
            "- Groundwater table dropping every year\n"
            "- Bore wells at 300+ feet\n"
            "- Farmers need water for fodder crops\n"
            "- Communities lack drinking water\n\n"
            "Amul says: 'Milk is India's strength.'\n"
            "That strength is built on water depletion.\n\n"
            "Plant-based milk: ~300 litres water/litre\n"
            "Cow milk: 1000+ litres water/litre\n\n"
            "Water is running out. Alternatives exist."
        )

        return Narrative(
            title="Amul's Water Footprint",
            angle="water_footprint",
            target_audience="Environmentally conscious, Gujarat residents, water activists",
            platform=platform,
            content_hindi=hindi,
            content_english=english,
            sources=[
                "CGWB Gujarat monitoring data",
                "NITI Aayog Composite Water Management Index",
                "Water Footprint Network data",
                "GCMMF collection data",
            ],
        )

    def operation_flood_critique(self, platform: str = "article") -> Narrative:
        """
        Narrative: Operation Flood created India's dairy dependency.

        Frame: India's dairy revolution was engineered, not organic.
        Funded by European dairy surplus and World Bank loans.
        """
        english = (
            "Operation Flood: How Europe's Dairy Surplus Created India's Dairy Dependency\n\n"
            "The standard narrative: Dr. Verghese Kurien and Operation Flood (1970-1996) "
            "liberated Indian farmers through dairy cooperatives. India became the world's "
            "largest milk producer.\n\n"
            "The overlooked facts:\n\n"
            "1. FUNDING SOURCE: Operation Flood was primarily funded by the European "
            "Economic Community (EEC) donating its dairy surplus — butter oil and milk "
            "powder that Europe couldn't sell. This surplus was monetized in India "
            "to fund cooperative infrastructure.\n\n"
            "2. WORLD BANK LOANS: Three phases of World Bank financing totaling over "
            "$150 million. India took loans to import a dairy production model.\n\n"
            "3. DEPENDENCY CREATION: Before Operation Flood, India had diverse traditional "
            "food systems with lower dairy dependency. Operation Flood specifically "
            "aimed to increase per-capita milk consumption — creating demand that "
            "didn't previously exist at that scale.\n\n"
            "4. WHO BENEFITED: Researchers like Shanti George documented that Operation "
            "Flood primarily benefited middle-to-large farmers, not the landless poor. "
            "The cooperative model required land (for animals and fodder) that the "
            "poorest didn't have.\n\n"
            "5. THE CROSSBREEDING PUSH: Operation Flood promoted crossbreeding Indian "
            "cattle with Holstein-Friesian and Jersey — creating high-yield animals "
            "unsuited to Indian conditions, dependent on purchased feed, and prone "
            "to health issues. This is the foundation of today's male calf crisis.\n\n"
            "Operation Flood was a development success story by one metric: milk production. "
            "By every other metric — animal welfare, environmental sustainability, food "
            "sovereignty, equity — it created problems we are only now beginning to "
            "understand.\n\n"
            "Amul is Operation Flood's monument. The question is whether we want to "
            "keep building on that foundation."
        )

        hindi = (
            "*Operation Flood: Europe की मदद से बना भारत का dairy system* 🐄\n"
            "\n"
            "हमें बताया जाता है कि Operation Flood (1970-96) ने भारत को "
            "दूध में आत्मनिर्भर बनाया।\n"
            "\n"
            "लेकिन ये नहीं बताया जाता:\n"
            "\n"
            "1. पैसा कहाँ से आया? Europe का extra butter और milk powder — "
            "जो वो बेच नहीं पा रहे थे — भारत को 'donate' किया गया\n"
            "\n"
            "2. World Bank ने $150 million से ज़्यादा का loan दिया\n"
            "\n"
            "3. भारत में पहले दूध की इतनी माँग नहीं थी — "
            "Operation Flood ने माँग create की\n"
            "\n"
            "4. फ़ायदा किसे हुआ? बड़े किसानों को। "
            "भूमिहीन ग़रीबों को cooperative में जगह नहीं मिली\n"
            "\n"
            "5. Cross-breeding: देसी गायों को Holstein-Friesian/Jersey से "
            "cross किया — ज़्यादा दूध, लेकिन ज़्यादा बीमारियाँ, "
            "ज़्यादा feed ख़र्च, और नर बछड़ों का crisis\n"
            "\n"
            "*Operation Flood ने दूध बढ़ाया। लेकिन जानवरों, पर्यावरण, "
            "और खाद्य सुरक्षा की क़ीमत पर।*\n"
        )

        return Narrative(
            title="Operation Flood Critique",
            angle="operation_flood_legacy",
            target_audience="Intellectuals, policy community, food sovereignty advocates",
            platform=platform,
            content_hindi=hindi,
            content_english=english,
            sources=[
                "World Bank Operation Flood project documents (I, II, III)",
                "Shanti George, 'Operation Flood: An Appraisal of Current Indian Dairy Policy' (1985)",
                "Claude Alvares, various critiques of Green/White Revolution",
                "DAHD historical data",
            ],
        )

    def list_narratives(self) -> list[str]:
        """List available narrative types."""
        return [
            "cooperative_betrayal",
            "missing_calves",
            "water_footprint",
            "operation_flood_critique",
        ]

    def generate_all(self, platform: str = "whatsapp") -> list[Narrative]:
        """Generate all available narratives."""
        return [
            self.cooperative_betrayal(platform),
            self.missing_calves(platform),
            self.water_footprint(platform),
            self.operation_flood_critique(platform),
        ]
