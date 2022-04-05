import random
from utils import genders
from database.data_block import fill_data
from data.fng.names import fantasy
from models.fng.names.fantasy import AnimatronicName
from genesys.fng.factories.name_block_factory import NameBlockFactory, GenderNameBlockFactory
from genesys.fng.factories.name_factory import ComplexNameFactory, GenderFactory, BaseNameFactory


class AnimatronicNamePartFactory(BaseNameFactory):
    def get_data(self, *args, **kwargs):
        items = list(self.factory_data.find(*args, **kwargs))
        if len(items) == 0:
            return {}

        return random.choice(items)


class BaseAnimatronicNameFactory(ComplexNameFactory):
    model = AnimatronicName

    def __init__(self, data=None):
        """
        :param data: Data blocks for factory
        """
        super().__init__(data)
        self.factories = {
            factory_id: AnimatronicNamePartFactory(self.factory_data.find(block_id=block_id))
            for factory_id, block_id in self.block_map.items()
        }

    def validate(self, items) -> dict:
        print("VALIDATE", items)
        item = items['nm1'].items.get('value', [[], []])
        print("ITEM", item)
        return {
            'nm0': random.choice(item[0]),
            'nm1': random.choice(item[1]),
        }

    def __call__(self, *args, **kwargs):
        """
        Main factory method

        :param args: Model args
        :param kwargs: Fields to search in data
        :return: Model, built by factory
        """
        print("DATA", args, kwargs)
        values = self.get_data(*args, **kwargs)
        print("VALUES", values)
        values = self.validate(values)
        return self.build(*args, **values)


class AnimatronicNameFactory(GenderNameBlockFactory):
    """Animatronic Name Factory

    There's a large variety of names in this generator. Some are normal, friendly names you'd expect for normal
    animatronics, other names are more creepy for the horror kinds of animatronics, like those in the Five Nights at
    Freddy's games.
    With thousands of different names, there's plenty to pick from for all sorts of genres and purposes."""

    class MaleNameFactory(BaseAnimatronicNameFactory):
        block_map = {
            'nm1': 1,
        }

    class FemaleNameFactory(BaseAnimatronicNameFactory):
        block_map = {
            'nm1': 2,
        }

    factory_classes = {
        genders.MALE: MaleNameFactory,
        genders.FEMALE: FemaleNameFactory,
    }

    default_data = fill_data(group_id='animatronic')({
        1: fantasy.animatronic.nm1,
        2: fantasy.animatronic.nm2,
    })
