from models.universe.planet import Planet, BarrenPlanet, TelluricPlanet, GasGiant
# from ...temporary import VisitorCityFactory, VisitorInstallationFactory, ContinentFactory, FutureContinentFactory, \
#     MedievalContinentFactory, AncientContinentFactory, FutureMoonFactory
# from ...life import BarrenPlanetLifeFactory, VisitorPlanetLifeFactory
# from ...terrain import OceanFactory, SkyFactory, FutureSkyFactory, TerraformedSkyFactory
from .atmosphere import AtmosphereFactory, GasGiantAtmosphereFactory
from .body import PlanetLikeFactory, MoonFactory, TerraformedMoonFactory
from .core import PlanetCoreFactory
from .plate import PlateFactory


class PlanetFactory(PlanetLikeFactory):
    default_model = Planet
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
    default_model = BarrenPlanet

    def biosphere(self):
        # yield BarrenPlanetLifeFactory()
        yield None

    def plates(self):
        yield PlateFactory()

    @classmethod
    def moons(cls):
        yield None


class VisitorPlanetFactory(BarrenPlanetFactory):
    def biosphere(self):
        # yield VisitorPlanetLifeFactory()
        yield None

    def visited(self):
        # yield from VisitorCityFactory().multiple(1, 8)
        # yield from VisitorInstallationFactory().multiple(2, 6)
        yield None


class TelluricPlanetFactory(PlanetFactory):
    default_model = TelluricPlanet

    def atmosphere(self):
        yield AtmosphereFactory()

    def biosphere(self):
        yield None

    def continents(self):
        # yield from ContinentFactory().multiple(2, 7)
        yield None

    def oceans(self):
        # yield from OceanFactory().multiple(1, 7)
        yield None

    def plates(self):
        yield from self.continents()
        yield from self.oceans()

    def sky(self):
        # yield SkyFactory()
        yield None


class FuturePlanetFactory(TelluricPlanetFactory):
    def continents(self):
        # yield from FutureContinentFactory().multiple(2, 7)
        yield None

    def sky(self):
        # yield FutureSkyFactory()
        yield None

    def moons(self):
        yield from super().moons()
        # yield FutureMoonFactory().probable(30)
        yield None


class TerraformedPlanetFactory(TelluricPlanetFactory):
    def sky(self):
        # yield TerraformedSkyFactory()
        yield None

    def moons(self):
        yield from super().moons()
        yield TerraformedMoonFactory().probable(30)


class DefaultPlanetFactory(TerraformedPlanetFactory):
    pass


class MedievalPlanetFactory(TelluricPlanetFactory):
    def continents(self):
        # yield from MedievalContinentFactory().multiple(2, 4)
        # yield from AncientContinentFactory().multiple(0, 3)
        yield None


class AncientPlanetFactory(TelluricPlanetFactory):
    def continents(self):
        # yield from AncientContinentFactory().multiple(2, 7)
        yield None


class GasGiantFactory(PlanetFactory):
    default_model = GasGiant

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
