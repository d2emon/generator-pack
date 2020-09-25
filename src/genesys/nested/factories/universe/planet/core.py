from generated import universe
from ...factory import Factory
from ...materials import RockFactory, IronFactory, DiamondFactory, MagmaFactory


class PlanetCoreFactory(Factory):
    default_model = universe.PlanetCore

    def life(self):
        # "space monster,0.5%"
        # yield PlanetCoreLife
        yield None

    def minerals(self):
        yield IronFactory()
        yield RockFactory()
        yield DiamondFactory().probable(2)
        yield MagmaFactory()

    def children(self):
        yield from self.life()
        yield from self.minerals()
