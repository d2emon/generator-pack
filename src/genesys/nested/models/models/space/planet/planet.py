from genesys.nested.models.models.unknown import VisitorCity, VisitorInstallation, Continent, FutureContinent, \
    MedievalContinent, AncientContinent, FutureMoon
from genesys.nested.models.mixins import TerraformedMixin
from .atmosphere import Atmosphere
from .moon import Moon, TerraformedMoon
from .planet_like import PlanetLike
# from ...biology import GalacticLife
# from ...terrain import Ocean, Sky, TerraformedSky, FutureSky


class Planet(PlanetLike):
    moons = PlanetLike.children_property(Moon)

    class Factory(PlanetLike.Factory):
        def moons(self):
            yield Moon.probable(40)
            yield Moon.probable(20)
            yield Moon.probable(10)

        def children(self):
            yield from super().children()
            yield from self.moons()


class BarrenPlanet(Planet):
    default_name = 'telluric planet'

    class Factory(Planet.Factory):
        life_probability = 10

        def biosphere(self):
            # yield GalacticLife.probable(self.life_probability)
            yield None


class VisitorPlanet(BarrenPlanet):
    class Factory(Planet.Factory):
        life_probability = 100

        def visited(self):
            yield from VisitorCity.multiple(1, 8)
            yield from VisitorInstallation.multiple(2, 6)


class TelluricPlanet(Planet, TerraformedMixin):
    class Factory(Planet.Factory):
        def atmosphere(self):
            yield Atmosphere

        def continents(self):
            yield from Continent.multiple(2, 7)

        def oceans(self):
            # yield from Ocean.multiple(1, 7)
            yield None

        def plates(self):
            yield from self.continents()
            yield from self.oceans()

        def sky(self):
            # yield Sky
            yield None


class FuturePlanet(TelluricPlanet):
    class Factory(TelluricPlanet.Factory):
        def continents(self):
            yield from FutureContinent.multiple(2, 7)

        def sky(self):
            # yield FutureSky
            yield None

        def moons(self):
            yield from super().moons()
            yield FutureMoon.probable(30)


class TerraformedPlanet(TelluricPlanet):
    class Factory(TelluricPlanet.Factory):
        def sky(self):
            # yield TerraformedSky
            yield None

        def moons(self):
            yield from super().moons()
            yield TerraformedMoon.probable(30)


class MedievalPlanet(TelluricPlanet):
    class Factory(TelluricPlanet.Factory):
        def continents(self):
            yield from MedievalContinent.multiple(2, 4)
            yield from AncientContinent.multiple(0, 3)


class AncientPlanet(TelluricPlanet):
    class Factory(TelluricPlanet.Factory):
        def continents(self):
            yield from AncientContinent.multiple(2, 7)
