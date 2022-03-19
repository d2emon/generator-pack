import random
from v1.fixtures import genders
from v1.fixtures.data_block import fill_data
from v1.fixtures.fng.names import fantasy
from v1.models.fng.names.fantasy import BanditName
from v1.factories.fng.name_factory import NameFactory, PercentFactory


class BanditNameFactory(PercentFactory):
    """Bandit Name Factory

    The names rely on nicknames to create a bandit-feel. They could be named after their reputation, their appearance,
    or even their way of theft.
    There are no last names, but some of the first names could also be used as a last name. There are plenty of real
    name generators to offer you surnames though."""

    class MaleNameFactory1(NameFactory):
        model = BanditName
        block_map = {
            'nm1': genders.MALE,
            'nm2': 2,
        }

    class FemaleNameFactory1(NameFactory):
        model = BanditName
        block_map = {
            'nm1': genders.FEMALE,
            'nm2': 2,
        }

    class MaleNameFactory2(NameFactory):
        model = BanditName
        block_map = {
            'nm1': 3,
            'nm2': genders.MALE,
        }

    class FemaleNameFactory2(NameFactory):
        model = BanditName
        block_map = {
            'nm1': 3,
            'nm2': genders.FEMALE,
        }

    factory_classes = {
        f"{genders.MALE}.1": MaleNameFactory1,
        f"{genders.FEMALE}.1": FemaleNameFactory1,
        f"{genders.MALE}.2": MaleNameFactory2,
        f"{genders.FEMALE}.2": FemaleNameFactory2,
    }
    default_data = fill_data(group_id='bandit')({
        genders.MALE: fantasy.bandit.namesMale,
        genders.FEMALE: fantasy.bandit.namesFemale,
        2: fantasy.bandit.names2,
        3: fantasy.bandit.names3,
    })

    @property
    def default_gender(self):
        return genders.MALE

    def factory(self, factory_id=None, gender=None):
        if gender is None:
            gender = self.default_gender
        if factory_id is None:
            factory_id = random.randrange(100)

        if factory_id < 50:
            __factory_id = 1
        else:
            __factory_id = 2

        return self.factories.get(f"{gender}.{__factory_id}")

    def __call__(self, *args, factory_id=None, gender=None, **kwargs) -> BanditName:
        factory = self.factory(factory_id=factory_id, gender=gender)

        name = ''
        while name == '':
            name = factory()

        return name
