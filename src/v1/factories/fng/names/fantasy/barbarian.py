from v1.fixtures import genders
from v1.fixtures.data_block import fill_data
from v1.fixtures.fng.names import fantasy
from v1.models.fng.names.fantasy import BarbarianName, BarbarianName1, BarbarianName2, MaleBarbarianName3, \
    FemaleBarbarianName3
from v1.factories.fng.name_factory import NameFactory, PercentFactory
from v1.factories.fng.validators import generate_while


class BarbarianNameFactory(PercentFactory):
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
        model = BarbarianName1
        block_map = {
            'nm1': 2,
            'nm2': 1,
            'nm3': 4,
        }

    class MaleNameFactory2(NameFactory):
        model = BarbarianName2
        block_map = {
            'nm1': 2,
            'nm2': 1,
            'nm3': 4,
            'nm4': 1,
            'nm5': 3,
        }

        def validate(self, items):
            if items['nm1'].item_id < 3:
                items['nm4'] = generate_while(
                    items['nm4'],
                    lambda item: item.item_id < 3,
                    self['nm4'],
                )

            return items

    class MaleNameFactory3(NameFactory):
        model = MaleBarbarianName3
        block_map = {
            'nm1': 2,
            'nm2': 1,
            'nm3': 4,
            'nm4': 1,
            'nm5': 3,
            'nm6': 1,
            'nm7': 3,
        }

        def validate(self, items):
            if items['nm1'].item_id < 3:
                items['nm4'] = generate_while(
                    items['nm4'],
                    lambda item: item.item_id < 3,
                    self['nm4'],
                )

            if (items['nm1'].item_id < 3) or (items['nm4'].item_id < 3):
                items['nm6'] = generate_while(
                    items['nm6'],
                    lambda item: item.item_id < 3,
                    self['nm6'],
                )

            return items

    class FemaleNameFactory1(NameFactory):
        model = BarbarianName1
        block_map = {
            'nm1': 5,
            'nm2': 6,
            'nm3': 8,
        }

        def validate(self, items):
            items['nm1'] = generate_while(
                items['nm1'],
                lambda item: item.item_id < 5,
                self['nm5'],
            )

            return items

    class FemaleNameFactory2(NameFactory):
        model = BarbarianName2
        block_map = {
            'nm1': 5,
            'nm2': 6,
            'nm3': 8,
            'nm4': 6,
            'nm5': 7,
        }

        def validate(self, items):
            if items['nm2'].item_id < 5:
                items['nm4'] = generate_while(
                    items['nm4'],
                    lambda item: item.item_id < 5,
                    self['nm4'],
                )

            return items

    class FemaleNameFactory3(NameFactory):
        model = FemaleBarbarianName3
        block_map = {
            'nm1': 5,
            'nm2': 6,
            'nm3': 8,
            'nm4': 6,
            'nm5': 7,
            'nm6': 6,
            'nm7': 7,
        }

        def validate(self, items):
            if items['nm2'].item_id < 5:
                items['nm4'] = generate_while(
                    items['nm4'],
                    lambda item: item.item_id < 5,
                    self['nm4'],
                )

            if (items['nm2'].item_id < 5) or (items['nm4'].item_id < 5):
                items['nm6'] = generate_while(
                    items['nm6'],
                    lambda item: item.item_id < 5,
                    self['nm6'],
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
    default_data = fill_data(group_id='barbarian')({
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

    def factory(self, factory_id=0, gender=None):
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
        factory = self.factory(factory_id, gender=gender)

        name = ''
        while name == '':
            name = factory()

        return name
