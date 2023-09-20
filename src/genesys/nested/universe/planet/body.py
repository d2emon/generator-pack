from factories.thing.nested_factory import NestedFactory
from models import planet
from utils.nested import select_item
from ...materials import IceFactory, RockFactory
from ..data_provider import PROVIDER
from ..unsorted_life import GhostFactory, SpaceAnimalFactory
from ..unsorted_terrain import ContinentFactory, OceanFactory, SkyFactory
from .core import PlanetCoreFactory


class PlanetLikeFactory(NestedFactory):
    model = planet.body.PlanetLike

    def life(self):
        yield None

    def atmosphere(self):
        yield None

    def continents(self):
        yield None

    def core(self):
        yield None

    def moons(self):
        yield None

    def oceans(self):
        yield None

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
    default_model = planet.body.Asteroid

    def life(self):
        yield SpaceAnimalFactory.probable(0.5)

    def continents(self):
        yield RockFactory.one()

    def oceans(self):
        yield IceFactory.probable(30)


class MoonFactory(PlanetLikeFactory):
    default_data = PROVIDER
    model = planet.body.Moon

    def life(self):
        yield GhostFactory.probable(0.1)

    def continents(self):
        # yield MoonPlateFactory()
        yield RockFactory.one()

    def core(self):
        yield PlanetCoreFactory.one()

    def name_factory(self, data, *args, **kwargs):
        return f"{select_item(*data.moon)} moon"


class PlanetFactory(PlanetLikeFactory):
    # .planet composition
    default_name = 'planet'
    model = planet.Planet

    def core(self):
        yield PlanetCoreFactory.one()

    def moons(self):
        yield MoonFactory.probable(40)
        yield MoonFactory.probable(20)
        yield MoonFactory.probable(10)


class TerraformedMoonFactory(MoonFactory):
    default_data = PROVIDER
    model = planet.body.TerraformedMoon

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
