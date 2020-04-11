from genesys.nested.models.models.unknown import VisitorCity, VisitorInstallation, Continent, FutureContinent, \
    MedievalContinent, AncientContinent, FutureMoon
from genesys.nested.models.mixins import TerraformedMixin
from .planet_like import PlanetLike
# from .moon import Moon, TerraformedMoon
# from ...chemistry import Rock, Ice
# from ...terrain import Ocean, Sky, TerraformedSky, FutureSky
# from ...biology import GalacticLife


class Planet(PlanetLike):
    # moons = PlanetLike.children_property(Moon)

    class Factory(PlanetLike.Factory):
        def moons(self):
            # yield Moon.probable(40)
            # yield Moon.probable(20)
            # yield Moon.probable(10)
            yield None

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

        def children(self):
            # yield Rock
            # yield Ice
            yield from super().children()


# class VisitorPlanet(BarrenPlanet):
#     class ChildrenFactory(BarrenPlanet.ChildrenFactory):
#         life_probability = 100
#
#         def children_classes(self):
#             yield from VisitorCity.multiple(1, 8)
#             yield from VisitorInstallation.multiple(2, 6)
#             yield BarrenPlanet.ChildrenFactory.children_classes(self)


# class TelluricPlanet(Planet, TerraformedMixin):
#     class ChildrenFactory(Planet.ChildrenFactory):
#         @classmethod
#         def _continents(cls):
#             yield from Continent.multiple(2, 7)
#
#         @classmethod
#         def _oceans(cls):
#             yield from Ocean.multiple(1, 7)
#
#         @classmethod
#         def _sky(cls):
#             yield Sky
#
#         @classmethod
#         def _moons(cls):
#             yield None

#         def children_classes(self):
#             yield from self._continents()
#             yield from self._oceans()
#             yield from self._sky()
#             yield from self._moons()
#             yield Planet.ChildrenFactory.children_classes(self)


# class FuturePlanet(TelluricPlanet):
#     class ChildrenFactory(TelluricPlanet.ChildrenFactory):
#         @classmethod
#         def _continents(cls):
#             yield from FutureContinent.multiple(2, 7)
#
#         @classmethod
#         def _sky(cls):
#             yield FutureSky
#
#         @classmethod
#         def _moons(cls):
#             yield FutureMoon.probable(30)


# class TerraformedPlanet(TelluricPlanet):
#     class ChildrenFactory(TelluricPlanet.ChildrenFactory):
#         @classmethod
#         def _sky(cls):
#             yield TerraformedSky
#
#         @classmethod
#         def _moons(cls):
#             yield TerraformedMoon.probable(30)


# class MedievalPlanet(TelluricPlanet):
#     class ChildrenFactory(TelluricPlanet.ChildrenFactory):
#         @classmethod
#         def _continents(cls):
#             yield from MedievalContinent.multiple(2, 4)
#             yield from AncientContinent.multiple(0, 3)


# class AncientPlanet(TelluricPlanet):
#     class ChildrenFactory(TelluricPlanet.ChildrenFactory):
#         @classmethod
#         def _continents(cls):
#             yield from AncientContinent.multiple(2, 7)
