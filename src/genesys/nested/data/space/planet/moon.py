from ... import unknown
from genesys.nested.models.mixins import TerraformedMixin
from .planet_like import PlanetLike
from ... import lookups
from ...chemistry import Rock


class Moon(PlanetLike):
    class BaseFactory(PlanetLike.BaseFactory):
        default = lookups.moons

    class ChildrenFactory(PlanetLike.ChildrenFactory):
        def children_classes(self):
            yield unknown.Ghost.probable(0.1)
            yield Rock
            yield from PlanetLike.ChildrenFactory.children_classes(self)


class TerraformedMoon(Moon, TerraformedMixin):
    class BaseFactory(PlanetLike.BaseFactory):
        default = lookups.terraformed_moons

    class ChildrenFactory(Moon.ChildrenFactory):
        def children_classes(self):
            yield from unknown.Continent.multiple(1, 4)
            yield from unknown.Ocean.multiple(1, 4)
            yield unknown.Sky
            yield from PlanetLike.ChildrenFactory.children_classes(self)
