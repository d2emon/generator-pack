"""
Universe stuff
"""
# black_hole
# god
from factories.thing.nested_factory import NestedFactory
from models import universe
from utils.nested import select_item
from .data_provider import PROVIDER
from .planet.core import PlanetCoreFactory
from .planet.body import AsteroidFactory, MoonFactory, PlanetFactory, TerraformedMoonFactory
from .planet.gas_giant import GasGiantFactory, GasGiantAtmosphereFactory
from .planet import AncientPlanetFactory, BarrenPlanetFactory, DefaultPlanetFactory, FuturePlanetFactory, MedievalPlanetFactory, \
    TerraformedPlanetFactory, VisitorPlanetFactory
from .orbit import AsteroidBeltFactory, EarthFactory
from .star import DysonSphereFactory, StarFactory, StarSystemFactory
from .nebula import InterstellarCloudFactory, NebulaFactory
from .galaxy import GalaxyFactory, GalaxyArmFactory, GalaxyCenterFactory

from .black_hole import Answer42Factory, BlackHoleFactory, EndOfUniverseNoteFactory, EverythingFactory, InsideTheBlackHoleFactory, \
    WhiteHoleFactory
# from .god import D2emonThoughtsFactory, D2emonPsycheFactory, D2emonFactory, GodFactory


class SuperclusterFactory(NestedFactory):
    model = universe.Supercluster

    def children(self):
        yield GalaxyFactory.multiple(10, 30)


class UniverseFactory(NestedFactory):
    model = universe.Universe

    def children(self):
        yield SuperclusterFactory.multiple(10, 30)


class MultiverseFactory(NestedFactory):
    default_data = PROVIDER
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
    # # 'orteil': D2emonFactory(),
    # I do what I want
    # # 'god': GodFactory(),
    # I'm a fucking god
    # # 'orteil psyche': D2emonPsycheFactory(),
    # # 'orteil thoughts': D2emonThoughtsFactory(),
}


"""
new Thing("orteil",["body", "orteil psyche", "clothing set", "computer"],"Orteil");
//I do what I want
new Thing("god",[".orteil"],"Orteil");
//I'm a fucking god
new Thing("orteil psyche",["orteil thoughts"],"psyche");
new Thing("orteil thoughts",[],["OH MY GOD WHAT ARE YOU DOING HERE TURN BACK IMMEDIATELY", "WHAT IS WRONG WITH YOU", "WHAT THE HELL GO AWAY", "WHAT ARE YOU DOING OH GOD", "WHY THE HELL ARE YOU HERE", "I DO WHAT I WANT OKAY", "NO I DON'T CARE GO AWAY", "WHAT DID I EVEN DO TO YOU", "OH NO WHY THIS", "OKAY JUST <a href=\"http://orteil.deviantart.com\">GO THERE ALREADY</a>", "<a href=\"http://twitter.com/orteil42\">WHATEVER</a>"]);
"""
