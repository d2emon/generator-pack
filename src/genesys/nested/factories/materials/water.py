from generated.materials import Water, Dew, Ice, Snowflakes, Snow
from .matter import MoleculeFactory
from ..factory import Factory


class WaterFactory(Factory):
    default_model = Water

    def children(self):
        yield MoleculeFactory.from_elements('H', 'O')


class WaterStateFactory(Factory):
    def children(self):
        yield WaterFactory()


class DewFactory(WaterStateFactory):
    default_model = Dew


class IceFactory(WaterStateFactory):
    default_model = Ice


class SnowflakesFactory(WaterStateFactory):
    default_model = Snowflakes


class SnowFactory(Factory):
    default_model = Snow

    def children(self):
        yield SnowflakesFactory()
