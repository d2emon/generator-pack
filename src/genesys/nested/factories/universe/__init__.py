from .universe import SuperclusterFactory, UniverseFactory, MultiverseFactory
from .galaxy import SpaceFactory, GalaxyArmFactory, GalaxyCenterFactory, GalaxyFactory
from .nebula import InterstellarCloudFactory, NebulaFactory
from .star import StarFactory, StarSystemFactory, SingleStarFactory, DysonSphereFactory
from .orbit import OrbitFactory, PlanetOrbitFactory, BarrenOrbitFactory, VisitorOrbitFactory, FutureOrbitFactory, \
    TerraformedOrbitFactory, MedievalOrbitFactory, AncientOrbitFactory, GasGiantFactory, AsteroidBeltFactory, \
    EarthFactory
from .planet import *
from .atmosphere import AtmosphereFactory, GasGiantAtmosphereFactory
from .black_hole import EndOfUniverseNoteFactory, EverythingFactory, Answer42Factory, WhiteHoleFactory, \
    InsideTheBlackHoleFactory, BlackHoleFactory
from .god import D2emonThoughtsFactory, D2emonPsycheFactory, D2emonFactory, GodFactory


FACTORIES = {
    'multiverse': MultiverseFactory(),
    'universe': UniverseFactory(),
    'supercluster': SuperclusterFactory(),
    'galaxy': GalaxyFactory(),
    'galaxy arm': GalaxyArmFactory(),
    'galaxy center': GalaxyCenterFactory(),
    'nebula': NebulaFactory(),
    'interstellar cloud': InterstellarCloudFactory(),
    'star system': StarSystemFactory(),
    'dyson sphere': DysonSphereFactory(),
    'star': StarFactory(),
    'planet': DefaultPlanetFactory(),
    'barren planet': BarrenPlanetFactory(),
    'visitor planet': VisitorPlanetFactory(),
    'future planet': FuturePlanetFactory(),
    'terraformed planet': FuturePlanetFactory(),
    'medieval planet': FuturePlanetFactory(),
    'ancient planet': FuturePlanetFactory(),
    'planet composition': PlanetFactory(),
    'moon': MoonFactory(),
    'terraformed moon': TerraformedMoonFactory(),
    'asteroid belt': AsteroidBeltFactory(),
    'earth': EarthFactory(),
    'asteroid': AsteroidFactory(),
    'gas giant': GasGiantFactory(),
    'gas giant atmosphere': GasGiantAtmosphereFactory(),
    'planet core': PlanetCoreFactory(),

    'black hole': BlackHoleFactory(),
    'inside the black hole': InsideTheBlackHoleFactory(),
    'white hole': WhiteHoleFactory(),
    '42': Answer42Factory(),
    'everything': EverythingFactory(),
    'end of universe note': EndOfUniverseNoteFactory(),
    'orteil': D2emonFactory(),
    'god': GodFactory(),
    'orteil psyche': D2emonPsycheFactory(),
    'orteil thoughts': D2emonThoughtsFactory(),
}
