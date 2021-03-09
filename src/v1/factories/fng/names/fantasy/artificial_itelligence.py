from v1.fixtures.data_block import load_data
from v1.fixtures.fng.names import fantasy
from v1.models.fng.names.fantasy import ArtificialIntelligenceName
from v1.factories.fng.name_factory import NameFactory


class ArtificialIntelligenceNameFactory(NameFactory):
    """Artificial Intelligence Name Factory

    Artificial intelligence beings often have names related to robotics or electric concepts, these are also the names
    you'll find in this generator. However, logically speaking, artificial intelligence could have regular names just
    like humans do, or non-artificial intelligence. Obviously there are dozens upon dozens of real name generators to
    pick from on this site.
    The names in this generator cover themes like robotics, electronics, purposes, and in some cases identity as
    well."""

    default_blocks = load_data({
        1: fantasy.artificial_intelligence.nm1,
    })
    blocks_map = {
        1: 1,
    }
    name_class = ArtificialIntelligenceName
