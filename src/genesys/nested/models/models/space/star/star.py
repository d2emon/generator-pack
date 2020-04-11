from genesys.nested.models.models.unknown import Ghost, DysonSurface
from genesys.nested.models import Model
from genesys.nested.models.mixins import EncounteredMixin
from ..planet import Planet, BarrenPlanet
# from ..planet import Planet, BarrenPlanet, VisitorPlanet, FuturePlanet, TerraformedPlanet, MedievalPlanet, \
#     AncientPlanet, AsteroidBelt, GasGiant
# from ...biology import SpaceMonster
from ...chemistry import elements, Atom
from genesys.nested.data import lookups


class Star(Model, EncounteredMixin):
    contents = Model.children_property(Atom)

    class Factory(Model.Factory):
        class DataProvider:
            star = lookups.stars

        name = property(lambda self: self.provider.star)

        def children(self):
            # yield Ghost.probable(0.1)
            # yield SpaceMonster.probable(0.2)
            yield elements['H']
            yield elements['He']


class StarSystem(Model):
    main_star = Model.child_property(Star)
    stars = Model.children_property(Star)
    planets = Model.children_property(Planet)
    # asteroid_belts = Model.children_property(AsteroidBelt)
    # dyson_surfaces = Model.children_property(DysonSurface)
    # orbits = Model.children_property(Planet, AsteroidBelt, DysonSurface)

    class Factory(Model.Factory):
        @classmethod
        def _generate_inhabited(cls):
            # yield VisitorPlanet.probable(5)
            # yield FuturePlanet.probable(10)
            # yield TerraformedPlanet.probable(50)
            # yield TerraformedPlanet.probable(20)
            # yield TerraformedPlanet.probable(10)
            # yield MedievalPlanet.probable(30)
            # yield MedievalPlanet.probable(20)
            # yield AncientPlanet.probable(50)
            # yield AncientPlanet.probable(30)
            # yield AncientPlanet.probable(10)
            yield None

        def children(self):
            yield Star
            yield Star.probable(3)
            yield from self._generate_inhabited()
            yield BarrenPlanet.probable(60)
            yield BarrenPlanet.probable(40)
            yield BarrenPlanet.probable(20)
            # yield GasGiant.probable(60)
            # yield GasGiant.probable(40)
            # yield GasGiant.probable(20)
            # yield GasGiant.probable(10)
            # yield from AsteroidBelt.multiple(0, 2)


class SingleStar(StarSystem):
    class Factory(Model.Factory):
        def children(self):
            yield Star
