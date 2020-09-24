from generated import materials
from .matter import MoleculeFactory
from ..factory import Factory


class WaterFactory(Factory):
    default_model = materials.Water

    def children(self):
        yield MoleculeFactory.from_elements('H', 'O')


class WaterStateFactory(Factory):
    def children(self):
        yield WaterFactory()


class DewFactory(WaterStateFactory):
    default_model = materials.Dew


class IceFactory(WaterStateFactory):
    default_model = materials.Ice


class SnowflakesFactory(WaterStateFactory):
    default_model = materials.Snowflakes


class SnowFactory(Factory):
    default_model = materials.Snow

    def children(self):
        yield SnowflakesFactory()
