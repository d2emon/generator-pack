from genesys.nested.factories.nested_factory import NestedFactory
from models.planet import GasGiant
from models.planet.atmosphere import Atmosphere
from . import PlanetFactory


# Gas Giant
# Gas Giant Atmosphere


class GasGiantFactory(PlanetFactory):
    default_model = GasGiant

    def atmosphere(self):
        # yield GasGiantAtmosphereFactory()
        # gas giant atmosphere 
        yield None

    def core(self):
        # yield PlanetCoreFactory().probable(50)
        # planet core,50% 
        yield None

    def moons(self):
        # yield from MoonFactory().multiple(0, 3)
        # yield TerraformedMoonFactory().probable(20)
        # yield TerraformedMoonFactory().probable(10)
        # moon,0-3
        # terraformed moon,20%
        # terraformed moon,10% 
        yield None


class GasGiantAtmosphereFactory(NestedFactory):
    default_model = Atmosphere

    def life(self):
        # yield GasGiantLifeFactory()
        # galactic life,10%
        yield None

    def contents(self):
        # yield MoleculeFactory.from_elements('He')
        # yield MoleculeFactory.from_elements('H')
        # yield SteamFactory().probable(50)
        # yield AmmoniaFactory().probable(50)
        # yield MethaneFactory().probable(50)
        # helium
        # hydrogen
        # water,50%
        # ammonia,50%
        # methane,50%
        yield None


"""
new Thing("gas giant",[
    "gas giant atmosphere",
    "planet core,50%",
    "moon,0-3",
    "terraformed moon,20%",
    "terraformed moon,10%"
]);
new Thing("gas giant atmosphere",[
    "galactic life,10%",
    "helium",
    "hydrogen",
    "water,50%",
    "ammonia,50%",
    "methane,50%"
],"atmosphere");
"""
