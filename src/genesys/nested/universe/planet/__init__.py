from genesys.nested.factories.nested_factory import NestedFactory
from models.planet import Planet, BarrenPlanet, TelluricPlanet
# from ...temporary import VisitorCityFactory, VisitorInstallationFactory, ContinentFactory, FutureContinentFactory, \
#     MedievalContinentFactory, AncientContinentFactory, FutureMoonFactory
# from ...life import BarrenPlanetLifeFactory, VisitorPlanetLifeFactory
# from ...terrain import OceanFactory, SkyFactory, FutureSkyFactory, TerraformedSkyFactory
# from .atmosphere import AtmosphereFactory, GasGiantAtmosphereFactory
from .body import PlanetLikeFactory, MoonFactory, TerraformedMoonFactory, FutureMoonFactory
from .core import PlanetCoreFactory
# from .plate import PlateFactory, MoonPlateFactory, AsteroidPlateFactory
# from .plate import PlateFactory
# from .planet import PlanetFactory, BarrenPlanetFactory, VisitorPlanetFactory, TelluricPlanetFactory, \
#     FuturePlanetFactory, TerraformedPlanetFactory, DefaultPlanetFactory, MedievalPlanetFactory, AncientPlanetFactory, \
#     GasGiantFactory


# Default Planet
# Barren Planet
# Visitor Planet
# Future Planet
# Terraformed Planet
# Medieval Planet
# Ancient Planet
# Planet Composition
# Body in .body
# Asteroid in .asteroid
# GasGiant in .gas_giant
# PlanetCore in .core


class PlanetFactory(PlanetLikeFactory):
    default_model = Planet
    default_name = 'telluric planet'

    def core(self):
        yield from PlanetCompositionFactory.planet_composition()

    def moons(self):
        # yield MoonFactory().probable(40)
        # yield MoonFactory().probable(20)
        # yield MoonFactory().probable(10)
        yield from super().moons()


class TelluricPlanetFactory(PlanetFactory):
    default_model = TelluricPlanet
    default_name = 'telluric planet'

    def life(self):
        yield None

    def atmosphere(self):
        # yield AtmosphereFactory()
        yield None

    def continents(self):
        # yield from ContinentFactory().multiple(2, 7)
        yield None

    def core(self):
        yield from PlanetCompositionFactory.planet_composition()

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
    default_model = BarrenPlanet

    def life(self):
        # yield BarrenPlanetLifeFactory()
        # galactic life,10%
        yield None

    def atmosphere(self):
        yield None

    def continents(self):
        # rock
        yield None

    def oceans(self):
        # ice,50%
        yield None

    def sky(self):
        yield None


class VisitorPlanetFactory(TelluricPlanetFactory):
    default_model = BarrenPlanet

    def life(self):
        # yield VisitorPlanetLifeFactory()
        # galactic life
        yield None

    def visited(self):
        # yield from VisitorCityFactory().multiple(1, 8)
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


class PlanetCompositionFactory(NestedFactory):
    default_model = Planet
    default_name = 'planet'

    @classmethod
    def planet_composition(cls):
        yield PlanetCoreFactory

        yield MoonFactory.probable(40)
        yield MoonFactory.probable(20)
        yield MoonFactory.probable(10)

    def contents(self):
        yield from self.planet_composition()


"""
new Thing("planet",[".terraformed planet"],"telluric planet");
new Thing("barren planet",[
    ##Life##
    "galactic life,10%",
    ##Continent##
    "rock",
    ##Ocean##
    "ice,50%",
    ##Sky##
    ##Moon##
    ##Planet##
    ".planet composition"
], "telluric planet" );
new Thing("visitor planet",[
    "visitor city,1-8",
    "visitor installation,2-6",
    "galactic life",
    ##Continent##
    "rock",
    ##Ocean##
    "ice,50%",
    ##Sky##
    ##Moon##
    ##Planet##
    ".planet composition"
],"telluric planet");
new Thing("future planet",[
    ##Continent##
    "future continent,2-7",
    ##Ocean##
    "ocean,1-7",
    ##Sky##
    "future sky",
    ##Moon##
    ".future moon,30%",
    ##Planet##
    ".planet composition"
],"telluric planet");
new Thing("terraformed planet",[
    ##Continent##
    "continent,2-7",
    ##Ocean##
    "ocean,1-7",
    ##Sky##
    "terraformed sky",
    ##Moon##
    ".terraformed moon,30%",
    ##Planet##
    ".planet composition"
],"telluric planet");
new Thing("medieval planet",[
    ##Continent##
    "medieval continent,2-4",
    "ancient continent,0-3",
    ##Ocean##
    "ocean,1-7",
    ##Sky##
    "sky",
    ##Moon##
    ##Planet##
    ".planet composition"
],"telluric planet");
new Thing("ancient planet",[
    ##Continent##
    "ancient continent,2-7",
    ##Ocean##
    "ocean,1-7",
    ##Sky##
    "sky",
    ##Moon##
    ##Planet##
    ".planet composition"
],"telluric planet");
new Thing("planet composition",[
    "planet core",
    "moon,40%",
    "moon,20%",
    "moon,10%"
],"planet");
"""
