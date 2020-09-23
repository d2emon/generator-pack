from generated.nested_v2.models import DysonSurface
from genesys.nested.models import Model
from ..life import Habitat, StarLife
from ..planet import AncientPlanet, AsteroidBelt, BarrenPlanet, FuturePlanet, GasGiant, MedievalPlanet, Orbit, \
    Planet, TerraformedPlanet, VisitorPlanet
from generated.materials.chemistry import elements, Atom
from genesys.nested.data import lookups


class Star(Habitat):
    matter = Model.children_property(Atom)

    class Factory(Model.Factory):
        class DataProvider:
            star = lookups.stars

        name = property(lambda self: self.provider.star)

        @classmethod
        def life(cls):
            yield StarLife

        @classmethod
        def matter(cls):
            yield elements['H']
            yield elements['He']

        def children(self):
            yield from self.life()
            yield from self.matter()


class StarSystem(Model):
    main_star = Model.child_property(Star)
    stars = Model.children_property(Star)
    orbits = Model.children_property(Orbit)
    planets = Model.children_property(Planet)
    asteroid_belts = Model.children_property(AsteroidBelt)
    dyson_surfaces = Model.children_property(DysonSurface)

    class Factory(Model.Factory):
        @classmethod
        def stars(cls):
            yield Star
            yield Star.probable(3)

        @classmethod
        def inhabited(cls):
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

        @classmethod
        def orbits(cls):
            yield from cls.inhabited()
            yield BarrenPlanet.probable(60)
            yield BarrenPlanet.probable(40)
            yield BarrenPlanet.probable(20)
            yield GasGiant.probable(60)
            yield GasGiant.probable(40)
            yield GasGiant.probable(20)
            yield GasGiant.probable(10)
            yield from AsteroidBelt.multiple(0, 2)

        def children(self):
            yield from self.stars()
            yield from self.orbits()


class SingleStar(StarSystem):
    class Factory(StarSystem.Factory):
        @classmethod
        def stars(cls):
            yield Star

        @classmethod
        def inhabited(cls):
            yield None

        @classmethod
        def orbits(cls):
            yield None
