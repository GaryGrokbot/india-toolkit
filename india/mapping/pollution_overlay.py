"""
Pollution Overlay Analysis

Overlay animal agriculture facility locations with environmental data:
- Water bodies (rivers, lakes, reservoirs)
- Residential areas and population density
- Groundwater quality data (CGWB monitoring network)
- Air quality data (CPCB monitoring stations)

Data sources:
- Central Ground Water Board (CGWB) monitoring data
- CPCB ambient air quality monitoring
- India-WRIS (Water Resources Information System)
- Census 2011 village/town boundaries
- OpenStreetMap for water bodies and settlement data
"""

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

try:
    import rasterio
    HAS_RASTERIO = True
except ImportError:
    HAS_RASTERIO = False


@dataclass
class WaterBody:
    """A water body near an animal agriculture facility."""
    name: str
    water_type: str  # "river", "lake", "reservoir", "canal", "pond", "well"
    distance_km: float
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    quality_data: Optional[dict] = None  # Latest monitoring data


@dataclass
class Settlement:
    """A residential settlement near a facility."""
    name: str
    settlement_type: str  # "village", "town", "city"
    distance_km: float
    population: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


@dataclass
class GroundwaterData:
    """Groundwater quality data for an area."""
    monitoring_well_id: str
    location: str
    depth_m: float
    date_sampled: str
    nitrate_mg_l: Optional[float] = None  # BIS limit: 45 mg/L
    ammonia_mg_l: Optional[float] = None
    tds_mg_l: Optional[float] = None  # BIS limit: 500 mg/L (desirable), 2000 (permissible)
    coliform_mpn: Optional[float] = None  # BIS: 0 per 100ml (drinking)
    fluoride_mg_l: Optional[float] = None  # BIS limit: 1.0 mg/L (desirable), 1.5 (permissible)
    iron_mg_l: Optional[float] = None
    ph: Optional[float] = None  # BIS: 6.5-8.5
    source: str = "CGWB"  # Central Ground Water Board


@dataclass
class PollutionProfile:
    """Pollution profile for a facility and its surroundings."""
    facility_name: str
    facility_lat: Optional[float] = None
    facility_lon: Optional[float] = None
    nearby_water_bodies: list[WaterBody] = field(default_factory=list)
    nearby_settlements: list[Settlement] = field(default_factory=list)
    groundwater_data: list[GroundwaterData] = field(default_factory=list)
    air_quality_data: Optional[dict] = None
    risk_assessment: Optional[str] = None


# Key groundwater quality thresholds (BIS 10500:2012)
BIS_DRINKING_WATER_LIMITS = {
    "nitrate_mg_l": {"desirable": 45, "permissible": 45, "unit": "mg/L",
                     "health_impact": "Methemoglobinemia (blue baby syndrome), linked to cancer"},
    "tds_mg_l": {"desirable": 500, "permissible": 2000, "unit": "mg/L",
                 "health_impact": "Gastrointestinal irritation, scale formation"},
    "coliform_mpn": {"desirable": 0, "permissible": 0, "unit": "MPN/100ml",
                     "health_impact": "Waterborne diseases — typhoid, cholera, dysentery"},
    "ammonia_mg_l": {"desirable": 0.5, "permissible": 0.5, "unit": "mg/L",
                     "health_impact": "Indicator of organic pollution, affects aquatic life"},
    "ph": {"desirable_min": 6.5, "desirable_max": 8.5},
    "fluoride_mg_l": {"desirable": 1.0, "permissible": 1.5, "unit": "mg/L",
                      "health_impact": "Dental and skeletal fluorosis"},
    "iron_mg_l": {"desirable": 0.3, "permissible": 1.0, "unit": "mg/L"},
}

