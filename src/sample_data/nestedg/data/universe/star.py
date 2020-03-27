from nestedg.mixins import EncounteredMixin
from nestedg.model import Model
from nestedg.data import unknown, lookups
from nestedg.data.materials import elements
from . import planet


class Star(Model, EncounteredMixin):
    contents = Model.children_property(elements.Hydrogen, elements.Helium)

    class BaseGenerator(Model.BaseGenerator):
        default = lookups.stars

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield unknown.Ghost.probable(0.1)
            yield unknown.SpaceMonster.probable(0.2)
            yield elements.Hydrogen
            yield elements.Helium


class StarSystem(Model):
    star = Model.child_property(Star)
    stars = Model.children_property(Star)
    planets = Model.children_property(planet.Planet)
    asteroid_belts = Model.children_property(planet.AsteroidBelt)
    dyson_surfaces = Model.children_property(unknown.DysonSurface)
    orbits = Model.children_property(planet.Planet, planet.AsteroidBelt, unknown.DysonSurface)

    class ChildrenGenerator(Model.ChildrenGenerator):
        @classmethod
        def _generate_inhabited(cls):
            yield planet.VisitorPlanet.probable(5)
            yield planet.FuturePlanet.probable(10)
            yield planet.TerraformedPlanet.probable(50)
            yield planet.TerraformedPlanet.probable(20)
            yield planet.TerraformedPlanet.probable(10)
            yield planet.MedievalPlanet.probable(30)
            yield planet.MedievalPlanet.probable(20)
            yield planet.AncientPlanet.probable(50)
            yield planet.AncientPlanet.probable(30)
            yield planet.AncientPlanet.probable(10)

        def children_classes(self):
            yield Star
            yield Star.probable(3)
            yield from self._generate_inhabited()
            yield planet.BarrenPlanet.probable(60)
            yield planet.BarrenPlanet.probable(40)
            yield planet.BarrenPlanet.probable(20)
            yield planet.GasGiant.probable(60)
            yield planet.GasGiant.probable(40)
            yield planet.GasGiant.probable(20)
            yield planet.GasGiant.probable(10)
            yield from planet.AsteroidBelt.multiple(0, 2)


class DysonSphere(StarSystem):
    class ChildrenGenerator(StarSystem.ChildrenGenerator):
        @classmethod
        def _generate_inhabited(cls):
            yield unknown.DysonSurface
            yield from planet.FuturePlanet.multiple(1, 8)


class SingleStar(StarSystem):
    class ChildrenGenerator(StarSystem.ChildrenGenerator):
        def children_classes(self):
            yield Star
