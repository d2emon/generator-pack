from genesys.nested.models.models.unknown import Ghost, Continent
from genesys.nested.models.mixins import TerraformedMixin
from .planet_like import PlanetLike
from genesys.nested.models.models.chemistry import Rock
from genesys.nested.models.models.terrain import Ocean, Sky
from genesys.nested.data import lookups


class Moon(PlanetLike):
    class BaseFactory(PlanetLike.BaseFactory):
        default = lookups.moons

    class ChildrenFactory(PlanetLike.ChildrenFactory):
        def children_classes(self):
            yield Ghost.probable(0.1)
            yield Rock
            yield from PlanetLike.ChildrenFactory.children_classes(self)


class TerraformedMoon(Moon, TerraformedMixin):
    class BaseFactory(PlanetLike.BaseFactory):
        default = lookups.terraformed_moons

    class ChildrenFactory(Moon.ChildrenFactory):
        def children_classes(self):
            yield from Continent.multiple(1, 4)
            yield from Ocean.multiple(1, 4)
            yield Sky
            yield from PlanetLike.ChildrenFactory.children_classes(self)