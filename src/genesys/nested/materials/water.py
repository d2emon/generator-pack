from genesys.nested.factories.nested_factory import NestedFactory
from models.materials import water
from .molecules import MoleculeFactory


class WaterMoleculeFactory(MoleculeFactory):
    contents = 'H', 'O'


class WaterFactory(NestedFactory):
    model = water.Water

    def children(self):
        yield WaterMoleculeFactory.one()


class DewFactory(WaterFactory):
    model = water.Dew


class IceFactory(WaterFactory):
    model = water.Ice


class SnowflakesFactory(WaterFactory):
    model = water.Snowflakes


class SnowFactory(NestedFactory):
    model = water.Snow

    def children(self):
        yield SnowflakesFactory.one()


class SteamFactory(WaterFactory):
    model = water.Steam
