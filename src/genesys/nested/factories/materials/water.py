from generated import materials
from .matter import MoleculeFactory
from factories.nested_factory import NestedFactory as Factory


class WaterMoleculeFactory(MoleculeFactory):
    def children(self):
        yield from self.elements('H', 'O')


class WaterFactory(Factory):
    def children(self):
        yield WaterMoleculeFactory()


class SteamFactory(WaterFactory):
    default_model = materials.Steam


class DewFactory(WaterFactory):
    default_model = materials.Dew


class IceFactory(WaterFactory):
    default_model = materials.Ice


class SnowflakesFactory(WaterFactory):
    default_model = materials.Snowflakes


class SnowFactory(Factory):
    default_model = materials.Snow

    def children(self):
        yield SnowflakesFactory()
