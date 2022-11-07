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
from genesys.fng.factories.name_block_factory import NameBlockFactory, GenderNameBlockFactory
from genesys.fng.factories.name_factory import ComplexNameFactory
from genesys.fng.factories.validators import generate_while
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

    class MaleNameFactory(NameBlockFactory):
        """Method #1."""

        class MaleNameFactory1(ComplexNameFactory):
            """Method #1."""

            model = BarbarianName
            block_map = {
                'nm1': 2,
                'nm2': 1,
                'nm3': 4,
            }

        class MaleNameFactory2(ComplexNameFactory):
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
                'nm4': lambda items: items['nm4'].item_id < 3,
            }

            def validate_item(self, item_id, item, items):
                """
                Validate item.

                :param item_id str: Id of current item
                :param item: Current item
                :param items list: Generated items
                :return: ItemId of current item
                :rtype: list
                """
                if item_id == 'nm4':
                    if items['nm1'].item_id >= 3:
                        return items

                return super().validate_item(item_id, item, items)

        class MaleNameFactory3(ComplexNameFactory):
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
                'nm4': lambda items: items['nm4'].item_id < 3,
                'nm6': lambda items: items['nm6'].item_id < 3,
            }

            def validate_item(self, item_id, item, items):
                """
                Validate item.

                :param item_id str: Id of current item
                :param item: Current item
                :param items list: Generated items
                :return: ItemId of current item
                :rtype: list
                """
                if item_id == 'nm4':
                    if items['nm1'].item_id >= 3:
                        return items

                if item_id == 'nm6':
                    if (items['nm1'].item_id >= 3) and (items['nm4'].item_id >= 3):
                        return items

                return super().validate_item(item_id, item, items)

        factory_classes = {
            0: MaleNameFactory1,
            1: MaleNameFactory2,
            2: MaleNameFactory3,
        }

    class FemaleNameFactory(NameBlockFactory):
        """Method #1."""

        class FemaleNameFactory1(ComplexNameFactory):
            """Method #1."""

            model = BarbarianName
            block_map = {
                'nm1': 5,
                'nm2': 6,
                'nm3': 8,
            }

            def validate_item(self, item_id, item, items):
                """
                Validate item.

                :param item_id str: Id of current item
                :param item: Current item
                :param items list: Generated items
                :return: ItemId of current item
                :rtype: list
                """
                if item_id == 'nm1':
                    return generate_while(
                        items['nm1'],
                        lambda item: item.item_id < 5,
                        self['nm5'],
                    )

                return super().validate_item(item_id, item, items)

        class FemaleNameFactory2(ComplexNameFactory):
            """Method #2."""

            model = BarbarianName
            block_map = {
                'nm1': 5,
                'nm2': 6,
                'nm3': 8,
                'nm4': 6,
                'nm5': 7,
            }

            def validate_item(self, item_id, item, items):
                """
                Validate item.

                :param item_id str: Id of current item
                :param item: Current item
                :param items list: Generated items
                :return: ItemId of current item
                :rtype: list
                """
                if item_id == 'nm4':
                    if items['nm2'].item_id < 5:
                        return generate_while(
                            items['nm4'],
                            lambda item: item.item_id < 5,
                            self['nm5'],
                        )

                return super().validate_item(item_id, item, items)

        class FemaleNameFactory3(ComplexNameFactory):
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
                'nm4': lambda items: items['nm4'].item_id < 5,
                'nm6': lambda items: items['nm6'].item_id < 5,
            }

            def validate_item(self, item_id, item, items):
                """
                Validate item.

                :param item_id str: Id of current item
                :param item: Current item
                :param items list: Generated items
                :return: ItemId of current item
                :rtype: list
                """
                if item_id == 'nm4':
                    if items['nm2'].item_id >= 5:
                        return items

                if item_id == 'nm6':
                    if (items['nm2'].item_id >= 5) and (items['nm4'].item_id >= 5):
                        return items

                return super().validate_item(item_id, item, items)

        factory_classes = {
            0: FemaleNameFactory1,
            1: FemaleNameFactory2,
            2: FemaleNameFactory3,
        }

    model = BarbarianName
    default_data = DB
