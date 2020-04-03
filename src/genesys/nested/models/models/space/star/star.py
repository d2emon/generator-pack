from genesys.nested.models.models.unknown import Ghost, SpaceMonster, DysonSurface
from genesys.nested.models import Model
from genesys.nested.models.mixins import EncounteredMixin
from genesys.nested.data import lookups
from genesys.nested.models.models.chemistry import elements, Atom
from ..planet import Planet, BarrenPlanet, VisitorPlanet, FuturePlanet, TerraformedPlanet, MedievalPlanet, \
    AncientPlanet, AsteroidBelt, GasGiant


class Star(Model, EncounteredMixin):
    contents = Model.children_property(Atom)

    class BaseFactory(Model.BaseFactory):
        default = lookups.stars

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Ghost.probable(0.1)
            yield SpaceMonster.probable(0.2)
            yield elements['H']
            yield elements['He']


class StarSystem(Model):
    star = Model.child_property(Star)
    stars = Model.children_property(Star)
    planets = Model.children_property(Planet)
    asteroid_belts = Model.children_property(AsteroidBelt)
    dyson_surfaces = Model.children_property(DysonSurface)
    orbits = Model.children_property(Planet, AsteroidBelt, DysonSurface)

    class ChildrenFactory(Model.ChildrenFactory):
        @classmethod
        def _generate_inhabited(cls):
            yield VisitorPlanet.probable(5)
            yield FuturePlanet.probable(10)
            yield TerraformedPlanet.probable(50)
            yield TerraformedPlanet.probable(20)
            yield TerraformedPlanet.probable(10)
            yield MedievalPlanet.probable(30)
            yield MedievalPlanet.probable(20)
            yield AncientPlanet.probable(50)
            yield AncientPlanet.probable(30)
            yield AncientPlanet.probable(10)

        def children_classes(self):
            yield Star
            yield Star.probable(3)
            yield from self._generate_inhabited()
            yield BarrenPlanet.probable(60)
            yield BarrenPlanet.probable(40)
            yield BarrenPlanet.probable(20)
            yield GasGiant.probable(60)
            yield GasGiant.probable(40)
            yield GasGiant.probable(20)
            yield GasGiant.probable(10)
            yield from AsteroidBelt.multiple(0, 2)


class SingleStar(StarSystem):
    class ChildrenFactory(StarSystem.ChildrenFactory):
        def children_classes(self):
            yield Star
