"""
Factory Farm Mapping

Map industrial animal agriculture facilities using pollution control board data,
satellite imagery, and livestock census data. Overlay with environmental and
community data.
"""

from india.mapping.facility_mapper import FacilityMapper
from india.mapping.pollution_overlay import PollutionOverlay

__all__ = ["FacilityMapper", "PollutionOverlay"]
