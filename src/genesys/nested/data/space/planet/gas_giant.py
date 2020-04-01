from .planet_like import PlanetCore
from .atmosphere import GasGiantAtmosphere
from .moon import Moon, TerraformedMoon
from .planet import Planet


class GasGiant(Planet):
    class ChildrenFactory(Planet.ChildrenFactory):
        def children_classes(self):
            yield GasGiantAtmosphere
            yield PlanetCore.probable(50)
            yield from Moon.multiple(0, 3)
            yield TerraformedMoon.probable(20)
            yield TerraformedMoon.probable(10)
