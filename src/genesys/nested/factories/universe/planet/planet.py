from generated import universe
from .body import PlanetLikeFactory, MoonFactory, TerraformedMoonFactory
from .core import PlanetCoreFactory
from .plate import PlateFactory
from .atmosphere import AtmosphereFactory, GasGiantAtmosphereFactory


class PlanetFactory(PlanetLikeFactory):
    default_model = universe.Planet
    default_name = 'planet'

    @classmethod
    def moons(cls):
        yield MoonFactory().probable(40)
        yield MoonFactory().probable(20)
        yield MoonFactory().probable(10)

    def children(self):
        yield from super().children()
        yield from self.moons()


class BarrenPlanetFactory(PlanetFactory):
    default_model = universe.BarrenPlanet

    def biosphere(self):
        # "galactic life,10%"
        # yield BarrenPlanetLife
        yield None

    def plates(self):
        yield PlateFactory()

    @classmethod
    def moons(cls):
        yield None


class VisitorPlanetFactory(BarrenPlanetFactory):
    def biosphere(self):
        # "galactic life"
        # yield VisitorPlanetLife
        yield None

    def visited(self):
        # yield from VisitorCity.multiple(1, 8)
        # yield from VisitorInstallation.multiple(2, 6)
        yield None


class TelluricPlanetFactory(PlanetFactory):
    default_model = universe.TelluricPlanet

    def atmosphere(self):
        yield AtmosphereFactory()

    def biosphere(self):
        yield None

    def continents(self):
        # yield from Continent.multiple(2, 7)
        yield None

    def oceans(self):
        # yield from Ocean.multiple(1, 7)
        yield None

    def plates(self):
        yield from self.continents()
        yield from self.oceans()

    def sky(self):
        # yield Sky
        yield None


class FuturePlanetFactory(TelluricPlanetFactory):
    def continents(self):
        # yield from FutureContinent.multiple(2, 7)
        yield None

    def sky(self):
        # yield FutureSky
        yield None

    def moons(self):
        yield from super().moons()
        # yield FutureMoon.probable(30)


class TerraformedPlanetFactory(TelluricPlanetFactory):
    def continents(self):
        # "continent,2-7"
        yield None

    def sky(self):
        # yield TerraformedSky
        yield None

    def moons(self):
        yield from super().moons()
        yield TerraformedMoonFactory().probable(30)


class DefaultPlanetFactory(TerraformedPlanetFactory):
    pass


class MedievalPlanetFactory(TelluricPlanetFactory):
    def continents(self):
        # yield from MedievalContinent.multiple(2, 4)
        # yield from AncientContinent.multiple(0, 3)
        yield None


class AncientPlanetFactory(TelluricPlanetFactory):
    def continents(self):
        # yield from AncientContinent.multiple(2, 7)
        yield None


class GasGiantFactory(PlanetFactory):
    default_model = universe.GasGiant

    def atmosphere(self):
        yield GasGiantAtmosphereFactory()

    def core(self):
        yield PlanetCoreFactory().probable(50)

    def moons(self):
        yield from MoonFactory().multiple(0, 3)
        yield TerraformedMoonFactory().probable(20)
        yield TerraformedMoonFactory().probable(10)

    def plates(self):
        yield None
