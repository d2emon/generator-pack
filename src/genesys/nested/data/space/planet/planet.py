from ... import unknown
from genesys.nested.models.mixins import TerraformedMixin
from .planet_like import PlanetLike
from .moon import Moon, TerraformedMoon
from ...chemistry import Rock, Ice
from genesys.nested.data.unprocessed.future.planet import FutureMoon


class Planet(PlanetLike):
    moons = PlanetLike.children_property(Moon)

    class ChildrenFactory(PlanetLike.ChildrenFactory):
        def children_classes(self):
            yield from PlanetLike.ChildrenFactory.children_classes(self)
            yield Moon.probable(40)
            yield Moon.probable(20)
            yield Moon.probable(10)


class BarrenPlanet(Planet):
    class NameFactory(Planet.NameFactory):
        default = 'telluric planet'

    class ChildrenFactory(Planet.ChildrenFactory):
        life_probability = 10

        def children_classes(self):
            yield unknown.GalacticLife.probable(self.life_probability)
            yield Rock
            yield Ice
            yield Planet.ChildrenFactory.children_classes(self)


class VisitorPlanet(BarrenPlanet):
    class ChildrenFactory(BarrenPlanet.ChildrenFactory):
        life_probability = 100

        def children_classes(self):
            yield from unknown.VisitorCity.multiple(1, 8)
            yield from unknown.VisitorInstallation.multiple(2, 6)
            yield BarrenPlanet.ChildrenFactory.children_classes(self)


class TelluricPlanet(Planet, TerraformedMixin):
    class ChildrenFactory(Planet.ChildrenFactory):
        @classmethod
        def _continents(cls):
            yield from unknown.Continent.multiple(2, 7)

        @classmethod
        def _oceans(cls):
            yield from unknown.Ocean.multiple(1, 7)

        @classmethod
        def _sky(cls):
            yield unknown.Sky

        @classmethod
        def _moons(cls):
            yield None

        def children_classes(self):
            yield from self._continents()
            yield from self._oceans()
            yield from self._sky()
            yield from self._moons()
            yield Planet.ChildrenFactory.children_classes(self)


class FuturePlanet(TelluricPlanet):
    class ChildrenFactory(TelluricPlanet.ChildrenFactory):
        @classmethod
        def _continents(cls):
            yield from unknown.FutureContinent.multiple(2, 7)

        @classmethod
        def _sky(cls):
            yield unknown.FutureSky

        @classmethod
        def _moons(cls):
            yield FutureMoon.probable(30)


class TerraformedPlanet(TelluricPlanet):
    class ChildrenFactory(TelluricPlanet.ChildrenFactory):
        @classmethod
        def _sky(cls):
            yield unknown.TerraformedSky

        @classmethod
        def _moons(cls):
            yield TerraformedMoon.probable(30)


class MedievalPlanet(TelluricPlanet):
    class ChildrenFactory(TelluricPlanet.ChildrenFactory):
        @classmethod
        def _continents(cls):
            yield from unknown.MedievalContinent.multiple(2, 4)
            yield from unknown.AncientContinent.multiple(0, 3)


class AncientPlanet(TelluricPlanet):
    class ChildrenFactory(TelluricPlanet.ChildrenFactory):
        @classmethod
        def _continents(cls):
            yield from unknown.AncientContinent.multiple(2, 7)
