import random
from factories import Factory
from .campsite import BaseCampsiteFactory
from .simple import SimpleCampsiteFactory
from .unusual import UnusualCampsiteFactory


class CampsiteFactory(Factory):
    @property
    def data(self):
        return None

    def build(self, roll=None, *args, **kwargs):
        if roll is None:
            roll = random.randrange(12)

        if roll < 11:
            factory = SimpleCampsiteFactory()
        else:
            factory = UnusualCampsiteFactory()

        return factory.build(*args, **kwargs)
