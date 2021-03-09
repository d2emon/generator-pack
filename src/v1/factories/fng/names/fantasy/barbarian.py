from v1.fixtures import genders
from v1.fixtures.data_block import load_data
from v1.fixtures.fng.names import fantasy
from v1.models.fng.names.fantasy import BarbarianName, BarbarianName1, BarbarianName2, MaleBarbarianName3, \
    FemaleBarbarianName3
from v1.factories.fng.name_factory import NameFactory, ComplexNameFactory
from v1.factories.fng.validators import generate_while


class BarbarianNameFactory(ComplexNameFactory):
    """Barbarian Name Factory

    A barbarian could be pretty much anything, it's mostly a term that relies on the eye of the beholder. A barbarian is
    usually somebody seen as a primitive and often rough and cruel person, so anybody could fit that description, but
    there are some stereotypes. Vikings are often seen as barbarians, as were many Nordic people. Ancient Mongolians are
    often seen as barbarians, and so were Native Americans. Since enemies are often seen as barbarians as well, pretty
    much every group of people has probably been considered to be barbaric.

    This generator has a lot of different possible influences for each name, some real, some fictional and some merely
    because it sounds 'barbaric'. This means there's a wide variety of possible names, so some names will fit a specific
    culture better than others. Most names do share the same overall feel however, so while not all names would work
    well together as a single culture, the vast majority of names should still work for many stereotypical barbarian
    styles, as well as several other styles."""

    class MaleNameFactory1(NameFactory):
        name_class = BarbarianName1
        blocks_map = {
            1: 2,
            2: 1,
            3: 4,
        }

    class MaleNameFactory2(NameFactory):
        name_class = BarbarianName2
        blocks_map = {
            1: 2,
            2: 1,
            3: 4,
            4: 1,
            5: 3,
        }

        def validate(self, items):
            if items[1].item_id < 3:
                items[4] = generate_while(
                    items[4],
                    lambda item: item.item_id < 3,
                    self.blocks[1],
                )

            return items

    class MaleNameFactory3(NameFactory):
        name_class = MaleBarbarianName3
        blocks_map = {
            1: 2,
            2: 1,
            3: 4,
            4: 1,
            5: 3,
            6: 1,
            7: 3,
        }

        def validate(self, items):
            if items[1].item_id < 3:
                items[4] = generate_while(
                    items[4],
                    lambda item: item.item_id < 3,
                    self.blocks[1],
                )

            if (items[1].item_id < 3) or (items[4].item_id < 3):
                items[6] = generate_while(
                    items[6],
                    lambda item: item.item_id < 3,
                    self.blocks[1],
                )

            return items

    class FemaleNameFactory1(NameFactory):
        name_class = BarbarianName1
        blocks_map = {
            1: 5,
            2: 6,
            3: 8,
        }

        def validate(self, items):
            items[1] = generate_while(
                items[1],
                lambda item: item.item_id < 5,
                self.blocks[5],
            )

            return items

    class FemaleNameFactory2(NameFactory):
        name_class = BarbarianName2
        blocks_map = {
            1: 5,
            2: 6,
            3: 8,
            4: 6,
            5: 7,
        }

        def validate(self, items):
            if items[2].item_id < 5:
                items[4] = generate_while(
                    items[4],
                    lambda item: item.item_id < 5,
                    self.blocks[6],
                )

            return items

    class FemaleNameFactory3(NameFactory):
        name_class = FemaleBarbarianName3
        blocks_map = {
            1: 5,
            2: 6,
            3: 8,
            4: 6,
            5: 7,
            6: 6,
            7: 7,
        }

        def validate(self, items):
            if items[2].item_id < 5:
                items[4] = generate_while(
                    items[4],
                    lambda item: item.item_id < 5,
                    self.blocks[6],
                )

            if (items[2].item_id < 5) or (items[4].item_id < 5):
                items[6] = generate_while(
                    items[6],
                    lambda item: item.item_id < 5,
                    self.blocks[6],
                )

            return items

    factory_classes = {
        f"{genders.MALE}.1": MaleNameFactory1,
        f"{genders.FEMALE}.1": FemaleNameFactory1,
        f"{genders.MALE}.2": MaleNameFactory2,
        f"{genders.FEMALE}.2": FemaleNameFactory2,
        f"{genders.MALE}.3": MaleNameFactory3,
        f"{genders.FEMALE}.3": FemaleNameFactory3,
    }
    default_blocks = load_data({
        1: fantasy.barbarian.nm1,
        2: fantasy.barbarian.nm2,
        3: fantasy.barbarian.nm3,
        4: fantasy.barbarian.nm4,
        5: fantasy.barbarian.nm5,
        6: fantasy.barbarian.nm6,
        7: fantasy.barbarian.nm7,
        8: fantasy.barbarian.nm8,
    })

    @property
    def default_gender(self):
        return genders.MALE

    def factory(self, factory_id, gender=None):
        if gender is None:
            gender = self.default_gender

        if factory_id < 30:
            __factory_id = 1
        elif factory_id < 80:
            __factory_id = 2
        else:
            __factory_id = 3

        return self.factories.get(f"{gender}.{__factory_id}")

    def __call__(self, *args, factory_id=None, gender=None, **kwargs) -> BarbarianName:
        if factory_id is None:
            factory_id = self.factory_id()

        factory = self.factory(factory_id, gender=gender)

        name = ''
        while name == '':
            name = factory()

        return name
