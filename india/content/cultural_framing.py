"""
Cultural Framing for Indian Animal Advocacy

Frame animal welfare arguments through Indian cultural lenses that resonate
without reinforcing harmful narratives. Key frames:

1. AHIMSA: Non-violence as a universal Indian value (NOT limited to Hinduism)
   — Jain, Buddhist, Gandhian traditions. Emphasize ahimsa as action, not
   just abstention.

2. HEALTH & ADULTERATION: Food safety resonates universally. FSSAI data on
   milk adulteration (urea, detergent, synthetic milk), antibiotic residues,
   and hormone contamination.

3. WATER CRISIS: India's water emergency is real and visceral. Dairy and
   poultry's water footprint is a powerful lever.

4. ECONOMICS: Who profits from factory farming? Follow the money —
   corporate consolidation vs. small farmer squeeze.

5. EXPLICITLY REJECT: Casteist purity framing, communal cow politics,
   "vegetarian = upper caste = pure" narratives.

6. PARTNER WITH: Dalit-Bahujan perspectives on food sovereignty,
   Adivasi land rights, small farmer movements.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class CulturalFrame:
    """A cultural framing approach for advocacy content."""
    name: str
    description: str
    key_messages: list[str]
    target_audience: str
    do_use: list[str]
    do_not_use: list[str]
    example_content: str


FRAMES = {
    "ahimsa": CulturalFrame(
        name="Ahimsa (Non-violence)",
        description=(
            "Non-violence as a core Indian value across traditions — Jain, Buddhist, "
            "Gandhian, and broader Indian philosophy. Frame factory farming as a "
            "violation of ahimsa that all traditions agree on."
        ),
        key_messages=[
            "Factory farming is organized violence. Ahimsa demands we confront it.",
            "Gandhi said: 'The greatness of a nation can be judged by the way its animals are treated.'",
            "Ahimsa is not just not-killing. It is actively preventing suffering.",
            "Every Indian tradition values compassion for animals. Factory farms betray all of them.",
            "Jain ahimsa teaches that even indirect violence (through consumption) matters.",
        ],
        target_audience="General Indian audience, especially those who identify with ahimsa traditions",
        do_use=[
            "Gandhi quotes on animals and non-violence (well-sourced)",
            "Jain tradition of animal protection and sanctuaries (panjrapoles)",
            "Buddhist first precept (do not harm living beings)",
            "Cross-traditional consensus on compassion",
            "Modern interpretation: ahimsa as active resistance to industrial cruelty",
        ],
        do_not_use=[
            "Hindu nationalist cow rhetoric",
            "Framing vegetarianism as 'Hindu' or 'upper caste'",
            "Using ahimsa to shame meat-eaters (especially Dalit/Adivasi/Muslim communities)",
            "Implying that those who eat meat are 'less Indian'",
            "Sanskrit-heavy language that alienates non-Hindi speakers",
        ],
        example_content=(
            "Gandhi ji ne kaha tha: 'Kisi desh ki mahanata aur uski tarakki ka andaaza "
            "is baat se lagaaya ja sakta hai ki woh apne janwaron ke saath kaisa "
            "bartaav karta hai.' Aaj factory farms mein janwaron ke saath jo ho raha "
            "hai — woh ahimsa ke bilkul khilaf hai. Ye sirf Hindu ya Jain ka maamla "
            "nahi hai. Har insaan jaanta hai ki berahmi galat hai."
        ),
    ),
    "health_adulteration": CulturalFrame(
        name="Health & Food Adulteration",
        description=(
            "Food safety and adulteration concerns resonate across all communities. "
            "FSSAI data consistently shows milk adulteration (urea, detergent, "
            "synthetic milk), antibiotic residues, and aflatoxin M1 contamination. "
            "This is a health argument, not a moral one."
        ),
        key_messages=[
            "FSSAI ki jaanch mein doodh mein milaawat paai gayi — urea, detergent, starch.",
            "Dairy industry mein antibiotics ka bharee istemaal hota hai. Ye doodh ke zariye aapke sharir mein aata hai.",
            "Antibiotic resistance duniya ki sabse badi health crisis ban rahi hai. Dairy ek bada kaaran hai.",
            "India mein har saal hazaaron log milaawati doodh se beemar hote hain.",
            "Aapke bachche kya pee rahe hain? Jaaniye, phir faisla kijiye.",
        ],
        target_audience="Parents, health-conscious consumers, urban middle class",
        do_use=[
            "FSSAI survey data (National Milk Quality Survey)",
            "WHO reports on antibiotic resistance",
            "Specific adulteration incidents (named, dated)",
            "Health impact data: cancer, antibiotic resistance, hormonal disruption",
            "Economic framing: you pay for pure milk, you get chemicals",
        ],
        do_not_use=[
            "Shaming milk drinkers",
            "Claiming all milk is 'poison' (be specific and evidence-based)",
            "Targeting specific communities' food practices",
            "Unverified health claims",
        ],
        example_content=(
            "Kya aap jaante hain? FSSAI ki 2018 National Milk Quality Survey "
            "mein paaya gaya ki 41% doodh ke samples standards ke mutaabiq "
            "nahi the. Aflatoxin M1 (ek carcinogen), antibiotic residues, "
            "aur pesticides paaye gaye. Aapke ghar ka doodh kitna safe hai?"
        ),
    ),
    "water_crisis": CulturalFrame(
        name="Water Crisis",
        description=(
            "India faces a genuine water emergency. NITI Aayog reported that 21 "
            "major cities will run out of groundwater by 2025-2030. Connecting "
            "dairy and poultry's enormous water footprint to this crisis is "
            "powerful and non-controversial."
        ),
        key_messages=[
            "1 litre doodh = 1000+ litre paani. Jab gaanvon mein peene ka paani nahi, toh ye sahi hai?",
            "NITI Aayog: 2030 tak paani ki maang supply se doguni ho jaayegi.",
            "Poultry farming mein bhi karodon litre paani lagta hai — feed ugaane aur processing mein.",
            "Gujarat ke dairy belt (Banaskantha) mein groundwater khatarnaak level tak gir gaya hai.",
            "Plant-based khaane mein 80% kam paani lagta hai.",
        ],
        target_audience="Everyone — water scarcity affects all classes and communities",
        do_use=[
            "NITI Aayog water crisis report (Composite Water Management Index)",
            "Central Ground Water Board data on groundwater depletion",
            "Water footprint comparisons (milk vs. plant milk, chicken vs. dal)",
            "District-level water stress data for agricultural areas",
            "Summer water tanker images — visceral and real",
        ],
        do_not_use=[
            "Blaming farmers individually",
            "Ignoring industrial water use (textiles, mining) — be fair",
            "Overstating claims without data",
        ],
        example_content=(
            "Banaskantha, Gujarat — desh ka sabse bada doodh utpaadak zila. "
            "CGWB ke data ke mutaabiq, yahan groundwater level har saal 1-2 "
            "metre neeche gir raha hai. Hazaron bore wells sukh chuke hain. "
            "Lekin har roz 3 crore litre se zyada doodh ka utpaadan jaari hai. "
            "Paani pehle ya doodh pehle?"
        ),
    ),
    "economics": CulturalFrame(
        name="Economics & Corporate Power",
        description=(
            "Follow the money. Factory farming consolidates profit with corporations "
            "while squeezing small farmers. Contract farming models (Suguna, Venky's) "
            "transfer all risk to farmers while extracting profit. Amul's cooperative "
            "model is increasingly industrialized."
        ),
        key_messages=[
            "Suguna ka contract farming model: company ka munafa, kisaan ka nuqsaan.",
            "Murgi paalne wale kisaan ko 2-3 rupaye milte hain. Company ko 20-30.",
            "Factory farming se bade kisaan aur corporations ameer hote hain. Chhote kisaan barbad.",
            "Dairy industry Rs 10 lakh crore ki hai. Kitna paisa gaay paalne wale ko milta hai?",
            "Amul cooperative hai ya corporate? Rs 72,000 crore revenue — kisaan ko kitna?",
        ],
        target_audience="Farmers, rural communities, economically aware audiences",
        do_use=[
            "Company annual reports (publicly available for listed companies)",
            "Contract farming terms — risk-reward imbalance",
            "Milk procurement prices vs. retail prices (farmer share)",
            "Subsidy data (NLM, RGM) — who benefits?",
            "Small farmer displacement data",
        ],
        do_not_use=[
            "Anti-business rhetoric without data",
            "Ignoring that farmers need income (always propose alternatives)",
            "Romanticizing subsistence farming",
        ],
        example_content=(
            "Suguna Foods — India ki sabse badi poultry company. Revenue: "
            "Rs 18,000 crore+. Contract farmer ko milta hai: har murge "
            "par Rs 3-5 ka margin. Agar murgi mar jaaye (mortality risk) "
            "toh nuqsaan kisaan ka. Company sirf munafe mein. "
            "Ye hai 'kisaan ke saath' ka matlab?"
        ),
    ),
    "dalit_bahujan_solidarity": CulturalFrame(
        name="Dalit-Bahujan Solidarity & Food Sovereignty",
        description=(
            "CRITICAL FRAME. Animal advocacy in India MUST engage with caste. "
            "The dominant narrative equates vegetarianism with upper-caste purity "
            "and meat-eating with 'impurity'. This is casteist violence. "
            "Our frame MUST center food sovereignty and economic justice, "
            "NOT dietary policing."
        ),
        key_messages=[
            "Har insaan ko ye haq hai ki woh decide kare ki kya khaaye. "
            "Food sovereignty sabka haq hai.",
            "Factory farming se sabse zyada nuqsaan Dalit aur garib communities ko hota hai — "
            "slaughterhouse workers, poultry farm mazdoor, leather workers.",
            "Hum vegetarianism ko upper-caste purity se nahi jodte. "
            "Hum factory farming ke corporate zulm ke khilaf hain.",
            "Contract poultry farming mein mazdoori karne wale — unki sehat, unka haq, "
            "unki suraksha — ye hamara masla hai.",
            "Occupational hazards: slaughterhouse workers face respiratory disease, "
            "injuries, mental health impacts — and no safety protections.",
        ],
        target_audience="Social justice communities, labor movements, progressive organizations",
        do_use=[
            "Worker safety data from slaughterhouses and poultry farms",
            "Economic exploitation of contract farming laborers",
            "Environmental racism: factory farms located near marginalized communities",
            "Solidarity framing: factory farming harms animals AND workers",
            "Quote Dalit-Bahujan thinkers who have written on food sovereignty",
            "Center the voices and agency of affected communities",
        ],
        do_not_use=[
            "NEVER: 'go vegetarian' messaging aimed at Dalit/Muslim communities",
            "NEVER: purity/pollution language about food",
            "NEVER: cow protection rhetoric (deeply entangled with anti-Dalit violence)",
            "NEVER: assume that all Dalits eat meat or that diet defines caste identity",
            "NEVER: speak FOR communities instead of amplifying their own voices",
            "NEVER: ignore that cow vigilantism has killed Dalits and Muslims",
        ],
        example_content=(
            "Factory farming ka sabse bada nuqsaan un logon ko hota hai jo "
            "ismein kaam karte hain. Poultry farm workers ko din mein 12-14 "
            "ghante kaam karna padta hai — ammonia gas, dust, bimariyon ka "
            "khatra. Minimum wages nahi milta. Safety equipment nahi milta. "
            "Ye workers' rights ka masla hai. Ye jaati ka masla hai. "
            "Ye insaaf ka masla hai."
        ),
    ),
}


class CulturalFramer:
    """
    Generate culturally appropriate advocacy content for Indian audiences.

    Provides framing strategies that resonate with Indian cultural contexts
    while explicitly avoiding casteist, communal, and elitist narratives.
    """

    def __init__(self):
        self.frames = FRAMES

    def get_frame(self, frame_name: str) -> Optional[CulturalFrame]:
        """Get a specific cultural frame."""
        return self.frames.get(frame_name)

    def list_frames(self) -> list[str]:
        """List available frames."""
        return list(self.frames.keys())

    def get_do_not_use_guidelines(self) -> dict:
        """Get all 'do not use' guidelines across frames."""
        guidelines = {}
        for name, frame in self.frames.items():
            guidelines[name] = frame.do_not_use
        return guidelines

    def recommend_frames(self, topic: str, audience: str) -> list[str]:
        """Recommend appropriate frames for a topic and audience."""
        recommendations = []
        topic_lower = topic.lower()
        audience_lower = audience.lower()

        if any(w in topic_lower for w in ["dairy", "milk", "cow", "buffalo", "amul"]):
            recommendations.extend(["health_adulteration", "water_crisis", "economics"])
            if "farmer" in audience_lower or "rural" in audience_lower:
                recommendations.append("economics")
            if "health" in audience_lower or "parent" in audience_lower:
                recommendations.append("health_adulteration")

        if any(w in topic_lower for w in ["poultry", "chicken", "egg", "factory"]):
            recommendations.extend(["economics", "health_adulteration"])

        if any(w in topic_lower for w in ["slaughter", "meat", "worker"]):
            recommendations.append("dalit_bahujan_solidarity")

        if any(w in topic_lower for w in ["water", "pollution", "environment"]):
            recommendations.append("water_crisis")

        if any(w in topic_lower for w in ["tradition", "culture", "values"]):
            recommendations.append("ahimsa")

        # Always include ahimsa as a base frame if nothing else matches
        if not recommendations:
            recommendations = ["ahimsa", "health_adulteration"]

        # Remove duplicates while preserving order
        seen = set()
        unique = []
        for r in recommendations:
            if r not in seen:
                seen.add(r)
                unique.append(r)

        return unique

    def generate_content_brief(
        self,
        topic: str,
        audience: str,
        platform: str = "whatsapp",
        frames: Optional[list[str]] = None,
    ) -> str:
        """Generate a content creation brief with framing guidance."""
        if frames is None:
            frames = self.recommend_frames(topic, audience)

        brief = [
            f"CONTENT BRIEF",
            f"=" * 50,
            f"Topic: {topic}",
            f"Audience: {audience}",
            f"Platform: {platform}",
            f"Recommended Frames: {', '.join(frames)}",
            "",
        ]

        for frame_name in frames:
            frame = self.frames.get(frame_name)
            if frame:
                brief.extend([
                    f"--- {frame.name} ---",
                    f"Key messages:",
                ])
                for msg in frame.key_messages[:3]:
                    brief.append(f"  - {msg}")
                brief.append("DO NOT:")
                for dont in frame.do_not_use[:3]:
                    brief.append(f"  - {dont}")
                brief.append("")

        brief.extend([
            "UNIVERSAL GUIDELINES:",
            "- Use accessible Hindustani (see hindi_translator.py glossary)",
            "- Include specific data/citations",
            "- End with a clear call to action",
            "- Do not shame individuals for food choices",
            "- Center compassion, not superiority",
            "- Always provide alternatives, not just criticism",
        ])

        return "\n".join(brief)

    def caste_sensitivity_check(self, content: str) -> list[str]:
        """
        Check content for potentially casteist framing.

        Returns list of warnings. NOT a replacement for review by
        Dalit-Bahujan advocates — always seek that review.
        """
        warnings = []
        content_lower = content.lower()

        problematic_terms = {
            "gau mata": "Avoid 'gau mata' — entangled with Hindutva cow vigilantism",
            "gau raksha": "Avoid 'gau raksha' — associated with violence against Dalits and Muslims",
            "pure vegetarian": "Avoid 'pure vegetarian' — implies impurity of meat-eaters (casteist)",
            "shuddh shakahari": "Avoid 'shuddh shakahari' — purity language is casteist",
            "satvik": "Caution with 'satvik' — can reinforce caste hierarchy through food",
            "tamsik": "Avoid 'tamsik' — designating foods as 'impure' reinforces caste hierarchy",
            "rajsik": "Caution with Ayurvedic food classification — often maps to caste hierarchy",
            "beef ban": "Handle carefully — beef bans have been weaponized against Dalits and Muslims",
            "cow slaughter": "Handle carefully — cow protection movement has caused lynchings",
            "vegan nation": "Avoid nationalist framing of veganism — exclusionary",
            "ancient wisdom": "Caution — 'ancient Indian wisdom' rhetoric often means upper-caste Brahminical texts",
        }

        for term, warning in problematic_terms.items():
            if term in content_lower:
                warnings.append(warning)

        # Check for absence of worker solidarity
        if any(w in content_lower for w in ["slaughter", "meat plant", "processing"]):
            if not any(w in content_lower for w in ["worker", "labour", "labor", "mazdoor"]):
                warnings.append(
                    "Content about slaughterhouses/meat processing should include "
                    "worker welfare perspective — omitting it risks framing that "
                    "dehumanizes workers (who are predominantly Dalit/Muslim)."
                )

        if not warnings:
            warnings.append(
                "No automated issues detected. IMPORTANT: This check is NOT sufficient. "
                "Always have content reviewed by Dalit-Bahujan advocates before publishing."
            )

        return warnings
