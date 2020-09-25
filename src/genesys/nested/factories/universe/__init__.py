from .universe import SuperclusterFactory, UniverseFactory, MultiverseFactory
from .galaxy import SpaceFactory, GalaxyArmFactory, GalaxyCenterFactory, GalaxyFactory
from .nebula import InterstellarCloudFactory, NebulaFactory
from .star import StarFactory, StarSystemFactory, SingleStarFactory, DysonSphereFactory
from .planet import *


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

    # 'black hole",["inside the black hole"]);
    # 'inside the black hole",["end of universe note,0.5%","crustacean,0.2%","white hole"]);
    # 'white hole",["universe"]);
    # '42",["universe"]);
    # 'everything",["universe"]);
    # 'end of universe note",["pasta,0.1%"],["Help! I'm trapped in a universe factory!","Okay, you can stop clicking now.","I want to get off Mr Orteil's Wild Ride","my sides"]);
    # 'orteil",["body","orteil psyche","clothing set","computer"],"Orteil");//I do what I want
    # 'god",[".orteil"],"Orteil");//I'm a fucking god
    # 'orteil psyche",["orteil thoughts"],"psyche");
    # 'orteil thoughts",[],["OH MY GOD WHAT ARE YOU DOING HERE TURN BACK IMMEDIATELY","WHAT IS WRONG WITH YOU","WHAT THE HELL GO AWAY","WHAT ARE YOU DOING OH GOD","WHY THE HELL ARE YOU HERE","I DO WHAT I WANT OKAY","NO I DON'T CARE GO AWAY","WHAT DID I EVEN DO TO YOU","OH NO WHY THIS","OKAY JUST <a href=\"http://orteil.deviantart.com\">GO THERE ALREADY</a>","<a href=\"http://twitter.com/orteil42\">WHATEVER</a>"]);
}
