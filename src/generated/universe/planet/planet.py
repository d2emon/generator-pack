from generated.nested_v2.models import VisitorCity, VisitorInstallation, Continent, FutureContinent, \
    MedievalContinent, AncientContinent, FutureMoon
from genesys.model.mixins import TerraformedMixin
from .atmosphere import Atmosphere
from .moon import Moon, TerraformedMoon
from .planet_like import PlanetLike
from generated.universe.space.life import BarrenPlanetLife, VisitorPlanetLife
from generated.nested_v2.models.terrain import Ocean
# from ...terrain import Ocean, Sky, TerraformedSky, FutureSky


class Planet(PlanetLike):
    moons = PlanetLike.children_property(Moon)

    class Factory(PlanetLike.Factory):
        @classmethod
        def moons(cls):
            yield Moon.probable(40)
            yield Moon.probable(20)
            yield Moon.probable(10)

        def children(self):
            yield from super().children()
            yield from self.moons()


class BarrenPlanet(Planet):
    default_name = 'telluric planet'

    class Factory(Planet.Factory):
        @classmethod
        def biosphere(cls):
            yield BarrenPlanetLife


class VisitorPlanet(BarrenPlanet):
    class Factory(Planet.Factory):
        @classmethod
        def biosphere(cls):
            yield VisitorPlanetLife

        @classmethod
        def visited(cls):
            yield from VisitorCity.multiple(1, 8)
            yield from VisitorInstallation.multiple(2, 6)


class TelluricPlanet(Planet, TerraformedMixin):
    class Factory(Planet.Factory):
        @classmethod
        def atmosphere(cls):
            yield Atmosphere

        @classmethod
        def continents(cls):
            yield from Continent.multiple(2, 7)

        @classmethod
        def oceans(cls):
            yield from Ocean.multiple(1, 7)

        @classmethod
        def plates(cls):
            yield from cls.continents()
            yield from cls.oceans()

        @classmethod
        def sky(cls):
            # yield Sky
            yield None


class FuturePlanet(TelluricPlanet):
    class Factory(TelluricPlanet.Factory):
        @classmethod
        def continents(cls):
            yield from FutureContinent.multiple(2, 7)

        @classmethod
        def sky(cls):
            # yield FutureSky
            yield None

        @classmethod
        def moons(cls):
            yield from super().moons()
            yield FutureMoon.probable(30)


class TerraformedPlanet(TelluricPlanet):
    class Factory(TelluricPlanet.Factory):
        @classmethod
        def sky(cls):
            # yield TerraformedSky
            yield None

        @classmethod
        def moons(cls):
            yield from super().moons()
            yield TerraformedMoon.probable(30)


class MedievalPlanet(TelluricPlanet):
    class Factory(TelluricPlanet.Factory):
        @classmethod
        def continents(cls):
            yield from MedievalContinent.multiple(2, 4)
            yield from AncientContinent.multiple(0, 3)


class AncientPlanet(TelluricPlanet):
    class Factory(TelluricPlanet.Factory):
        @classmethod
        def continents(cls):
            yield from AncientContinent.multiple(2, 7)
