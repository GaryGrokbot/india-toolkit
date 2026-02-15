"""
Factory Farm Facility Mapper

Map industrial animal agriculture facilities across India using:
- State Pollution Control Board (SPCB) consent records
- Satellite imagery (Sentinel-2, Landsat via Google Earth Engine)
- 20th Livestock Census (2019) district-level data
- FSSAI license registries
- Company annual reports and filings (MCA/ROC)

Major operators tracked:
- Poultry: Suguna Foods, Venky's (India) Ltd, IB Group, Godrej Agrovet, SKM Group
- Dairy: GCMMF (Amul), Hatsun Agro, Heritage Foods, Parag Milk Foods, Kwality Ltd
- Integrated: Godrej Agrovet, Cargill India, Allana Group
- Aquaculture: Avanti Feeds, Waterbase Ltd, The Coastal Corporation
"""

import json
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional


class FacilityType(str, Enum):
    POULTRY_BROILER = "poultry_broiler"
    POULTRY_LAYER = "poultry_layer"
    POULTRY_BREEDER = "poultry_breeder"
    POULTRY_HATCHERY = "poultry_hatchery"
    POULTRY_PROCESSING = "poultry_processing"
    DAIRY_FARM = "dairy_farm"
    DAIRY_PROCESSING = "dairy_processing"
    DAIRY_CHILLING = "dairy_chilling_centre"
    PIGGERY = "piggery"
    GOAT_SHEEP_FARM = "goat_sheep_farm"
    AQUACULTURE_SHRIMP = "aquaculture_shrimp"
    AQUACULTURE_FISH = "aquaculture_fish"
    SLAUGHTERHOUSE = "slaughterhouse"
    MEAT_PROCESSING = "meat_processing"
    FEED_MILL = "feed_mill"
    RENDERING = "rendering_plant"


class PCBCategory(str, Enum):
    RED = "red"  # Slaughterhouses, large meat processing
    ORANGE = "orange"  # Poultry >5000 birds, large dairy
    GREEN = "green"  # Small operations
    WHITE = "white"  # Minimal pollution


@dataclass
class Facility:
    """An animal agriculture facility."""
    name: str
    facility_type: FacilityType
    operator: str
    state: str
    district: str
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    pcb_category: Optional[PCBCategory] = None
    cto_number: Optional[str] = None
    cto_valid_until: Optional[str] = None
    fssai_license: Optional[str] = None
    capacity: Optional[str] = None  # e.g., "50,000 birds", "500 cattle"
    animal_count: Optional[int] = None
    employees: Optional[int] = None
    annual_revenue_crore: Optional[float] = None
    parent_company: Optional[str] = None
    cin: Optional[str] = None  # Corporate Identity Number (MCA)
    notes: Optional[str] = None
    data_sources: list[str] = field(default_factory=list)


