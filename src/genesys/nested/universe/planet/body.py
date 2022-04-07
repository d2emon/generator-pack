from models.universe.planet import PlanetLike
from models.universe.planet.body import Asteroid, Moon, TerraformedMoon
from factories.nested_factory import NestedFactory as Factory
from ...temporary import ContinentFactory
from ...life import AsteroidLifeFactory, MoonLifeFactory
from ...terrain import OceanFactory, SkyFactory
from .plate import AsteroidPlateFactory, MoonPlateFactory, PlateFactory
from .core import PlanetCoreFactory


class PlanetLikeFactory(Factory):
    default_model = PlanetLike

    def atmosphere(self):
        yield None

    def biosphere(self):
        yield None

    def core(self):
        yield PlanetCoreFactory()

    def plates(self):
        yield from PlateFactory().multiple(2, 7)
        yield from PlateFactory().multiple(1, 7)

    def sky(self):
        yield None

    def visited(self):
        yield None

    def children(self):
        yield from self.core()
        yield from self.atmosphere()
        yield from self.biosphere()
        yield from self.plates()
        yield from self.sky()
        yield from self.visited()


class AsteroidFactory(PlanetLikeFactory):
    default_model = Asteroid

    def biosphere(self):
        yield AsteroidLifeFactory()

    def plates(self):
        yield AsteroidPlateFactory()


class MoonFactory(PlanetLikeFactory):
    default_model = Moon
    names = ["young", "old", "large", "small", "pale", "white", "dark", "black", "old"]

    def generate_name(self):
        return f"{self.select_item(*self.names)} moon"

    def biosphere(self):
        yield MoonLifeFactory()

    def plates(self):
        yield MoonPlateFactory()


class TerraformedMoonFactory(MoonFactory):
    default_model = TerraformedMoon
    names = [
        "young", "old", "large", "small", "pale", "white", "dark", "black", "old", "green", "lush", "blue", "city",
        "colonized", "life",
    ]

    def biosphere(self):
        yield None

    def plates(self):
        yield from ContinentFactory().multiple(1, 4)
        yield from OceanFactory().multiple(1, 4)

    def sky(self):
        yield SkyFactory()
