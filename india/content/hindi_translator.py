"""
Hindi Translation Framework

Translates advocacy content into accessible Hindustani (Hindi-Urdu register)
that reaches the widest possible audience. Key principles:

1. USE ACCESSIBLE HINDUSTANI: paani (not jal), doodh (not dugdh),
   janwar (not pashu). Avoid Sanskritized Hindi that alienates
   Urdu speakers, Muslims, and people from non-Hindi-belt states.

2. WHATSAPP-OPTIMIZED: Short paragraphs, emoji for visual breaks,
   maximum 300 words per message. No PDFs — text only.

3. BILINGUAL WHERE NEEDED: Hindi text with key English terms retained
   where they are commonly used (e.g., "factory farm", "pollution",
   "antibiotic").

4. NO TRANSLITERATION SNOBBERY: Accept that people read Hindi in
   both Devanagari and Roman script. Provide both where possible.

5. REGIONAL SENSITIVITY: Avoid assuming Hindi is universal. Many
   target audiences (Tamil Nadu, Kerala, Karnataka, Andhra Pradesh,
   Northeast) prefer English or regional languages.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TranslatedContent:
    """Bilingual content piece."""
    english: str
    hindi_devanagari: str
    hindi_roman: str  # Romanized Hindi for WhatsApp
    format_type: str  # "whatsapp", "social_media", "pamphlet", "poster"
    word_count_hindi: int = 0
    character_count: int = 0


# Common advocacy terms — accessible Hindustani equivalents
GLOSSARY = {
    # Use the Hindustani/common word, not the Sanskrit-derived one
    "water": ("paani", "पानी"),  # NOT "jal" (जल)
    "milk": ("doodh", "दूध"),  # NOT "dugdh"
    "animal": ("janwar", "जानवर"),  # NOT "pashu" (पशु) except in formal/legal
    "cow": ("gaay", "गाय"),
    "buffalo": ("bhains", "भैंस"),
    "chicken": ("murgi/murga", "मुर्गी/मुर्गा"),
    "egg": ("anda", "अंडा"),
    "meat": ("gosht/maas", "गोश्त/मांस"),
    "fish": ("machhli", "मछली"),
    "farmer": ("kisaan", "किसान"),
    "factory farm": ("factory farm", "फ़ैक्ट्री फ़ार्म"),  # Retain English
    "pollution": ("pradushan", "प्रदूषण"),
    "disease": ("bimari", "बीमारी"),  # NOT "rog" (रोग)
    "health": ("sehat", "सेहत"),  # NOT "swasthya" in casual register
    "medicine": ("dawai", "दवाई"),  # NOT "aushadhi"
    "food": ("khaana", "खाना"),  # NOT "aahar"
    "cruelty": ("zulm", "ज़ुल्म"),  # OR "berahmi" — NOT "kroorta" in casual
    "suffering": ("takleef", "तकलीफ़"),  # NOT "kasht"
    "right": ("haq", "हक़"),  # OR "adhikar" — both are fine
    "government": ("sarkaar", "सरकार"),  # NOT "shaasan"
    "law": ("qaanoon", "क़ानून"),  # NOT "vidhi"
    "truth": ("sach/sachai", "सच/सचाई"),  # NOT "satya" in casual
    "lie": ("jhooth", "झूठ"),  # NOT "asatya"
    "money": ("paisa", "पैसा"),  # NOT "dhan"
    "profit": ("munafa/faayda", "मुनाफ़ा/फ़ायदा"),  # NOT "laabh" in casual
    "company": ("company", "कंपनी"),  # Retain English
    "antibiotic": ("antibiotic", "एंटीबायोटिक"),  # Retain English
    "hormone": ("hormone", "हॉर्मोन"),  # Retain English
    "cancer": ("cancer", "कैंसर"),  # Retain English — understood universally
    "environment": ("maahol/vaatavaran", "माहौल/वातावरण"),
    "poison": ("zahar", "ज़हर"),  # NOT "vish"
}

# Common WhatsApp formatting
WHATSAPP_FORMAT = {
    "max_words": 300,
    "max_chars": 1500,
    "line_break": "\n",
    "section_break": "\n\n",
    "emphasis_start": "*",
    "emphasis_end": "*",
    "italic_start": "_",
    "italic_end": "_",
}


class HindiTranslator:
    """
    Translation framework for Hindi/Hindustani advocacy content.

    Produces WhatsApp-optimized, bilingual content using accessible
    language that reaches the widest audience.
    """

    def __init__(self):
        self.glossary = GLOSSARY
        self.format = WHATSAPP_FORMAT

    def get_term(self, english_term: str) -> tuple[str, str]:
        """Get Hindi equivalent (roman, devanagari) for an English term."""
        term = self.glossary.get(english_term.lower())
        if term:
            return term
        return (english_term, english_term)  # Return as-is if not in glossary

    def create_whatsapp_message(
        self,
        hindi_text: str,
        english_text: Optional[str] = None,
        include_english: bool = True,
    ) -> TranslatedContent:
        """
        Create a WhatsApp-optimized bilingual message.

        Returns content formatted for WhatsApp sharing: short paragraphs,
        emphasis markers, within character limits.
        """
        # Build Hindi message (Devanagari)
        hindi_formatted = self._format_for_whatsapp(hindi_text)

        # Build romanized version
        hindi_roman = ""  # Would need transliteration engine

        english = english_text or ""

        if include_english and english:
            combined = f"{hindi_formatted}\n\n---\n\n{english}"
        else:
            combined = hindi_formatted

        return TranslatedContent(
            english=english,
            hindi_devanagari=hindi_formatted,
            hindi_roman=hindi_roman,
            format_type="whatsapp",
            word_count_hindi=len(hindi_text.split()),
            character_count=len(combined),
        )

    def create_social_media_post(
        self,
        hindi_text: str,
        english_text: str,
        platform: str = "twitter",  # "twitter", "instagram", "facebook"
    ) -> TranslatedContent:
        """Create a social media post with bilingual content."""
        max_chars = {
            "twitter": 280,
            "instagram": 2200,
            "facebook": 63206,
        }

        limit = max_chars.get(platform, 2200)

        # Combine for platform
        combined_hindi = hindi_text[:limit]

        return TranslatedContent(
            english=english_text,
            hindi_devanagari=combined_hindi,
            hindi_roman="",
            format_type=f"social_media_{platform}",
            word_count_hindi=len(hindi_text.split()),
            character_count=len(combined_hindi),
        )

    def dairy_facts_hindi(self) -> str:
        """Pre-built: Dairy industry facts in Hindi (accessible Hindustani)."""
        return (
            "*दूध की सचाई जो आपको कोई नहीं बताता* 🐄\n"
            "\n"
            "1️⃣ भारत में हर साल 4 करोड़ से ज़्यादा बछड़े पैदा होते हैं। "
            "नर बछड़ों को दूध नहीं दे सकते, इसलिए उन्हें छोड़ दिया जाता है या "
            "कसाई को बेच दिया जाता है।\n"
            "\n"
            "2️⃣ गाय और भैंस को बार-बार गर्भवती किया जाता है ताकि दूध मिलता रहे। "
            "जब दूध कम हो जाता है, तो उन्हें भी बेच दिया जाता है।\n"
            "\n"
            "3️⃣ FSSAI की जाँच में दूध में मिलावट पाई गई है — "
            "यूरिया, डिटर्जेंट, स्टार्च, और पानी। ये आपकी सेहत के लिए "
            "ख़तरनाक है।\n"
            "\n"
            "4️⃣ एक लीटर दूध बनाने में 1000 लीटर से ज़्यादा पानी लगता है। "
            "जब हमारे गाँवों में पीने का पानी नहीं है, तो क्या ये सही है?\n"
            "\n"
            "5️⃣ Dairy industry में antibiotics का भारी इस्तेमाल होता है। "
            "ये दूध के ज़रिए आपके शरीर में आते हैं और antibiotic resistance "
            "बढ़ाते हैं।\n"
            "\n"
            "*सोचिए। जानिए। बदलिए।* 🌱\n"
            "\n"
            "आगे भेजें ➡️"
        )

    def water_crisis_hindi(self) -> str:
        """Pre-built: Water crisis and dairy connection in Hindi."""
        return (
            "*पानी का संकट और dairy industry का कनेक्शन* 💧\n"
            "\n"
            "भारत दुनिया का सबसे बड़ा दूध उत्पादक है — 23 करोड़ टन/साल।\n"
            "\n"
            "लेकिन इसकी क़ीमत:\n"
            "\n"
            "💧 1 लीटर दूध = 1000+ लीटर पानी\n"
            "(चारा उगाने, जानवरों को पिलाने, सफ़ाई, processing)\n"
            "\n"
            "💧 भारत के 23 करोड़ टन दूध के लिए सालाना ~230 अरब लीटर पानी चाहिए\n"
            "\n"
            "💧 NITI Aayog की रिपोर्ट: 2030 तक भारत में पानी की माँग "
            "उपलब्धता से दोगुनी हो जाएगी\n"
            "\n"
            "💧 21 बड़े शहरों का groundwater 2025-2030 तक ख़त्म होने की आशंका\n"
            "\n"
            "💧 Dairy farming वाले इलाक़ों (बनासकांठा, आणंद, नामक्कल) में "
            "groundwater level तेज़ी से गिर रहा है\n"
            "\n"
            "हम पानी की बर्बादी को रोक सकते हैं:\n"
            "🌱 Plant-based दूध (सोया, बादाम, नारियल) में 80% कम पानी लगता है\n"
            "🌱 दालों और सब्ज़ियों से protein मिलता है, बिना पानी बर्बाद किए\n"
            "\n"
            "*पानी बचाएँ। भविष्य बचाएँ।* 🌍\n"
            "\n"
            "आगे भेजें ➡️"
        )

    def _format_for_whatsapp(self, text: str) -> str:
        """Format text for WhatsApp readability."""
        # Ensure paragraphs are separated
        lines = text.split("\n")
        formatted = []
        for line in lines:
            line = line.strip()
            if line:
                formatted.append(line)
            else:
                formatted.append("")
        return "\n".join(formatted)

    def get_glossary(self) -> dict:
        """Return the full glossary."""
        return self.glossary

    def language_guide(self) -> str:
        """Return guidelines for writing accessible Hindi content."""
        return (
            "LANGUAGE GUIDE: Writing Accessible Hindi for Animal Advocacy\n"
            "=" * 60 + "\n\n"
            "1. USE HINDUSTANI, NOT SANSKRITIZED HINDI\n"
            "   - paani, not jal\n"
            "   - doodh, not dugdh\n"
            "   - janwar, not pashu (except in legal contexts)\n"
            "   - dawai, not aushadhi\n"
            "   - sehat, not swasthya (casual register)\n"
            "   - zulm/berahmi, not kroorta (casual register)\n"
            "   - haq, not adhikar (both acceptable)\n"
            "   - sarkaar, not shaasan\n"
            "   - qaanoon, not vidhi\n\n"
            "2. RETAIN ENGLISH FOR TECHNICAL TERMS\n"
            "   - antibiotic, hormone, cancer, pollution, factory farm\n"
            "   - These are understood across language boundaries\n\n"
            "3. SHORT SENTENCES\n"
            "   - Max 15-20 words per sentence\n"
            "   - One idea per paragraph\n"
            "   - Use numbered lists\n\n"
            "4. AVOID\n"
            "   - Religious framing (no 'gau mata' rhetoric — see CULTURAL_SENSITIVITY.md)\n"
            "   - Caste-based food shaming\n"
            "   - Assumptions about diet\n"
            "   - Dense academic language\n\n"
            "5. WHATSAPP SPECIFICS\n"
            "   - Max 300 words per message\n"
            "   - Use *bold* for emphasis\n"
            "   - Use emoji as visual anchors (sparingly)\n"
            "   - End with 'Forward kijiye' / 'आगे भेजें'\n"
            "   - No attachments — text only for maximum reach\n"
        )
