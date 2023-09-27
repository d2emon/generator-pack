"""
Universe stuff
"""
from genesys.nested.factories.nested_factory import NestedFactory
from models import universe
from utils.nested import select_item
from .black_hole import Answer42Factory, BlackHoleFactory, EndOfUniverseNoteFactory, EverythingFactory, InsideTheBlackHoleFactory, \
    WhiteHoleFactory
from .god import D2emonPsycheFactory, D2emonThoughtsFactory, GodFactory
from .planet.core import PlanetCoreFactory
from .planet.body import AsteroidFactory, MoonFactory, TerraformedMoonFactory
from .planet.gas_giant import GasGiantFactory, GasGiantAtmosphereFactory
from .planet import AncientPlanetFactory, BarrenPlanetFactory, DefaultPlanetFactory, FuturePlanetFactory, MedievalPlanetFactory, \
    PlanetFactory, TerraformedPlanetFactory, VisitorPlanetFactory
from .orbit import AsteroidBeltFactory, EarthFactory
from .star import DysonSphereFactory, StarFactory, StarSystemFactory
from .nebula import InterstellarCloudFactory, NebulaFactory
from .galaxy import GalaxyFactory, GalaxyArmFactory, GalaxyCenterFactory


class SuperclusterFactory(NestedFactory):
    model = universe.Supercluster

    def children(self):
        yield GalaxyFactory.multiple(10, 30)


class UniverseFactory(NestedFactory):
    model = universe.Universe

    def children(self):
        yield SuperclusterFactory.multiple(10, 30)


class MultiverseFactory(NestedFactory):
    model = universe.Multiverse

    def children(self):
        yield UniverseFactory.multiple(10, 30)

    def name_factory(self, data, *args, **kwargs):
        return select_item(*data.multiverse)


FACTORIES = {
    'multiverse': MultiverseFactory,
    'universe': UniverseFactory,
    'supercluster': SuperclusterFactory,
    'galaxy': GalaxyFactory,
    'galaxy arm': GalaxyArmFactory,
    'galaxy center': GalaxyCenterFactory,
    'nebula': NebulaFactory,
    'interstellar cloud': InterstellarCloudFactory,
    'star system': StarSystemFactory,
    'dyson sphere': DysonSphereFactory,
    'star': StarFactory,
    'planet': DefaultPlanetFactory,
    'barren planet': BarrenPlanetFactory,
    'visitor planet': VisitorPlanetFactory,
    'future planet': FuturePlanetFactory,
    'terraformed planet': TerraformedPlanetFactory,
    'medieval planet': MedievalPlanetFactory,
    'ancient planet': AncientPlanetFactory,
    'planet composition': PlanetFactory,
    'moon': MoonFactory,
    'terraformed moon': TerraformedMoonFactory,
    'asteroid belt': AsteroidBeltFactory,
    'earth': EarthFactory,
    'asteroid': AsteroidFactory,
    'gas giant': GasGiantFactory,
    'gas giant atmosphere': GasGiantAtmosphereFactory,
    'planet core': PlanetCoreFactory,

    'black hole': BlackHoleFactory,
    'inside the black hole': InsideTheBlackHoleFactory,
    'white hole': WhiteHoleFactory,
    '42': Answer42Factory,
    'everything': EverythingFactory,
    'end of universe note': EndOfUniverseNoteFactory,
    # I do what I want
    # I'm a fucking god
    'd2emon': GodFactory,
    'god': GodFactory,
    'd2emon psyche': D2emonPsycheFactory,
    'd2emon thoughts': D2emonThoughtsFactory,
}
