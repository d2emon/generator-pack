from genesys.nested.factories.nested_factory import NestedFactory
from models.planet import body
from utils.nested import select_item
from .core import PlanetCoreFactory
from .plate import IcePlateFactory, RockPlateFactory

from ...unsorted_life import GhostFactory, SpaceAnimalFactory
from ...unsorted_terrain import ContinentFactory, OceanFactory, SkyFactory


class PlanetLikeFactory(NestedFactory):
    model = body.PlanetLike

    def life(self):
        yield None

    def atmosphere(self):
        yield None

    def continents(self):
        yield RockPlateFactory.one()

    def core(self):
        yield PlanetCoreFactory.one()

    def moons(self):
        yield None

    def oceans(self):
        yield IcePlateFactory.probable(30)

    def plates(self):
        yield from self.continents()
        yield from self.oceans()

    def sky(self):
        yield None

    def visited(self):
        yield None

    def children(self):
        yield from self.atmosphere()
        yield from self.core()
        yield from self.moons()
        yield from self.plates()
        yield from self.sky()
        yield from self.visited()
        yield from self.life()


class AsteroidFactory(PlanetLikeFactory):
    model = body.Asteroid

    def core(self):
        yield None

    def life(self):
        yield SpaceAnimalFactory.probable(0.5)


class MoonFactory(PlanetLikeFactory):
    model = body.Moon

    def life(self):
        yield GhostFactory.probable(0.1)

    def oceans(self):
        yield None

    def name_factory(self, data, *args, **kwargs):
        return f"{select_item(*data.moon)} moon"


class TerraformedMoonFactory(MoonFactory):
    model = body.TerraformedMoon

    def continents(self):
        yield ContinentFactory.multiple(1, 4)

    def oceans(self):
        yield OceanFactory.multiple(1, 4)

    def sky(self):
        yield SkyFactory.one()

    def name_factory(self, data, *args, **kwargs):
        return f"{select_item(*data.terraformed_moon)} moon"


class FutureMoonFactory(TerraformedMoonFactory):
    pass
