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
from genesys.fng.factories.name_factory import ComplexFactory
from models.fng.names.fantasy import AnimatronicName


DB = Database('animatronic', {
    1: fantasy.animatronic.nm1,
    2: fantasy.animatronic.nm2,
})


class BaseAnimatronicNameFactory(ComplexFactory):
    """Method #1."""

    model = AnimatronicName

    def build_kwargs(self, *args, **kwargs) -> dict:
        """
        Build data for model.

        Returns:
            dict: Data for model.
        """
        block_id = self.block_map.get('nm1')
        data = self.data.find(block_id)
        value = data(*args, **kwargs)

        if not value:
            return {}

        items = value.value
        return {
            'nm0': random.choice(items[0]) if len(items) > 0 else '',
            'nm1': random.choice(items[1]) if len(items) > 1 else '',
        }

    def __call__(self, *args, **kwargs) -> AnimatronicName:
        """
        Validate data for model.

        :param items dict: Data for model
        :return: Data for model
        :rtype: dict
        """
        items = self.build_kwargs(*args, **kwargs)

        model = self.model(**items)

        return model

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

    model = AnimatronicName
    default_data = DB
