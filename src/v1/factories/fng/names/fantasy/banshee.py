from v1.fixtures.data_block import load_data
from v1.fixtures.fng.names import fantasy
from v1.models.fng.names.fantasy import BansheeName
from v1.factories.fng.name_factory import NameFactory


class BansheeNameFactory(NameFactory):
    """Banshee Name Factory

    A banshee is a female spirit who mourns the loss of a relative, and tends to do so by shrieking loudly. There are
    many different variants of banshees today, some come to existence through huge amounts of pain for example, while
    others are simply beings with the power to deafen their enemies. The overlapping theme is almost always high pitched
    screams and feminine spirits though.

    Banshees originate in Irish mythology, and as such the only named banshees have Irish names. Since I already have an
    Irish name generator on this site I decided to focus entirely on the more nickname-like names instead. Names like
    "The Ivory Maiden" or "The Shrieking Wife", for example. These names tend to be more common in games as well, but if
    you want to add more back-story to your banshee, and require a personal name, I definitely recommend starting with
    real names, either Irish or otherwise depending on the cultural background you need."""

    name_class = BansheeName
    blocks_map = {
        1: 1,
        2: 2,
    }
    default_blocks = load_data({
        1: fantasy.banshee.nm1,
        2: fantasy.banshee.nm2,
    })
