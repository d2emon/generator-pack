"""
Banshee Name.

A banshee is a female spirit who mourns the loss of a relative, and tends to do so by shrieking
loudly. There are many different variants of banshees today, some come to existence through huge
amounts of pain for example, while others are simply beings with the power to deafen their enemies.
The overlapping theme is almost always high pitched screams and feminine spirits though.

Banshees originate in Irish mythology, and as such the only named banshees have Irish names. Since
I already have an Irish name generator on this site I decided to focus entirely on the more
nickname-like names instead. Names like "The Ivory Maiden" or "The Shrieking Wife", for example.
These names tend to be more common in games as well, but if you want to add more back-story to your
banshee, and require a personal name, I definitely recommend starting with real names, either Irish
or otherwise depending on the cultural background you need.
"""

from data.fng.names import fantasy
from genesys.fng.database import Database
from genesys.fng.factories.name_factory import ComplexNameFactory
from models.fng.names.fantasy import BansheeName


DB = Database('banshee', {
    'nm1': fantasy.banshee.nm1,
    'nm2': fantasy.banshee.nm2,
})


class BansheeNameFactory(ComplexNameFactory):
    """Banshee Name Factory."""

    model = BansheeName
    default_data = DB
    block_map = {
        'nm1': 'nm1',
        'nm2': 'nm2',
    }
