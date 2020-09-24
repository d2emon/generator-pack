from genesys.model.model import Model
from .atmosphere import GasGiantAtmosphere
from .moon import Moon, TerraformedMoon
from .planet import Planet
from .planet_like import PlanetCore


class GasGiant(Planet):
    class Factory(Planet.Factory):
        @classmethod
        def atmosphere(cls):
            yield GasGiantAtmosphere

        @classmethod
        def core(cls):
            yield PlanetCore.probable(50)

        @classmethod
        def moons(cls):
            yield from Moon.multiple(0, 3)
            yield TerraformedMoon.probable(20)
            yield TerraformedMoon.probable(10)

        @classmethod
        def plates(cls):
            yield None
