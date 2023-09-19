from models import planet
from ...materials import ELEMENTS, AmmoniaFactory, MethaneFactory
from ...materials.water import SteamFactory
from ..unsorted_life import GalacticLifeFactory
from .atmosphere import AtmosphereFactory
from .body import MoonFactory, PlanetFactory, TerraformedMoonFactory
from .core import PlanetCoreFactory


class GasGiantAtmosphereFactory(AtmosphereFactory):
    model = planet.atmosphere.Atmosphere

    def life(self):
        yield GalacticLifeFactory.probable(10)

    def children(self):
        yield ELEMENTS['He'].one()
        yield ELEMENTS['H'].one()
        yield SteamFactory.probable(50)
        yield AmmoniaFactory.probable(50)
        yield MethaneFactory.probable(50)


class GasGiantFactory(PlanetFactory):
    model = planet.GasGiant

    def atmosphere(self):
        yield GasGiantAtmosphereFactory.one()

    def core(self):
        yield PlanetCoreFactory.probable(50)

    def moons(self):
        yield MoonFactory.multiple(0, 3)
        yield TerraformedMoonFactory.probable(20)
        yield TerraformedMoonFactory.probable(10)