# Major operators and known facilities
MAJOR_OPERATORS = {
    "suguna_foods": {
        "name": "Suguna Foods Private Limited",
        "cin": "U01222TZ1984PTC001395",
        "headquarters": "Coimbatore, Tamil Nadu",
        "type": "Poultry (integrated)",
        "scale": "India's largest poultry integrator. ~16 million birds/day capacity. "
                 "Contract farming model across 25+ states.",
        "revenue_2024_crore": 18000,  # approx
        "key_states": ["Tamil Nadu", "Andhra Pradesh", "Telangana", "Karnataka",
                       "Maharashtra", "Odisha", "West Bengal", "Assam"],
        "brands": ["Suguna", "Suguna Daily Fresh"],
        "model": "Contract farming — company provides chicks, feed, medicines; "
                 "farmer provides land and labour. Farmer bears mortality risk.",
        "welfare_concerns": [
            "Broiler chickens reach slaughter weight in 35-40 days (accelerated growth)",
            "Contract farmers have no control over breed, feed, or medicines",
            "High stocking density in broiler sheds",
            "Antibiotic growth promoters used until recent FSSAI restrictions",
            "Dead bird disposal often inadequate",
        ],
    },
    "venkys": {
        "name": "Venky's (India) Limited",
        "cin": "L15100PN1976PLC020926",
        "headquarters": "Pune, Maharashtra",
        "type": "Poultry (integrated, publicly listed BSE: 523261)",
        "scale": "Second-largest poultry company. Breeder farms, hatcheries, "
                 "feed plants, processing plants across India.",
        "revenue_2024_crore": 8500,
        "key_states": ["Maharashtra", "Madhya Pradesh", "Rajasthan", "Gujarat",
                       "Karnataka", "Chhattisgarh"],
        "brands": ["Venky's", "Venky's Xprs"],
        "model": "Combination of own farms and contract farming.",
        "welfare_concerns": [
            "Intensive broiler operations with standard industry practices",
            "Large-scale breeder operations for genetic stock",
            "Processing plants handle millions of birds annually",
        ],
    },
    "ib_group": {
        "name": "IB Group (Indodan Hatcheries)",
        "cin": "U01223RJ1993PLC007410",
        "headquarters": "Rajnandgaon, Chhattisgarh",
        "type": "Poultry (integrated)",
        "scale": "Third-largest poultry integrator. Major presence in central and eastern India.",
        "revenue_2024_crore": 7000,
        "key_states": ["Chhattisgarh", "Madhya Pradesh", "Rajasthan", "Odisha",
                       "Jharkhand", "West Bengal", "Bihar"],
        "brands": ["IB"],
        "model": "Contract farming and own operations.",
    },
    "godrej_agrovet": {
        "name": "Godrej Agrovet Limited",
        "cin": "L15410MH1991PLC135359",
        "headquarters": "Mumbai, Maharashtra",
        "type": "Diversified (poultry, dairy, aqua feed, crop protection). BSE: 543318",
        "scale": "Part of Godrej Group. Animal feed, oil palm, dairy (Creamline Dairy), "
                 "poultry (Godrej Tyson JV until 2021, now Real Good Chicken).",
        "revenue_2024_crore": 9500,
        "key_states": ["Maharashtra", "Andhra Pradesh", "Telangana", "Tamil Nadu",
                       "Karnataka", "Madhya Pradesh"],
        "brands": ["Real Good Chicken", "Creamline Dairy"],
        "subsidiaries": [
            "Creamline Dairy Products Ltd (dairy processing)",
            "Astec LifeSciences (crop protection, not animal ag)",
        ],
    },
    "gcmmf_amul": {
        "name": "Gujarat Cooperative Milk Marketing Federation Ltd (GCMMF/Amul)",
        "headquarters": "Anand, Gujarat",
        "type": "Dairy (cooperative federation)",
        "scale": "World's largest dairy cooperative. 3.6 million+ farmer members. "
                 "~26 million litres milk/day collection. 90+ products.",
        "revenue_2024_crore": 72000,  # Rs. 72,000 crore (FY2023-24)
        "key_states": ["Gujarat"],  # Collection primarily Gujarat
        "brands": ["Amul"],
        "member_unions": [
            "Kaira District Co-operative Milk Producers' Union (original Amul)",
            "Banaskantha District Co-operative Milk Producers' Union (largest union)",
            "Surat District Co-operative Milk Producers' Union",
            "Mehsana District Co-operative Milk Producers' Union",
            "Sabarkantha District Co-operative Milk Producers' Union",
            # 18 district unions total
        ],
        "welfare_concerns": [
            "Cooperative model marketed as farmer-friendly obscures industrial scale",
            "Male calf abandonment/sale to informal slaughter — systematic issue",
            "Artificial insemination drives with imported semen (Holstein/Jersey crossbreeding)",
            "Oxytocin injection for milk let-down (banned 2018 but enforcement weak)",
            "Antibiotic use for mastitis treatment — residues detected in milk samples",
            "Water footprint: 1000+ litres per litre of milk produced",
        ],
    },
    "hatsun_agro": {
        "name": "Hatsun Agro Product Limited",
        "cin": "L15200TN1986PLC012747",
        "headquarters": "Chennai, Tamil Nadu",
        "type": "Dairy (private, publicly listed BSE: 531531)",
        "scale": "Largest private dairy company in India by milk procurement. "
                 "~7.5 million litres/day procurement.",
        "revenue_2024_crore": 8500,
        "key_states": ["Tamil Nadu", "Andhra Pradesh", "Telangana", "Karnataka", "Maharashtra"],
        "brands": ["Arun Ice Creams", "Arokya", "Hatsun", "Ibaco"],
    },
    "heritage_foods": {
        "name": "Heritage Foods Limited",
        "cin": "L15209AP1992PLC014953",
        "headquarters": "Hyderabad, Telangana",
        "type": "Dairy (private, publicly listed BSE: 519552)",
        "scale": "~3.5 million litres/day procurement. Founded by N. Chandrababu Naidu.",
        "revenue_2024_crore": 3500,
        "key_states": ["Andhra Pradesh", "Telangana", "Karnataka", "Tamil Nadu",
                       "Maharashtra", "Rajasthan", "Haryana", "Punjab"],
        "brands": ["Heritage"],
    },
    "parag_milk_foods": {
        "name": "Parag Milk Foods Limited",
        "cin": "L15204PN2012PLC142830",
        "headquarters": "Pune, Maharashtra",
        "type": "Dairy (private, publicly listed BSE: 539889)",
        "scale": "Known for Gowardhan and Go brands. Cheese and whey focus.",
        "revenue_2024_crore": 3200,
        "key_states": ["Maharashtra", "Andhra Pradesh", "Karnataka"],
        "brands": ["Gowardhan", "Go Cheese", "Pride of Cows"],
    },
    "skm_group": {
        "name": "SKM Animal Feeds & Foods (India) Pvt Ltd",
        "headquarters": "Erode, Tamil Nadu",
        "type": "Poultry & Eggs (integrated)",
        "scale": "Major egg and poultry producer in South India. Large layer operations.",
        "key_states": ["Tamil Nadu", "Andhra Pradesh", "Karnataka"],
        "brands": ["SKM"],
    },
    "allana_group": {
        "name": "Allana Group (Frigerio Conserva Allana)",
        "headquarters": "Mumbai, Maharashtra",
        "type": "Meat processing and export (buffalo meat)",
        "scale": "India's largest buffalo meat exporter. Multiple APEDA-approved "
                 "processing plants. Major markets: Vietnam, Malaysia, Egypt, Saudi Arabia.",
        "revenue_2024_crore": 15000,
        "key_states": ["Maharashtra", "Uttar Pradesh", "Andhra Pradesh"],
        "brands": ["Allana", "Frigerio"],
        "welfare_concerns": [
            "Buffalo sourcing from dairy industry — spent/unproductive buffaloes",
            "Transport conditions from rural areas to processing plants",
            "Scale of operation — one of largest meat processors globally",
        ],
    },
    "avanti_feeds": {
        "name": "Avanti Feeds Limited",
        "cin": "L16001AP1993PLC015890",
        "headquarters": "Hyderabad, Telangana",
        "type": "Aquaculture (shrimp feed and processing, BSE: 512573)",
        "scale": "Largest shrimp feed producer in India. JV with Thai Union Group.",
        "revenue_2024_crore": 5500,
        "key_states": ["Andhra Pradesh", "Gujarat", "Tamil Nadu", "Odisha"],
        "brands": ["Avanti"],
    },
}


