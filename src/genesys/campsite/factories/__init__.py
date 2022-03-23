from factories.factory import Factory
from .campsite import BaseCampsiteFactory
from ..providers import CampsiteDataProvider


class CampsiteFactory(Factory):
    def __init__(self, data=CampsiteDataProvider):
        self.__data = data
        self.simple_campsite_factory = BaseCampsiteFactory(data.simple)
        self.unusual_campsite_factory = BaseCampsiteFactory(data.unusual)

    @property
    def data(self):
        return self.__data

    def factory(self, roll):
        if roll < self.data.unusual_roll:
            return self.simple_campsite_factory
        else:
            return self.unusual_campsite_factory

    def __call__(self, roll=None, *args, **kwargs):
        factory = self.factory(roll or self.data.roll())
        return factory(*args, **kwargs)
