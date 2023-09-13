from factories.thing.nested_factory import NestedFactory
from models.planet.body import PlanetLike, Asteroid, Moon, TerraformedMoon
from utils.nested import select_item
# from .body import Asteroid, Moon, TerraformedMoon
# from ...temporary import ContinentFactory
# from ...life import AsteroidLifeFactory, MoonLifeFactory
# from ...terrain import OceanFactory, SkyFactory
# from .plate import AsteroidPlateFactory, MoonPlateFactory, PlateFactory
from .core import PlanetCoreFactory


# Moon
# TerraformedMoon


class PlanetLikeFactory(NestedFactory):
    default_model = PlanetLike

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

    def contents(self):
        yield from self.atmosphere()
        yield from self.core()
        yield from self.moons()
        yield from self.plates()
        yield from self.sky()
        yield from self.visited()


class MoonFactory(PlanetLikeFactory):
    default_model = Moon
    names = ["young", "old", "large", "small", "pale", "white", "dark", "black", "old"]

    def life(self):
        # yield MoonLifeFactory()
        # ghost,0.1%
        yield None

    def continents(self):
        # yield MoonPlateFactory()
        # rock
        yield None

    def oceans(self):
        yield None

    def core(self):
        yield PlanetCoreFactory

    def name_factory(self):
        return f"{select_item(*self.names)} moon"


class TerraformedMoonFactory(MoonFactory):
    default_model = TerraformedMoon
    names = [
        "young", "old", "large", "small", "pale", "white", "dark", "black", "old", "green", "lush", "blue", "city",
        "colonized", "life",
    ]

    def life(self):
        yield None

    def core(self):
        # yield from PlanetCompositionFactory.planet_composition()
        yield None

    def continents(self):
        # yield from ContinentFactory().multiple(1, 4)
        # continent,1-4
        yield None

    def oceans(self):
        # yield from OceanFactory().multiple(1, 4)
        # ocean,1-4
        yield None

    def sky(self):
        # yield SkyFactory()
        # sky
        yield None

    def name_factory(self):
        return f"{select_item(*self.names)} moon"


class FutureMoonFactory(TerraformedMoonFactory):
    pass


"""
new Thing("moon",[
    "ghost,0.1%",
    "rock",
    "planet core"
],[["young","old","large","small","pale","white","dark","black","old"],[" moon"]]);
new Thing("terraformed moon",[
    ".planet composition",
    "continent,1-4",
    "ocean,1-4",
    "sky"
],[["young","old","large","small","pale","white","dark","black","old","green","lush","blue","city","colonized","life"],[" moon"]]);
"""
