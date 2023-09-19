from factories.thing.nested_factory import NestedFactory as Factory
from models.v5 import materials
from .elements import MoleculeFactory


class WaterMoleculeFactory(MoleculeFactory):
    contents = 'H', 'O'


class WaterFactory(Factory):
    model = materials.Water

    def children(self):
        yield WaterMoleculeFactory.one()


class SteamFactory(WaterFactory):
    # TODO: Refactor it
    default_model = materials.Steam


class DewFactory(WaterFactory):
    model = materials.Dew


class IceFactory(WaterFactory):
    model = materials.Ice


class SnowflakesFactory(WaterFactory):
    model = materials.Snowflakes


class SnowFactory(Factory):
    model = materials.Snow

    def children(self):
        yield SnowflakesFactory.one()