# Known pollution hotspots from animal agriculture
KNOWN_HOTSPOTS = [
    {
        "area": "Namakkal District, Tamil Nadu",
        "type": "Poultry cluster",
        "description": "India's largest poultry cluster. ~50 million birds. Severe water "
                       "and air pollution from manure runoff and dead bird disposal. "
                       "Nitrate contamination in groundwater. Ammonia emissions.",
        "operators": ["Suguna", "SKM", "numerous small operators"],
        "livestock_census_poultry": 39_000_000,
    },
    {
        "area": "West Godavari District, Andhra Pradesh",
        "type": "Aquaculture (shrimp)",
        "description": "Massive shrimp farming belt. Conversion of agricultural land and "
                       "mangroves. Salinization of groundwater. Antibiotic residues in "
                       "waterways. Disease outbreaks (White Spot, EMS).",
        "operators": ["Avanti Feeds", "numerous small operators"],
    },
    {
        "area": "Anand-Kheda Districts, Gujarat",
        "type": "Dairy cluster (Amul belt)",
        "description": "Heart of Amul cooperative. High density of dairy animals. "
                       "Methane emissions, water consumption for fodder, effluent from "
                       "chilling centres and processing plants.",
        "operators": ["GCMMF/Amul member unions"],
    },
    {
        "area": "Pune-Nashik Belt, Maharashtra",
        "type": "Poultry and dairy",
        "description": "Large concentration of Venky's operations and dairy farms. "
                       "Processing plant effluent. Contract farming density.",
        "operators": ["Venky's", "Godrej Agrovet"],
    },
    {
        "area": "Nellore District, Andhra Pradesh",
        "type": "Aquaculture (shrimp and fish)",
        "description": "Major aquaculture zone. Coastal pollution, mangrove destruction, "
                       "antibiotic use in ponds.",
        "operators": ["Avanti Feeds", "Waterbase", "numerous small operators"],
    },
    {
        "area": "Banaskantha District, Gujarat",
        "type": "Dairy",
        "description": "Largest milk-producing district in India (Banas Dairy). "
                       "Massive water footprint for fodder. Groundwater depletion.",
        "operators": ["Banaskantha District Co-operative Milk Producers' Union"],
    },
]


