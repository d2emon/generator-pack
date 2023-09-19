from factories.thing.nested_factory import NestedFactory
from models.v5 import materials
from .molecules import MoleculeFactory


class WaterMoleculeFactory(MoleculeFactory):
    contents = 'H', 'O'


class WaterFactory(NestedFactory):
    model = materials.Water

    def children(self):
        yield WaterMoleculeFactory.one()


class DewFactory(WaterFactory):
    model = materials.Dew


class IceFactory(WaterFactory):
    model = materials.Ice


class SnowflakesFactory(WaterFactory):
    model = materials.Snowflakes


class SnowFactory(NestedFactory):
    model = materials.Snow

    def children(self):
        yield SnowflakesFactory.one()


class SteamFactory(WaterFactory):
    model = materials.Steam