class FacilityMapper:
    """
    Map and track industrial animal agriculture facilities across India.

    Data sources:
    - RTI responses from State Pollution Control Boards
    - FSSAI license registry (public)
    - MCA corporate filings (CIN lookup)
    - Livestock Census data (DAHD)
    - Satellite imagery (manual or GEE integration)
    - Media reports and company disclosures
    """

    def __init__(self, data_dir: Optional[Path] = None):
        self.data_dir = data_dir or Path(__file__).parent.parent.parent / "data"
        self.facilities: list[Facility] = []
        self.operators = MAJOR_OPERATORS

    def add_facility(self, facility: Facility) -> None:
        """Add a facility to the map."""
        self.facilities.append(facility)

    def load_from_json(self, filepath: str) -> int:
        """Load facilities from a JSON file. Returns count loaded."""
        path = Path(filepath)
        if not path.exists():
            return 0
        data = json.loads(path.read_text(encoding="utf-8"))
        count = 0
        for item in data:
            facility = Facility(
                name=item["name"],
                facility_type=FacilityType(item["facility_type"]),
                operator=item["operator"],
                state=item["state"],
                district=item["district"],
                address=item.get("address"),
                latitude=item.get("latitude"),
                longitude=item.get("longitude"),
                pcb_category=PCBCategory(item["pcb_category"]) if item.get("pcb_category") else None,
                cto_number=item.get("cto_number"),
                capacity=item.get("capacity"),
                animal_count=item.get("animal_count"),
                notes=item.get("notes"),
                data_sources=item.get("data_sources", []),
            )
            self.facilities.append(facility)
            count += 1
        return count

    def save_to_json(self, filepath: str) -> None:
        """Save all facilities to JSON."""
        data = []
        for f in self.facilities:
            data.append({
                "name": f.name,
                "facility_type": f.facility_type.value,
                "operator": f.operator,
                "state": f.state,
                "district": f.district,
                "address": f.address,
                "latitude": f.latitude,
                "longitude": f.longitude,
                "pcb_category": f.pcb_category.value if f.pcb_category else None,
                "cto_number": f.cto_number,
                "capacity": f.capacity,
                "animal_count": f.animal_count,
                "notes": f.notes,
                "data_sources": f.data_sources,
            })
        Path(filepath).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    def get_operator_info(self, operator_key: str) -> Optional[dict]:
        """Get information about a major operator."""
        return self.operators.get(operator_key)

    def list_operators(self) -> list[dict]:
        """List all known major operators."""
        return [
            {"key": k, "name": v["name"], "type": v["type"]}
            for k, v in self.operators.items()
        ]

    def filter_by_state(self, state: str) -> list[Facility]:
        """Get facilities in a specific state."""
        return [f for f in self.facilities if f.state.lower() == state.lower()]

    def filter_by_district(self, district: str, state: Optional[str] = None) -> list[Facility]:
        """Get facilities in a specific district."""
        results = [f for f in self.facilities if f.district.lower() == district.lower()]
        if state:
            results = [f for f in results if f.state.lower() == state.lower()]
        return results

    def filter_by_type(self, facility_type: FacilityType) -> list[Facility]:
        """Get facilities of a specific type."""
        return [f for f in self.facilities if f.facility_type == facility_type]

    def filter_by_operator(self, operator: str) -> list[Facility]:
        """Get facilities by operator name (partial match)."""
        operator_lower = operator.lower()
        return [f for f in self.facilities if operator_lower in f.operator.lower()]

    def get_stats(self) -> dict:
        """Get summary statistics of mapped facilities."""
        by_type = {}
        by_state = {}
        by_operator = {}

        for f in self.facilities:
            by_type[f.facility_type.value] = by_type.get(f.facility_type.value, 0) + 1
            by_state[f.state] = by_state.get(f.state, 0) + 1
            by_operator[f.operator] = by_operator.get(f.operator, 0) + 1

        return {
            "total_facilities": len(self.facilities),
            "by_type": by_type,
            "by_state": by_state,
            "by_operator": by_operator,
            "with_coordinates": sum(1 for f in self.facilities if f.latitude and f.longitude),
            "with_cto": sum(1 for f in self.facilities if f.cto_number),
        }

    def generate_geojson(self) -> dict:
        """Generate GeoJSON FeatureCollection of all facilities with coordinates."""
        features = []
        for f in self.facilities:
            if f.latitude and f.longitude:
                feature = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [f.longitude, f.latitude],
                    },
                    "properties": {
                        "name": f.name,
                        "type": f.facility_type.value,
                        "operator": f.operator,
                        "state": f.state,
                        "district": f.district,
                        "capacity": f.capacity,
                        "pcb_category": f.pcb_category.value if f.pcb_category else None,
                    },
                }
                features.append(feature)

        return {
            "type": "FeatureCollection",
            "features": features,
        }

    def get_livestock_census_context(self, state: str) -> dict:
        """
        Get 20th Livestock Census (2019) context for a state.

        Data from: Department of Animal Husbandry and Dairying,
        20th Livestock Census, 2019.
        """
        # National totals from 20th Livestock Census 2019
        national = {
            "total_livestock": 535_780_000,
            "cattle": 192_490_000,
            "buffalo": 109_850_000,
            "sheep": 74_260_000,
            "goat": 148_880_000,
            "pig": 9_060_000,
            "total_poultry": 851_810_000,
            "source": "20th Livestock Census, 2019, DAHD",
        }

        # Top states by livestock (approximate from census)
        state_data = {
            "uttar pradesh": {"cattle": 19_600_000, "buffalo": 33_000_000, "goat": 15_700_000},
            "rajasthan": {"cattle": 13_900_000, "buffalo": 12_900_000, "sheep": 7_900_000, "goat": 20_800_000},
            "madhya pradesh": {"cattle": 19_300_000, "buffalo": 10_700_000, "goat": 10_400_000},
            "west bengal": {"cattle": 16_700_000, "buffalo": 700_000, "goat": 16_200_000},
            "bihar": {"cattle": 12_200_000, "buffalo": 7_800_000, "goat": 12_800_000},
            "maharashtra": {"cattle": 13_900_000, "buffalo": 6_200_000, "goat": 10_600_000},
            "andhra pradesh": {"cattle": 6_600_000, "buffalo": 10_300_000, "sheep": 13_900_000, "poultry": 227_000_000},
            "tamil nadu": {"cattle": 8_800_000, "buffalo": 780_000, "sheep": 4_600_000, "goat": 8_100_000, "poultry": 117_000_000},
            "karnataka": {"cattle": 9_500_000, "buffalo": 3_700_000, "sheep": 11_100_000},
            "telangana": {"cattle": 4_600_000, "buffalo": 5_000_000, "sheep": 19_100_000, "poultry": 79_000_000},
            "gujarat": {"cattle": 10_400_000, "buffalo": 10_700_000},
            "punjab": {"cattle": 2_300_000, "buffalo": 5_200_000},
            "haryana": {"cattle": 1_800_000, "buffalo": 6_100_000},
        }

        return {
            "national": national,
            "state": state_data.get(state.lower(), {}),
            "note": "District-level data available via RTI to DAHD or state animal husbandry department.",
        }
