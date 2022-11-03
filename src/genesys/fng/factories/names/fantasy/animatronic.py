"""
Animatronic Name.

There's a large variety of names in this generator. Some are normal, friendly names you'd expect
for normal animatronics, other names are more creepy for the horror kinds of animatronics, like
those in the Five Nights at Freddy's games.
With thousands of different names, there's plenty to pick from for all sorts of genres and
purposes.
"""

import random
from data.fng.names import fantasy
from genesys.fng.database import Database
from genesys.fng.factories.name_block_factory import GenderNameBlockFactory
from genesys.fng.factories.name_factory import ComplexNameFactory, BaseNameFactory
from models.fng.names.fantasy import AnimatronicName
from utils import genders


DB = Database('animatronic', {
    1: fantasy.animatronic.nm1,
    2: fantasy.animatronic.nm2,
})


class AnimatronicNamePartFactory(BaseNameFactory):
    """Method #1."""

    def get_data(self, *args, **kwargs):
        """
        Generate value from data

        :param args: Args for generation
        :param kwargs: Kwargs for generation
        :return: Generated value
        """
        items = list(self.data.find(*args, **kwargs))
        if len(items) == 0:
            return {}

        return random.choice(items)


class BaseAnimatronicNameFactory(ComplexNameFactory):
    """Method #1."""

    model = AnimatronicName

    def __init__(self, data=None):
        """
        :param data: Data blocks for factory
        """
        super().__init__(data)
        self.factories = {
            factory_id: AnimatronicNamePartFactory(self.data.find(block_id=block_id))
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
        return super().__call__(*args, **values)


class AnimatronicNameFactory(GenderNameBlockFactory):
    """Animatronic Name Factory."""

    class MaleNameFactory(BaseAnimatronicNameFactory):
        """Method #1."""

        block_map = {
            'nm1': 1,
        }

    class FemaleNameFactory(BaseAnimatronicNameFactory):
        """Method #1."""

        block_map = {
            'nm1': 2,
        }

    default_data = DB
