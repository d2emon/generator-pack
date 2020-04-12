from genesys.nested.models.models.unknown import Ghost, Continent
from genesys.nested.models.mixins import TerraformedMixin
from .planet_like import PlanetLike, Plate
from ...chemistry import Rock
# from ...terrain import Ocean, Sky
from genesys.nested.data import lookups


class MoonPlate(Plate):
    class Factory(Plate.Factory):
        def children(self):
            yield Rock


class Moon(PlanetLike):
    class Factory(PlanetLike.Factory):
        class DataProvider:
            moon = lookups.moons

        name = property(lambda self: self.provider.moon)

        def biosphere(self):
            yield Ghost.probable(0.1)

        def plates(self):
            yield MoonPlate


class TerraformedMoon(Moon, TerraformedMixin):
    class Factory(Moon.Factory):
        class DataProvider:
            terraformed_moon = lookups.terraformed_moons

        name = property(lambda self: self.provider.terraformed_moon)

        def plates(self):
            yield from Continent.multiple(1, 4)
            # yield from Ocean.multiple(1, 4)

        def sky(self):
            # yield Sky
            yield None
