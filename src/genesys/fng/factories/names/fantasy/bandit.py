"""
Bandit Name.

The names rely on nicknames to create a bandit-feel. They could be named after their reputation,
their appearance, or even their way of theft.
There are no last names, but some of the first names could also be used as a last name. There are
plenty of real name generators to offer you surnames though."""

from data.fng.names import fantasy
from genesys.fng.database import Database
from genesys.fng.factories.name_block_factory import NameBlockFactory, GenderNameBlockFactory
from genesys.fng.factories.name_factory import ComplexNameFactory
from models.fng.names.fantasy import BanditName
from utils import genders


DB = Database('bandit', {
    genders.MALE: fantasy.bandit.namesMale,
    genders.FEMALE: fantasy.bandit.namesFemale,
    2: fantasy.bandit.names2,
    3: fantasy.bandit.names3,
})


class BanditNameFactory(GenderNameBlockFactory):
    """Bandit Name Factory."""

    class MaleNameFactory(NameBlockFactory):
        """Method #1."""

        class MaleNameFactory1(ComplexNameFactory):
            """Method #1."""

            model = BanditName
            block_map = {
                'nm1': genders.MALE,
                'nm2': 2,
            }

        class MaleNameFactory2(ComplexNameFactory):
            """Method #2."""

            model = BanditName
            block_map = {
                'nm1': 3,
                'nm2': genders.MALE,
            }

        factory_classes = {
            f"{genders.MALE}.1": MaleNameFactory1,
            f"{genders.MALE}.2": MaleNameFactory2,
        }

    class FemaleNameFactory(NameBlockFactory):
        """Method #1."""

        class FemaleNameFactory1(ComplexNameFactory):
            """Method #1."""

            model = BanditName
            block_map = {
                'nm1': genders.FEMALE,
                'nm2': 2,
            }

        class FemaleNameFactory2(ComplexNameFactory):
            """Method #2."""

            model = BanditName
            block_map = {
                'nm1': 3,
                'nm2': genders.FEMALE,
            }

        factory_classes = {
            f"{genders.FEMALE}.1": FemaleNameFactory1,
            f"{genders.FEMALE}.2": FemaleNameFactory2,
        }

    default_data = DB