class PollutionOverlay:
    """
    Overlay animal agriculture facilities with environmental data.

    Combines facility locations from FacilityMapper with water body proximity,
    settlement proximity, groundwater quality, and air quality to create
    pollution profiles for advocacy and PIL support.
    """

    def __init__(self):
        self.profiles: list[PollutionProfile] = []
        self.hotspots = KNOWN_HOTSPOTS
        self.bis_limits = BIS_DRINKING_WATER_LIMITS

    def create_profile(
        self,
        facility_name: str,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
    ) -> PollutionProfile:
        """Create a new pollution profile for a facility."""
        profile = PollutionProfile(
            facility_name=facility_name,
            facility_lat=latitude,
            facility_lon=longitude,
        )
        self.profiles.append(profile)
        return profile

    def add_water_body(
        self,
        profile: PollutionProfile,
        name: str,
        water_type: str,
        distance_km: float,
        quality_data: Optional[dict] = None,
    ) -> None:
        """Add a nearby water body to a profile."""
        wb = WaterBody(
            name=name,
            water_type=water_type,
            distance_km=distance_km,
            quality_data=quality_data,
        )
        profile.nearby_water_bodies.append(wb)

    def add_settlement(
        self,
        profile: PollutionProfile,
        name: str,
        settlement_type: str,
        distance_km: float,
        population: Optional[int] = None,
    ) -> None:
        """Add a nearby settlement to a profile."""
        settlement = Settlement(
            name=name,
            settlement_type=settlement_type,
            distance_km=distance_km,
            population=population,
        )
        profile.nearby_settlements.append(settlement)

    def add_groundwater_data(
        self,
        profile: PollutionProfile,
        well_id: str,
        location: str,
        depth_m: float,
        date_sampled: str,
        **params,
    ) -> None:
        """Add groundwater monitoring data to a profile."""
        gw = GroundwaterData(
            monitoring_well_id=well_id,
            location=location,
            depth_m=depth_m,
            date_sampled=date_sampled,
            nitrate_mg_l=params.get("nitrate_mg_l"),
            ammonia_mg_l=params.get("ammonia_mg_l"),
            tds_mg_l=params.get("tds_mg_l"),
            coliform_mpn=params.get("coliform_mpn"),
            fluoride_mg_l=params.get("fluoride_mg_l"),
            iron_mg_l=params.get("iron_mg_l"),
            ph=params.get("ph"),
        )
        profile.groundwater_data.append(gw)

    def assess_risk(self, profile: PollutionProfile) -> str:
        """
        Generate risk assessment for a facility.

        Checks:
        - Proximity to water bodies (<500m = high risk)
        - Proximity to settlements (<1km = high risk)
        - Groundwater contamination exceeding BIS limits
        - Population potentially affected
        """
        risks = []
        risk_level = "LOW"

        # Water body proximity
        close_water = [wb for wb in profile.nearby_water_bodies if wb.distance_km < 0.5]
        if close_water:
            risk_level = "HIGH"
            for wb in close_water:
                risks.append(
                    f"CRITICAL: {wb.name} ({wb.water_type}) is only {wb.distance_km:.1f} km "
                    f"from the facility. Effluent runoff risk is severe."
                )

        medium_water = [wb for wb in profile.nearby_water_bodies if 0.5 <= wb.distance_km < 2.0]
        if medium_water:
            if risk_level != "HIGH":
                risk_level = "MEDIUM"
            for wb in medium_water:
                risks.append(
                    f"WARNING: {wb.name} ({wb.water_type}) is {wb.distance_km:.1f} km away. "
                    f"Contamination risk during monsoon season."
                )

        # Settlement proximity
        close_settlements = [s for s in profile.nearby_settlements if s.distance_km < 1.0]
        if close_settlements:
            risk_level = "HIGH"
            total_pop = sum(s.population or 0 for s in close_settlements)
            risks.append(
                f"CRITICAL: {len(close_settlements)} settlements within 1 km. "
                f"Estimated {total_pop:,} people affected by air pollution (ammonia, "
                f"particulate matter) and odour."
            )

        # Groundwater
        for gw in profile.groundwater_data:
            if gw.nitrate_mg_l and gw.nitrate_mg_l > 45:
                risk_level = "HIGH"
                risks.append(
                    f"CRITICAL: Nitrate level {gw.nitrate_mg_l} mg/L at well {gw.monitoring_well_id} "
                    f"exceeds BIS limit of 45 mg/L. Indicates organic (manure) contamination. "
                    f"Health risk: methemoglobinemia, cancer."
                )
            if gw.coliform_mpn and gw.coliform_mpn > 0:
                risk_level = "HIGH"
                risks.append(
                    f"CRITICAL: Coliform detected ({gw.coliform_mpn} MPN/100ml) at well "
                    f"{gw.monitoring_well_id}. BIS limit is 0. Fecal contamination likely "
                    f"from animal waste."
                )
            if gw.ammonia_mg_l and gw.ammonia_mg_l > 0.5:
                risks.append(
                    f"WARNING: Ammonia level {gw.ammonia_mg_l} mg/L at well {gw.monitoring_well_id} "
                    f"exceeds BIS limit of 0.5 mg/L."
                )

        assessment = f"RISK LEVEL: {risk_level}\n\n"
        if risks:
            assessment += "FINDINGS:\n" + "\n".join(f"- {r}" for r in risks)
        else:
            assessment += "No significant risks identified with available data."

        assessment += "\n\nRECOMMENDATIONS:\n"
        if risk_level == "HIGH":
            assessment += (
                "- File complaint with State Pollution Control Board immediately.\n"
                "- Consider PIL under Article 21 (right to clean environment).\n"
                "- RTI for facility's CTO conditions and compliance reports.\n"
                "- Document affected communities for impact statement.\n"
                "- Contact National Green Tribunal if SPCB is non-responsive."
            )
        elif risk_level == "MEDIUM":
            assessment += (
                "- File RTI with SPCB for effluent monitoring data.\n"
                "- Monitor groundwater quality quarterly.\n"
                "- Document conditions during monsoon (peak runoff risk).\n"
                "- Engage local panchayat/municipal body."
            )
        else:
            assessment += (
                "- Continue monitoring.\n"
                "- File RTI for baseline data.\n"
                "- Establish community water quality monitoring."
            )

        profile.risk_assessment = assessment
        return assessment

    def get_known_hotspots(self) -> list[dict]:
        """Get known pollution hotspots from animal agriculture."""
        return self.hotspots

    def generate_report(self, profile: PollutionProfile) -> str:
        """Generate a text report for a pollution profile."""
        lines = [
            f"POLLUTION PROFILE: {profile.facility_name}",
            "=" * 60,
            "",
        ]

        if profile.facility_lat and profile.facility_lon:
            lines.append(f"Coordinates: {profile.facility_lat}, {profile.facility_lon}")
            lines.append("")

        lines.append("NEARBY WATER BODIES:")
        if profile.nearby_water_bodies:
            for wb in sorted(profile.nearby_water_bodies, key=lambda x: x.distance_km):
                lines.append(f"  - {wb.name} ({wb.water_type}): {wb.distance_km:.1f} km")
        else:
            lines.append("  No data.")

        lines.append("")
        lines.append("NEARBY SETTLEMENTS:")
        if profile.nearby_settlements:
            for s in sorted(profile.nearby_settlements, key=lambda x: x.distance_km):
                pop = f", population: {s.population:,}" if s.population else ""
                lines.append(f"  - {s.name} ({s.settlement_type}): {s.distance_km:.1f} km{pop}")
        else:
            lines.append("  No data.")

        lines.append("")
        lines.append("GROUNDWATER QUALITY:")
        if profile.groundwater_data:
            for gw in profile.groundwater_data:
                lines.append(f"  Well {gw.monitoring_well_id} ({gw.location}, {gw.date_sampled}):")
                if gw.nitrate_mg_l is not None:
                    flag = " [EXCEEDS BIS LIMIT]" if gw.nitrate_mg_l > 45 else ""
                    lines.append(f"    Nitrate: {gw.nitrate_mg_l} mg/L{flag}")
                if gw.ammonia_mg_l is not None:
                    flag = " [EXCEEDS BIS LIMIT]" if gw.ammonia_mg_l > 0.5 else ""
                    lines.append(f"    Ammonia: {gw.ammonia_mg_l} mg/L{flag}")
                if gw.tds_mg_l is not None:
                    flag = " [EXCEEDS DESIRABLE]" if gw.tds_mg_l > 500 else ""
                    lines.append(f"    TDS: {gw.tds_mg_l} mg/L{flag}")
                if gw.coliform_mpn is not None:
                    flag = " [CONTAMINATED]" if gw.coliform_mpn > 0 else ""
                    lines.append(f"    Coliform: {gw.coliform_mpn} MPN/100ml{flag}")
        else:
            lines.append("  No data.")

        if profile.risk_assessment:
            lines.append("")
            lines.append(profile.risk_assessment)

        return "\n".join(lines)

    def export_profiles_json(self, filepath: str) -> None:
        """Export all profiles to JSON."""
        data = []
        for p in self.profiles:
            data.append({
                "facility_name": p.facility_name,
                "latitude": p.facility_lat,
                "longitude": p.facility_lon,
                "water_bodies": [
                    {"name": wb.name, "type": wb.water_type, "distance_km": wb.distance_km}
                    for wb in p.nearby_water_bodies
                ],
                "settlements": [
                    {"name": s.name, "type": s.settlement_type,
                     "distance_km": s.distance_km, "population": s.population}
                    for s in p.nearby_settlements
                ],
                "risk_assessment": p.risk_assessment,
            })
        Path(filepath).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
