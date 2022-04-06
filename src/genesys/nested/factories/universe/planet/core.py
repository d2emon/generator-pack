from models.universe.planet.core import PlanetCore
from factories.nested_factory import NestedFactory as Factory
from ...life import PlanetCoreLifeFactory
from ...materials import RockFactory, IronFactory, DiamondFactory, MagmaFactory


class PlanetCoreFactory(Factory):
    default_model = PlanetCore

    def life(self):
        yield PlanetCoreLifeFactory()

    def minerals(self):
        yield IronFactory()
        yield RockFactory()
        yield DiamondFactory().probable(2)
        yield MagmaFactory()

    def children(self):
        yield from self.life()
        yield from self.minerals()
