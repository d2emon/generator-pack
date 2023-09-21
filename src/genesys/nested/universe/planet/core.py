from genesys.nested.factories.nested_factory import NestedFactory
from models.planet import core
from ...materials import DiamondFactory, IronFactory, MagmaFactory, RockFactory
from ..unsorted_life import SpaceMonsterFactory


class PlanetCoreFactory(NestedFactory):
    model = core.PlanetCore

    def life(self):
        yield SpaceMonsterFactory.probable(0,5)

    def minerals(self):
        yield IronFactory.one()
        yield RockFactory.one()
        yield DiamondFactory.probable(2)
        yield MagmaFactory.one()

    def children(self):
        yield from self.life()
        yield from self.minerals()
