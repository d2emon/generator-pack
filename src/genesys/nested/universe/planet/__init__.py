from genesys.nested.factories.nested_factory import NestedFactory
from models.universe.planet import Planet, BarrenPlanet, TelluricPlanet
# from ...temporary import VisitorCityFactory, VisitorInstallationFactory, ContinentFactory, FutureContinentFactory, \
#     MedievalContinentFactory, AncientContinentFactory, FutureMoonFactory
# from ...life import BarrenPlanetLifeFactory, VisitorPlanetLifeFactory
# from ...terrain import OceanFactory, SkyFactory, FutureSkyFactory, TerraformedSkyFactory
# from .atmosphere import AtmosphereFactory, GasGiantAtmosphereFactory
# from .body import PlanetLikeFactory, AsteroidFactory, MoonFactory, TerraformedMoonFactory
# from .body import PlanetLikeFactory, MoonFactory, TerraformedMoonFactory
# from .core import PlanetCoreFactory
# from .plate import PlateFactory, MoonPlateFactory, AsteroidPlateFactory
# from .plate import PlateFactory
# from .planet import PlanetFactory, BarrenPlanetFactory, VisitorPlanetFactory, TelluricPlanetFactory, \
#     FuturePlanetFactory, TerraformedPlanetFactory, DefaultPlanetFactory, MedievalPlanetFactory, AncientPlanetFactory, \
#     GasGiantFactory



# class PlanetFactory(PlanetLikeFactory):
class PlanetFactory(NestedFactory):
    default_model = Planet
    default_name = 'telluric planet'

    @classmethod
    def moons(cls):
        # yield MoonFactory().probable(40)
        # yield MoonFactory().probable(20)
        # yield MoonFactory().probable(10)
        yield None

    def contents(self):
        # yield from super().children()
        # .terraformed planet
        yield from self.moons()


class TelluricPlanetFactory(PlanetFactory):
    default_model = TelluricPlanet
    default_name = 'telluric planet'

    def atmosphere(self):
        # yield AtmosphereFactory()
        yield None

    def biosphere(self):
        yield None

    def continents(self):
        # yield from ContinentFactory().multiple(2, 7)
        yield None

    def oceans(self):
        # yield from OceanFactory().multiple(1, 7)
        yield None

    def plates(self):
        yield from self.continents()
        yield from self.oceans()

    def sky(self):
        # yield SkyFactory()
        yield None


class BarrenPlanetFactory(TelluricPlanetFactory):
    default_model = BarrenPlanet

    def life(self):
        # galactic life,10%
        yield None

    def biosphere(self):
        # yield BarrenPlanetLifeFactory()
        yield None

    def plates(self):
        # yield PlateFactory()
        yield None

    @classmethod
    def moons(cls):
        yield None

    def contents(self):
        # yield from super().children()
        # rock
        # ice,50%
        yield from PlanetCompositionFactory.planet_composition()


class VisitorPlanetFactory(TelluricPlanetFactory):
    default_model = BarrenPlanet

    def life(self):
        # galactic life
        yield None

    def biosphere(self):
        # yield VisitorPlanetLifeFactory()
        yield None

    def visited(self):
        # yield from VisitorCityFactory().multiple(1, 8)
        # yield from VisitorInstallationFactory().multiple(2, 6)
        yield None

    def contents(self):
        # yield from super().children()
        # visitor city,1-8
        # visitor installation,2-6

        # rock
        # ice,50%
        yield from PlanetCompositionFactory.planet_composition()


class FuturePlanetFactory(TelluricPlanetFactory):
    def life(self):
        # galactic life
        yield None

    def continents(self):
        # yield from FutureContinentFactory().multiple(2, 7)
        yield None

    def sky(self):
        # yield FutureSkyFactory()
        yield None

    def moons(self):
        yield from super().moons()
        # yield FutureMoonFactory().probable(30)
        yield None

    def contents(self):
        # yield from super().children()
        # future continent,2-7
        # ocean,1-7
        # future sky
        # .future moon,30%
        yield from PlanetCompositionFactory.planet_composition()


