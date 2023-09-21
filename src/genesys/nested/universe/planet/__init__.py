from models import planet
from ...materials import IceFactory, RockFactory
from .body import FutureMoonFactory, PlanetFactory, TerraformedMoonFactory
from ...unsorted_life import GalacticLifeFactory
from ...unsorted_terrain import ContinentFactory, AncientContinentFactory, MedievalContinentFactory, FutureContinentFactory, \
    OceanFactory, SkyFactory, TerraformedSkyFactory, FutureSkyFactory
from ...unsorted_visitor import VisitorCityFactory, VisitorInstallationFactory


class TelluricPlanetFactory(PlanetFactory):
    model = planet.TelluricPlanet

    def life(self):
        yield None

    def atmosphere(self):
        # yield AtmosphereFactory()
        yield None

    def continents(self):
        yield ContinentFactory.multiple(2, 7)

    def oceans(self):
        yield OceanFactory.multiple(1, 7)

    def sky(self):
        yield SkyFactory.one()

    def visited(self):
        yield None


class BarrenPlanetFactory(TelluricPlanetFactory):
    model = planet.BarrenPlanet

    def life(self):
        yield GalacticLifeFactory.probable(10)

    def atmosphere(self):
        yield None

    def continents(self):
        yield RockFactory.one()

    def oceans(self):
        yield IceFactory.probable(50)

    def sky(self):
        yield None


class VisitorPlanetFactory(BarrenPlanetFactory):
    model = planet.BarrenPlanet

    def life(self):
        yield GalacticLifeFactory.one()

    def visited(self):
        yield VisitorCityFactory.multiple(1, 8)
        yield VisitorInstallationFactory.multiple(2, 6)


class FuturePlanetFactory(TelluricPlanetFactory):
    def continents(self):
        yield FutureContinentFactory.multiple(2, 7)

    def oceans(self):
        yield OceanFactory.multiple(1, 7)

    def sky(self):
        yield FutureSkyFactory.one()

    def moons(self):
        yield from super().moons()
        yield FutureMoonFactory.probable(30)


class TerraformedPlanetFactory(TelluricPlanetFactory):
    def continents(self):
        yield ContinentFactory.multiple(2, 7)

    def oceans(self):
        yield OceanFactory.multiple(1, 7)

    def sky(self):
        yield TerraformedSkyFactory.one()

    def moons(self):
        yield from super().moons()
        yield TerraformedMoonFactory.probable(30)


class MedievalPlanetFactory(TelluricPlanetFactory):
    def continents(self):
        yield MedievalContinentFactory.multiple(2, 4)
        yield AncientContinentFactory.multiple(0, 3)

    def oceans(self):
        yield OceanFactory.multiple(1, 7)

    def sky(self):
        yield TerraformedSkyFactory.one()


class AncientPlanetFactory(TelluricPlanetFactory):
    def continents(self):
        yield AncientContinentFactory.multiple(2, 7)

    def oceans(self):
        yield OceanFactory.multiple(1, 7)

    def sky(self):
        yield TerraformedSkyFactory.one()


class DefaultPlanetFactory(TerraformedPlanetFactory):
    pass
