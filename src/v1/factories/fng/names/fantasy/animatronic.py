import random
from v1.fixtures import genders
from v1.fixtures.data_block import fill_data
from v1.fixtures.fng.names import fantasy
from v1.models.fng.names.fantasy import AnimatronicName
from v1.factories.fng.name_factory import NameFactory, GenderFactory


class AnimatronicNamePartFactory(NameFactory):
    def generate(self, *args, **kwargs):
        items = list(self.find(*args, **kwargs))
        if len(items) == 0:
            return {}

        return random.choice(items)


class AnimatronicNameFactory(GenderFactory):
    """Animatronic Name Factory

    There's a large variety of names in this generator. Some are normal, friendly names you'd expect for normal
    animatronics, other names are more creepy for the horror kinds of animatronics, like those in the Five Nights at
    Freddy's games.
    With thousands of different names, there's plenty to pick from for all sorts of genres and purposes."""

    class MaleNameFactory(NameFactory):
        model = AnimatronicName
        block_map = {
            'nm1': 1,
        }

        def __init__(self, data=None):
            """
            :param data: Data blocks for factory
            """
            super().__init__(data)
            self.factories = {
                factory_id: AnimatronicNamePartFactory(self.find(block_id=block_id))
                for factory_id, block_id in self.block_map.items()
            }

        def validate(self, items) -> dict:
            item = items['nm1'].items.get('value', [[], []])
            return {
                'nm0': random.choice(item[0]),
                'nm1': random.choice(item[1]),
            }

    class FemaleNameFactory(NameFactory):
        model = AnimatronicName
        block_map = {
            'nm1': 2,
        }

        def validate(self, items) -> dict:
            item = str(items['nm1'])
            return {
                'nm0': random.choice(item[0]),
                'nm1': random.choice(item[1]),
            }

    factory_classes = {
        genders.MALE: MaleNameFactory,
        genders.FEMALE: FemaleNameFactory,
    }
    default_data = fill_data(group_id='animatronic')({
        1: fantasy.animatronic.nm1,
        2: fantasy.animatronic.nm2,
    })
