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
    'planet': PlanetFactory(),
    'barren planet': BarrenPlanetFactory(),
    'visitor planet': VisitorPlanetFactory(),
    'future planet': FuturePlanetFactory(),
    'terraformed planet': FuturePlanetFactory(),
    'medieval planet': FuturePlanetFactory(),
    'ancient planet': FuturePlanetFactory(),
    'planet composition': PlanetCompositionFactory(),
    # 'moon",["ghost,0.1%","Rock","planet core"],[["young","old","large","small","pale","white","dark","black","old"],[" moon"]]);
    # 'terraformed moon",[".planet composition","continent,1-4","ocean,1-4","sky"],[["young","old","large","small","pale","white","dark","black","old","green","lush","blue","city","colonized","life"],[" moon"]]);
    # 'asteroid belt",["galactic life,20%","asteroid,10-30"]);
    # 'earth",[".asteroid belt"],"Earth");
    # 'asteroid",["space animal,0.5%","Rock","Ice,30%"],"asteroid");
    # 'gas giant",["gas giant atmosphere","planet core,50%","moon,0-3","terraformed moon,20%","terraformed moon,10%"]);
    # 'gas giant atmosphere",["galactic life,10%","Helium","Hydrogen","Water,50%","Ammonia,50%","Methane,50%"],"atmosphere");
    # 'planet core",["space monster,0.5%","Iron","Rock","Diamond,2%","Magma"],"core");

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
