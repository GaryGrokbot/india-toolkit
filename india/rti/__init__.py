"""
RTI (Right to Information) Act 2005 automation.

Generate, file, and track RTI requests targeting animal agriculture
oversight bodies across India.
"""

from india.rti.rti_generator import RTIGenerator
from india.rti.rti_tracker import RTITracker

__all__ = ["RTIGenerator", "RTITracker"]