class TerraformedPlanetFactory(TelluricPlanetFactory):
    def sky(self):
        # yield TerraformedSkyFactory()
        yield None

    def moons(self):
        yield from super().moons()
        # yield TerraformedMoonFactory().probable(30)
        yield None

    def contents(self):
        # yield from super().children()
        # continent,2-7
        # ocean,1-7
        # terraformed sky
        # .terraformed moon,30%
        yield from PlanetCompositionFactory.planet_composition()


class DefaultPlanetFactory(TerraformedPlanetFactory):
    pass


class MedievalPlanetFactory(TelluricPlanetFactory):
    def continents(self):
        # yield from MedievalContinentFactory().multiple(2, 4)
        # yield from AncientContinentFactory().multiple(0, 3)
        yield None

    def contents(self):
        # yield from super().children()
        # medieval continent,2-4
        # ancient continent,0-3
        # ocean,1-7
        # sky
        yield from PlanetCompositionFactory.planet_composition()


class AncientPlanetFactory(TelluricPlanetFactory):
    def continents(self):
        # yield from AncientContinentFactory().multiple(2, 7)
        yield None

    def contents(self):
        # yield from super().children()
        # ancient continent,2-7
        # ocean,1-7
        # sky
        yield from PlanetCompositionFactory.planet_composition()


class PlanetCompositionFactory(NestedFactory):
    default_model = Planet
    default_name = 'planet'

    @classmethod
    def planet_composition(cls):
        # planet core
        # moon,40%
        # moon,20%
        # moon,10%
        yield None

    def contents(self):
        yield from self.planet_composition()


"""
class GasGiantFactory(PlanetFactory):
    default_model = GasGiant

    def atmosphere(self):
        yield GasGiantAtmosphereFactory()

    def core(self):
        yield PlanetCoreFactory().probable(50)

    def moons(self):
        yield from MoonFactory().multiple(0, 3)
        yield TerraformedMoonFactory().probable(20)
        yield TerraformedMoonFactory().probable(10)

    def plates(self):
        yield None
"""


"""
new Thing("planet",[".terraformed planet"],"telluric planet");
new Thing("barren planet",[
    "galactic life,10%",
    "rock",
    "ice,50%",
    ".planet composition"
], "telluric planet" );
new Thing("visitor planet",[
    "visitor city,1-8",
    "visitor installation,2-6",
    "galactic life",
    "rock",
    "ice,50%",
    ".planet composition"
],"telluric planet");
new Thing("future planet",[
    "future continent,2-7",
    "ocean,1-7",
    "future sky",
    ".future moon,30%",
    ".planet composition"
],"telluric planet");
new Thing("terraformed planet",[
    "continent,2-7",
    "ocean,1-7",
    "terraformed sky",
    ".terraformed moon,30%",
    ".planet composition"
],"telluric planet");
new Thing("medieval planet",[
    "medieval continent,2-4",
    "ancient continent,0-3",
    "ocean,1-7",
    "sky",
    ".planet composition"
],"telluric planet");
new Thing("ancient planet",[
    "ancient continent,2-7",
    "ocean,1-7",
    "sky",
    ".planet composition"
],"telluric planet");
new Thing("planet composition",[
    "planet core",
    "moon,40%",
    "moon,20%",
    "moon,10%"
],"planet");

new Thing("moon",["ghost,0.1%","rock","planet core"],[["young","old","large","small","pale","white","dark","black","old"],[" moon"]]);
new Thing("terraformed moon",[".planet composition","continent,1-4","ocean,1-4","sky"],[["young","old","large","small","pale","white","dark","black","old","green","lush","blue","city","colonized","life"],[" moon"]]);
new Thing("asteroid belt",["galactic life,20%","asteroid,10-30"]);
new Thing("earth",[".asteroid belt"],"Earth");
new Thing("asteroid",["space animal,0.5%","rock","ice,30%"],"asteroid");
new Thing("gas giant",["gas giant atmosphere","planet core,50%","moon,0-3","terraformed moon,20%","terraformed moon,10%"]);
new Thing("gas giant atmosphere",["galactic life,10%","helium","hydrogen","water,50%","ammonia,50%","methane,50%"],"atmosphere");
new Thing("planet core",["space monster,0.5%","iron","rock","diamond,2%","magma"],"core");
"""
