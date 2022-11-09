"""
Artificial Intelligence Name.

Artificial intelligence beings often have names related to robotics or electric concepts, these are
also the names you'll find in this generator. However, logically speaking, artificial intelligence
could have regular names just like humans do, or non-artificial intelligence. Obviously there are
dozens upon dozens of real name generators to pick from on this site.
The names in this generator cover themes like robotics, electronics, purposes, and in some cases
identity as well.
"""

from data.fng.names import fantasy
from genesys.fng.database import Database
from genesys.fng.factories.name_factory import ComplexFactory
from models.fng.names.fantasy import ArtificialIntelligenceName


DB = Database('artificial-intelligence', {
    1: fantasy.artificial_intelligence.nm1,
})


class ArtificialIntelligenceNameFactory(ComplexFactory):
    """Artificial Intelligence Name Factory."""

    model = ArtificialIntelligenceName
    default_data = DB
    block_map = {
        'nm1': 1,
    }
