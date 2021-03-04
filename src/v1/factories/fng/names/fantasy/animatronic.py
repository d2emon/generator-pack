import random
from v1.fixtures import genders
from v1.fixtures.data_block import load_data
from v1.fixtures.fng.names import fantasy
from v1.models.fng.names.fantasy import AnimatronicName
from v1.factories.fng.name_factory import NameFactory, GenderNameFactory


class AnimatronicNameFactory(GenderNameFactory):
    """Animatronic Name Factory

    There's a large variety of names in this generator. Some are normal, friendly names you'd expect for normal
    animatronics, other names are more creepy for the horror kinds of animatronics, like those in the Five Nights at
    Freddy's games.
    With thousands of different names, there's plenty to pick from for all sorts of genres and purposes."""

    class MaleNameFactory(NameFactory):
        name_class = AnimatronicName
        blocks_map = {
            1: 1,
        }

        def validate(self, items) -> dict:
            item = str(items[1])
            return {
                0: random.choice(item[0]),
                1: random.choice(item[1]),
            }

    class FemaleNameFactory(NameFactory):
        name_class = AnimatronicName
        blocks_map = {
            1: 2,
        }

        def validate(self, items) -> dict:
            item = str(items[1])
            return {
                0: random.choice(item[0]),
                1: random.choice(item[1]),
            }

    factory_classes = {
        genders.MALE: MaleNameFactory,
        genders.FEMALE: FemaleNameFactory,
    }
    default_blocks = load_data({
        1: fantasy.animatronic.nm1,
        2: fantasy.animatronic.nm2,
    })
