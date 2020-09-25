from generated import universe
from ...factory import Factory
from .plate import AsteroidPlateFactory, MoonPlateFactory
from .core import PlanetCoreFactory


class PlanetLikeFactory(Factory):
    default_model = universe.PlanetLike

    def atmosphere(self):
        yield None

    def biosphere(self):
        yield None

    def core(self):
        yield PlanetCoreFactory()

    def plates(self):
        # yield from Plate.multiple(2, 7)
        # yield from Plate.multiple(1, 7)
        yield None

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
    default_model = universe.Asteroid

    def biosphere(self):
        # "space animal,0.5%"
        # yield AsteroidLife
        yield None

    def plates(self):
        yield AsteroidPlateFactory()


class MoonFactory(PlanetLikeFactory):
    default_model = universe.Moon

    # class DataProvider:
    #     moon = lookups.moons

    # name = property(lambda self: self.provider.moon)

    # ["young","old","large","small","pale","white","dark","black","old"],
    # [" moon"]

    def biosphere(self):
        # "ghost,0.1%"
        # yield MoonLife
        yield None

    def plates(self):
        yield MoonPlateFactory()


class TerraformedMoonFactory(MoonFactory):
    default_model = universe.TerraformedMoon

    # class DataProvider:
    #     terraformed_moon = lookups.terraformed_moons

    # name = property(lambda self: self.provider.terraformed_moon)

    # ["young", "old", "large", "small", "pale", "white", "dark", "black", "old", "green", "lush", "blue", "city",
    # "colonized", "life"],
    #
    # [" moon"]

    def biosphere(self):
        yield None

    def plates(self):
        # yield from Continent.multiple(1, 4)
        # yield from Ocean.multiple(1, 4)
        yield None

    def sky(self):
        # yield Sky
        yield None

    def children(self):
        # ".planet composition"
        yield from super().children()
