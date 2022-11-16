"""
Barbarian Name.

A barbarian could be pretty much anything, it's mostly a term that relies on the eye of the
beholder. A barbarian is usually somebody seen as a primitive and often rough and cruel person, so
anybody could fit that description, but there are some stereotypes. Vikings are often seen as
barbarians, as were many Nordic people. Ancient Mongolians are often seen as barbarians, and so
were Native Americans. Since enemies are often seen as barbarians as well, pretty much every group
of people has probably been considered to be barbaric.

This generator has a lot of different possible influences for each name, some real, some fictional
and some merely because it sounds 'barbaric'. This means there's a wide variety of possible names,
so some names will fit a specific culture better than others. Most names do share the same overall
feel however, so while not all names would work well together as a single culture, the vast
majority of names should still work for many stereotypical barbarian styles, as well as several
other styles.
"""

from data.fng.names import fantasy
from genesys.fng.database import Database
from genesys.fng.factories.name_block_factory import MultipleFactoryNameFactory, \
    GenderNameBlockFactory
from genesys.fng.factories.name_factory import ComplexFactory
from models.fng.names.fantasy import BarbarianName


DB = Database('barbarian', {
    1: fantasy.barbarian.nm1,
    2: fantasy.barbarian.nm2,
    3: fantasy.barbarian.nm3,
    4: fantasy.barbarian.nm4,
    5: fantasy.barbarian.nm5,
    6: fantasy.barbarian.nm6,
    7: fantasy.barbarian.nm7,
    8: fantasy.barbarian.nm8,
})


class BarbarianNameFactory(GenderNameBlockFactory):
    """Barbarian Name Factory."""

    class MaleNameFactory(MultipleFactoryNameFactory):
        """Method #1."""

        class MaleNameFactory1(ComplexFactory):
            """Method #1."""

            model = BarbarianName
            block_map = {
                'nm1': 2,
                'nm2': 1,
                'nm3': 4,
            }

        class MaleNameFactory2(ComplexFactory):
            """Method #2."""

            model = BarbarianName
            block_map = {
                'nm1': 2,
                'nm2': 1,
                'nm3': 4,
                'nm4': 1,
                'nm5': 3,
            }
            validators = {
                'nm4': lambda items: lambda item: items['nm1'].item_id >= 3 or item.item_id >=3,
            }

        class MaleNameFactory3(ComplexFactory):
            """Method #3."""

            model = BarbarianName
            block_map = {
                'nm1': 2,
                'nm2': 1,
                'nm3': 4,
                'nm4': 1,
                'nm5': 3,
                'nm6': 1,
                'nm7': 3,
            }
            validators = {
                'nm4': lambda items: lambda item: items['nm1'].item_id >= 3 or item.item_id >=3,
                'nm6': lambda items: lambda item: item.item_id >= 3 \
                    or ((items['nm1'].item_id >= 3) and (items['nm4'].item_id >= 3)),
            }

        model = BarbarianName
        factory_classes = [
            MaleNameFactory1,
            MaleNameFactory2,
            MaleNameFactory3,
        ]

    class FemaleNameFactory(MultipleFactoryNameFactory):
        """Method #1."""

        class FemaleNameFactory1(ComplexFactory):
            """Method #1."""

            model = BarbarianName
            block_map = {
                'nm1': 5,
                'nm2': 6,
                'nm3': 8,
            }
            validators = {
                'nm1': lambda items: lambda item: items['nm1'].item_id >= 5,
            }

        class FemaleNameFactory2(ComplexFactory):
            """Method #2."""

            model = BarbarianName
            block_map = {
                'nm1': 5,
                'nm2': 6,
                'nm3': 8,
                'nm4': 6,
                'nm5': 7,
            }
            validators = {
                'nm4': lambda items: lambda item: items['nm2'].item_id >= 5 or item.item_id >=5,
            }

        class FemaleNameFactory3(ComplexFactory):
            """Method #3."""

            model = BarbarianName
            block_map = {
                'nm1': 5,
                'nm2': 6,
                'nm3': 8,
                'nm4': 6,
                'nm5': 7,
                'nm6': 6,
                'nm7': 7,
            }
            validators = {
                'nm4': lambda items: lambda item: items['nm2'].item_id >= 5 or item.item_id >=5,
                'nm6': lambda items: lambda item: item.item_id >= 5 \
                    or ((items['nm2'].item_id >= 5) and (items['nm4'].item_id >= 5)),
            }

        model = BarbarianName
        factory_classes = [
            FemaleNameFactory1,
            FemaleNameFactory2,
            FemaleNameFactory3,
        ]

    model = BarbarianName
    default_data = DB
