"""
Artificial Intelligence Name.

Artificial intelligence beings often have names related to robotics or electric concepts, these are
also the names you'll find in this generator. However, logically speaking, artificial intelligence
could have regular names just like humans do, or non-artificial intelligence. Obviously there are
dozens upon dozens of real name generators to pick from on this site.
The names in this generator cover themes like robotics, electronics, purposes, and in some cases
identity as well.
"""

from database.data_block import fill_data
from data.fng.names import fantasy
from models.fng.names.fantasy import ArtificialIntelligenceName
from genesys.fng.factories.name_block_factory import SimpleNameBlockFactory


class ArtificialIntelligenceNameFactory(SimpleNameBlockFactory):
    """Artificial Intelligence Name Factory."""

    default_data = fill_data(group_id='artificial-intelligence')({
        1: fantasy.artificial_intelligence.nm1,
    })

    block_map = {
        'nm1': 1,
    }

    model = ArtificialIntelligenceName
