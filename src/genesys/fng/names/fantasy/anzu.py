"""
Anzû Name.

Anzû are beings from Mesopotamian religions, sometimes represented as a lesser deity and sometimes
as a monster. They're likewise represented as either a gigantic, fire- and water-breathing bird or
as a lion-headed eagle not too dissimilar from griffins. They're generally tied to rain, with the
roar of a lion representing thunder and a large, dark storm-cloud in the shape of an eagle forming
their body. But in Anzû depictions have changed over time as myths are prone to do.

As far as names go, I've used Mesopotamian names for this name generator. They won't be true names,
but altered ones to create a familiar, but different feel overall to mimic the otherworldly nature
of such a mythical being. Either way, there's plenty to pick from.
"""

from data.fng.names import fantasy
from genesys.fng.database import Database
from genesys.fng.factories.name_block_factory import GenderNameBlockFactory
from genesys.fng.factories.name_factory import ComplexFactory
from models.fng.names.fantasy import AnzuName


DB = Database('anzu', {
    1: fantasy.anzu.nm1,
    2: fantasy.anzu.nm2,
    3: fantasy.anzu.nm3,
    4: fantasy.anzu.nm4,
    5: fantasy.anzu.nm5,
    6: fantasy.anzu.nm6,
})


class AnzuNameFactory(GenderNameBlockFactory):
    """Anzû Name Factory."""

    class MaleNameFactory(ComplexFactory):
        """Method #1."""

        model = AnzuName
        block_map = {
            'nm1': 1,
            'nm2': 2,
        }

    class FemaleNameFactory(ComplexFactory):
        """Method #2."""

        model = AnzuName
        block_map = {
            'nm1': 3,
            'nm2': 4,
        }

    class NeutralNameFactory(ComplexFactory):
        """Method #3."""

        model = AnzuName
        block_map = {
            'nm1': 5,
            'nm2': 6,
        }

    model = AnzuName
    default_data = DB
