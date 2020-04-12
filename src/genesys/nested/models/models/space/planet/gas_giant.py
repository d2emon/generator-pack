from .atmosphere import GasGiantAtmosphere
from .moon import Moon, TerraformedMoon
from .planet import Planet
from .planet_like import PlanetCore


class GasGiant(Planet):
    class Factory(Planet.Factory):
        def atmosphere(self):
            yield GasGiantAtmosphere

        def core(self):
            yield PlanetCore.probable(50)

        def moons(self):
            yield from Moon.multiple(0, 3)
            yield TerraformedMoon.probable(20)
            yield TerraformedMoon.probable(10)

        def plates(self):
            yield None
