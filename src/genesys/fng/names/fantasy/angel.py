"""
Angel Name.

These angel names are great for any fantasy story, especially those with a more traditional style
in terms of names.

The names have been divided into male, female and neutral. The neutral names are also part of the
male and female names, so you'll likely come across some doubles if you're looking in multiple
sections.
"""

from data.fng.names import fantasy
from genesys.fng.database import Database
from genesys.fng.factories.name_block_factory import GenderNameBlockFactory
from genesys.fng.factories.name_factory import ComplexFactory
from models.fng.names.fantasy import AngelName


DB = Database('angel', {
    1: fantasy.angel.names1,
    2: fantasy.angel.names2,
    3: fantasy.angel.names3,
})


class AngelNameFactory(GenderNameBlockFactory):
    """Angel Name Factory."""

    class MaleNameFactory(ComplexFactory):
        """Method #1."""

        model = AngelName
        block_map = {
            'nm1': 1,
        }

    class FemaleNameFactory(ComplexFactory):
        """Method #2."""

        model = AngelName
        block_map = {
            'nm1': 2,
        }

    class NeutralNameFactory(ComplexFactory):
        """Method #3."""

        model = AngelName
        block_map = {
            'nm1': 3,
        }

    model = AngelName
    default_data = DB