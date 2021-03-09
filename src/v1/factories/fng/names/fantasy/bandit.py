from v1.fixtures import genders
from v1.fixtures.data_block import load_data
from v1.fixtures.fng.names import fantasy
from v1.models.fng.names.fantasy import BanditName
from v1.factories.fng.name_factory import NameFactory, ComplexNameFactory


class BanditNameFactory(ComplexNameFactory):
    """Bandit Name Factory

    The names rely on nicknames to create a bandit-feel. They could be named after their reputation, their appearance,
    or even their way of theft.
    There are no last names, but some of the first names could also be used as a last name. There are plenty of real
    name generators to offer you surnames though."""

    class MaleNameFactory1(NameFactory):
        name_class = BanditName
        blocks_map = {
            1: genders.MALE,
            2: 2,
        }

    class FemaleNameFactory1(NameFactory):
        name_class = BanditName
        blocks_map = {
            1: genders.FEMALE,
            2: 2,
        }

    class MaleNameFactory2(NameFactory):
        name_class = BanditName
        blocks_map = {
            1: 3,
            2: genders.MALE,
        }

    class FemaleNameFactory2(NameFactory):
        name_class = BanditName
        blocks_map = {
            1: 3,
            2: genders.FEMALE,
        }

    factory_classes = {
        f"{genders.MALE}.1": MaleNameFactory1,
        f"{genders.FEMALE}.1": FemaleNameFactory1,
        f"{genders.MALE}.2": MaleNameFactory2,
        f"{genders.FEMALE}.2": FemaleNameFactory2,
    }
    default_blocks = load_data({
        genders.MALE: fantasy.bandit.namesMale,
        genders.FEMALE: fantasy.bandit.namesFemale,
        2: fantasy.bandit.names2,
        3: fantasy.bandit.names3,
    })

    @property
    def default_gender(self):
        return genders.MALE

    def factory(self, factory_id, gender=None):
        if gender is None:
            gender = self.default_gender

        if factory_id < 50:
            __factory_id = 1
        else:
            __factory_id = 2

        return self.factories.get(f"{gender}.{__factory_id}")

    def __call__(self, *args, factory_id=None, gender=None, **kwargs) -> BanditName:
        if factory_id is None:
            factory_id = self.factory_id()

        factory = self.factory(factory_id, gender=gender)

        name = ''
        while name == '':
            name = factory()

        return name
