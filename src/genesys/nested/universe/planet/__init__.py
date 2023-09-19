from factories.thing.nested_factory import NestedFactory
from models import planet
# from ...temporary import VisitorCityFactory, VisitorInstallationFactory, ContinentFactory, FutureContinentFactory, \
#     MedievalContinentFactory, AncientContinentFactory, FutureMoonFactory
# from ...life import BarrenPlanetLifeFactory, VisitorPlanetLifeFactory
# from ...terrain import OceanFactory, SkyFactory, FutureSkyFactory, TerraformedSkyFactory
from ...materials import IceFactory, RockFactory
# from .atmosphere import AtmosphereFactory, GasGiantAtmosphereFactory
from .body import PlanetLikeFactory, MoonFactory, TerraformedMoonFactory, FutureMoonFactory
from .core import PlanetCoreFactory
# from .plate import PlateFactory, MoonPlateFactory, AsteroidPlateFactory
# from .plate import PlateFactory
# from .planet import DefaultPlanetFactory, GasGiantFactory


# Planet Composition
# Body in .body
# Asteroid in .asteroid
# GasGiant in .gas_giant
# PlanetCore in .core

"""
new Thing("planet composition",[
    "planet core", "moon,40%", "moon,20%", "moon,10%"],"planet");
new Thing("moon",[
    "ghost,0.1%",
    RockFactory.one(),
    "planet core"],[["young", "old", "large", "small", "pale", "white", "dark", "black", "old"], [" moon"]]);
new Thing("terraformed moon",[
    ".planet composition", "continent,1-4", "ocean,1-4", "sky"],[["young", "old", "large", "small", "pale", "white", "dark", "black", "old", "green", "lush", "blue", "city", "colonized", "life"], [" moon"]]);
new Thing("asteroid belt",["galactic life,20%", "asteroid,10-30"]);
new Thing("earth",[".asteroid belt"],"Earth");
new Thing("asteroid",["space animal,0.5%",
    RockFactory.one(),
    IceFactory.probable(30),
    ],"asteroid");
new Thing("gas giant",["gas giant atmosphere", "planet core,50%", "moon,0-3", "terraformed moon,20%", "terraformed moon,10%"]);
new Thing("gas giant atmosphere",["galactic life,10%",
    ELEMENTS['He'].one(),
    ELEMENTS['H'].one(),
    WaterFactory.one().probable(50),
    AmmoniaFactory.one().probable(50),
    MethaneFactory.one().probable(50),
],"atmosphere");
new Thing("planet core",["space monster,0.5%",
    IronFactory.one(),
    RockFactory.one(),
    DiamondFactory.one().probable(2),
    MagmaFactory.one(),
],"core");
"""


class PlanetFactory(PlanetLikeFactory):
    # .planet composition
    model = planet.Planet
    default_name = 'planet'

    @classmethod
    def planet_composition(cls):
        yield PlanetCoreFactory

        yield MoonFactory.probable(40)
        yield MoonFactory.probable(20)
        yield MoonFactory.probable(10)

    def core(self):
        # yield from PlanetCompositionFactory.planet_composition()
        yield from super().core()

    def moons(self):
        # yield MoonFactory().probable(40)
        # yield MoonFactory().probable(20)
        # yield MoonFactory().probable(10)
        yield from super().moons()

    def children(self):
        yield from self.planet_composition()



class TelluricPlanetFactory(PlanetFactory):
    # = planet composition
    model = planet.TelluricPlanet

    def life(self):
        yield None

    def atmosphere(self):
        # yield AtmosphereFactory()
        yield None

    def continents(self):
        # yield from ContinentFactory().multiple(2, 7)
        yield None

    def core(self):
        yield from super().planet_composition()

    def moons(self):
        yield None

    def oceans(self):
        # yield from OceanFactory().multiple(1, 7)
        yield None

    def sky(self):
        # yield SkyFactory()
        yield None

    def visited(self):
        yield None


class BarrenPlanetFactory(TelluricPlanetFactory):
    model = planet.BarrenPlanet

    def life(self):
        # yield BarrenPlanetLifeFactory()
        # galactic life,10%
        yield None

    def atmosphere(self):
        yield None

    def continents(self):
        # rock
        yield RockFactory.one()

    def oceans(self):
        # ice,50%
        yield IceFactory.probable(50)

    def sky(self):
        yield None


class VisitorPlanetFactory(BarrenPlanetFactory):
    model = planet.BarrenPlanet

    def life(self):
        # yield VisitorPlanetLifeFactory()
        # galactic life
        yield None

    def visited(self):
        # yield VisitorCityFactory.multiple(1, 8)
        # yield from VisitorInstallationFactory().multiple(2, 6)
        # visitor city,1-8
        # visitor installation,2-6
        yield None


class FuturePlanetFactory(TelluricPlanetFactory):
    def continents(self):
        # future continent,2-7
        yield None

    def oceans(self):
        # ocean,1-7
        yield None

    def sky(self):
        # future sky
        yield None

    def moons(self):
        yield FutureMoonFactory.probable(30)


class TerraformedPlanetFactory(TelluricPlanetFactory):
    def continents(self):
        # continent,2-7
        yield None

    def oceans(self):
        # ocean,1-7
        yield None

    def sky(self):
        # yield TerraformedSkyFactory()
        # terraformed sky
        yield None

    def moons(self):
        yield TerraformedMoonFactory.probable(30)


class MedievalPlanetFactory(TelluricPlanetFactory):
    def continents(self):
        # yield from MedievalContinentFactory().multiple(2, 4)
        # yield from AncientContinentFactory().multiple(0, 3)
        # medieval continent,2-4
        # ancient continent,0-3
        yield None

    def oceans(self):
        # ocean,1-7
        yield None

    def sky(self):
        # yield TerraformedSkyFactory()
        # sky
        yield None

    def moons(self):
        yield None


class AncientPlanetFactory(TelluricPlanetFactory):
    def continents(self):
        # yield from AncientContinentFactory().multiple(2, 7)
        # ancient continent,2-7
        yield None

    def oceans(self):
        # ocean,1-7
        yield None

    def sky(self):
        # yield TerraformedSkyFactory()
        # sky
        yield None

    def moons(self):
        yield None


class DefaultPlanetFactory(TerraformedPlanetFactory):
    pass


"""
new Thing("planet composition",[
    "planet core",
    "moon,40%",
    "moon,20%",
    "moon,10%"
],"planet");
"""
