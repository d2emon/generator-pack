from ..thing import Thing
from ..children import ChildGenerator

from .dyson import DysonSphere, DysonSurface, DysonSegment


class Multiverse(Thing):
    child_generators = [ChildGenerator("universe", (10, 30))]
    names_data = ["multiverse","lasagnaverse","doughnutverse","towelverse","baconverse","sharkverse","nestedverse","tastyverse","upverse","downverse","layerverse","clusterverse","metaverse","quantiverse","paraverse","epiverse","alterverse","hypoverse","dimensioverse","planiverse","pluriverse","polyverse","maniverse","stackoverse","antiverse","superverse","upperverse","maxiverse","megaverse","babyverse","tinyverse","retroverse","ultraverse","topoverse","otherverse","bubbleverse","esreverse","versiverse","'verse","cookieverse","grandmaverse"]


class Universe(Thing):
    child_generators = [ChildGenerator("supercluster", (10, 30))]


class Supercluster(Thing):
    child_generators = [ChildGenerator("galaxy", (10, 30))]
    names_data = "galactic supercluster"


class Galaxy(Thing):
    child_generators = [
        ChildGenerator("galaxy center"),
        ChildGenerator("galaxy arm", (2, 6)),
    ]


class GalaxyArm(Thing):
    child_generators = [
        ChildGenerator("galactic life", probability=5),
        ChildGenerator("dyson sphere", probability=4),
        ChildGenerator("dyson sphere", probability=2),
        ChildGenerator("star system", (20, 50)),
        ChildGenerator("nebula", (0, 12)),
        ChildGenerator("black hole", probability=20),
        ChildGenerator("black hole", probability=20),
    ]
    names_data = "arm"


class GalaxyCenter(Thing):
    child_generators = [
        ChildGenerator("black hole"),
        ChildGenerator("galactic life", probability=10),
        ChildGenerator("dyson sphere", probability=4),
        ChildGenerator("dyson sphere", probability=2),
        ChildGenerator("star system", (20, 50)),
        ChildGenerator("nebula", (0, 12))
    ]
    # children_data = ["black hole","galactic life,10%","dyson sphere,4%","dyson sphere,2%","star system,20-50","nebula,0-12"]
    names_data = "galactic center"


class Nebula(Thing):
    child_generators = [
        ChildGenerator("galactic life", probability=15),
        ChildGenerator("star", probability=2),
        ChildGenerator("star", probability=2),
        ChildGenerator("star", probability=2),
        ChildGenerator("interstellar cloud", (1, 6)),
    ]


class InterstellarCloud(Thing):
    child_generators = [
        ChildGenerator("helium"),
        ChildGenerator("hydrogen"),
        ChildGenerator("carbon", probability=80),
        ChildGenerator("water", probability=5),
        ChildGenerator("ammonia", probability=5),
        ChildGenerator("nitrogen", probability=5),
        ChildGenerator("iron", probability=5),
        ChildGenerator("sulfur", probability=5),
        ChildGenerator("oxygen", probability=15),
    ]
    names_data =[
        ["a bright pink", "a faint", "a fading", "a pale", "a fluo", "a glowing", "a green", "a bright green", "a dark brown", "a brooding", "a magenta", "a bright red", "a dark red", "a blueish", "a deep blue", "a turquoise", "a teal", "a golden", "a multicolored", "a silver", "a dramatic", "a luminous", "a colossal", "a purple", "a gold-trimmed", "an opaline", "a silvery", "a shimmering"],
        [" "],
        ["interstellar cloud"]
    ]


class StarSystem(Thing):
    child_generators = [
        ChildGenerator("star"),
        ChildGenerator("star", probability=3),
        ChildGenerator("visitor planet", probability=5),
        ChildGenerator("future planet", probability=10),
        ChildGenerator("future planet", probability=10),
        ChildGenerator("terraformed planet", probability=50),
        ChildGenerator("terraformed planet", probability=20),
        ChildGenerator("terraformed planet", probability=10),
        ChildGenerator("medieval planet", probability=30),
        ChildGenerator("medieval planet", probability=20),
        ChildGenerator("ancient planet", probability=50),
        ChildGenerator("ancient planet", probability=30),
        ChildGenerator("ancient planet", probability=10),
        ChildGenerator("barren planet", probability=60),
        ChildGenerator("barren planet", probability=40),
        ChildGenerator("barren planet", probability=20),
        ChildGenerator("gas giant", probability=60),
        ChildGenerator("gas giant", probability=40),
        ChildGenerator("gas giant", probability=20),
        ChildGenerator("gas giant", probability=10),
        ChildGenerator("asteroid belt", (0, 2)),
    ]


class Star(Thing):
    child_generators = [
        ChildGenerator("ghost", probability=0.1),
        ChildGenerator("space monster", probability=0.2),
        ChildGenerator("hydrogen"),
        ChildGenerator("helium"),
    ]
    name_data = [
        ["white","faint","yellow","red","blue","green","purple","bright","double","twin","triple","old","young","dying","small","giant","large","pale","dark","hell","horrific","twisted","spectral"],
        [" star"],
    ]


# addThing("planet",[".terraformed planet"],"telluric planet")
class Planet(Thing):
    pass


class TelluricPlanet(Planet):
    names_data = "telluric planet"


class BarrenPlanet(TelluricPlanet):
    child_generators = [
        ChildGenerator("galactic life", probability=10),
        ChildGenerator("rock"),
        ChildGenerator("ice", probability=50),
        ChildGenerator(".planet composition"),
    ]


class VisitorPlanet(TelluricPlanet):
    child_generators = [
        ChildGenerator("visitor city", (1, 8)),
        ChildGenerator("visitor installation", (2, 6)),
        ChildGenerator("galactic life"),
        ChildGenerator("rock"),
        ChildGenerator("ice", probability=50),
        ChildGenerator(".planet composition"),
    ]


class FuturePlanet(TelluricPlanet):
    child_generators = [
        ChildGenerator("future continent", (2, 7)),
        ChildGenerator("ocean", (1, 7)),
        ChildGenerator("future sky"),
        ChildGenerator(".future moon", probability=30),
        ChildGenerator(".planet composition"),
    ]


class TerraformedPlanet(TelluricPlanet):
    child_generators = [
        ChildGenerator("continent", (2, 7)),
        ChildGenerator("ocean", (1, 7)),
        ChildGenerator("terraformed sky"),
        ChildGenerator(".terraformed moon", probability=30),
        ChildGenerator(".planet composition"),
    ]


class MedievalPlanet(TelluricPlanet):
    child_generators = [
        ChildGenerator("medieval continent", (2, 4)),
        ChildGenerator("ancient continent", (0, 3)),
        ChildGenerator("ocean", (1, 7)),
        ChildGenerator("sky"),
        ChildGenerator(".planet composition"),
    ]


class AncientPlanet(TelluricPlanet):
    child_generators = [
        ChildGenerator("ancient continent", (2, 7)),
        ChildGenerator("ocean", (1, 7)),
        ChildGenerator("sky"),
        ChildGenerator(".planet composition"),
    ]


class PlanetComposition(Thing):
    child_generators = [
        ChildGenerator("planet core"),
        ChildGenerator("moon", probability=40),
        ChildGenerator("moon", probability=20),
        ChildGenerator("moon", probability=10)
    ]
    names_data = "planet"


class Moon(Planet):
    child_generators = [
        ChildGenerator("ghost", probability=0.1),
        ChildGenerator("rock"),
        ChildGenerator("planet core"),
    ]
    names_data = [
        ["young","old","large","small","pale","white","dark","black","old"],
        [" moon"],
    ]


class TerraformedMoon(Moon):
    child_generators = [
        ChildGenerator(".planet composition"),
        ChildGenerator("continent", (1, 4)),
        ChildGenerator("ocean", (1, 4)),
        ChildGenerator("sky"),
    ]
    names_data = [
        ["young", "old", "large", "small", "pale", "white", "dark", "black", "old", "green", "lush", "blue", "city", "colonized", "life"],
        [" moon"],
    ]


class AsteroidBelt(Thing):
    child_generators = [
        ChildGenerator("galactic life", probability=20),
        ChildGenerator("asteroid", (10, 30)),
    ]

#addThing("earth",[".asteroid belt"],"Earth")


class Asteroid(Planet):
    child_generators = [
        ChildGenerator("space animal", probability=0.5),
        ChildGenerator("rock"),
        ChildGenerator("ice", probability=30)
    ]
    names_data = "asteroid"


class GasGiant(Planet):
    child_generators = [
        ChildGenerator("gas giant atmosphere"),
        ChildGenerator("planet core", probability=50),
        ChildGenerator("moon", (0, 3)),
        ChildGenerator("terraformed moon", probability=20),
        ChildGenerator("terraformed moon", probability=10),
    ]


class GasGiantAtmosphere(Thing):
    child_generators = [
        ChildGenerator("galactic life", probability=10),
        ChildGenerator("helium"),
        ChildGenerator("hydrogen"),
        ChildGenerator("water", probability=50),
        ChildGenerator("ammonia", probability=50),
        ChildGenerator("methane", probability=50),
    ]
    names_data = "atmosphere"


class PlanetCore(Thing):
    child_generators = [
        ChildGenerator("space monster", probability=0.5),
        ChildGenerator("iron"),
        ChildGenerator("rock"),
        ChildGenerator("diamond", probability=2),
        ChildGenerator("magma"),
    ]
    names_data = "core"


class BlackHole(Star):
    child_generators = [ChildGenerator("inside the black hole")]


class InsideTheBlackHole(Thing):
    child_generators = [
        ChildGenerator("end of universe note", probability=0.5),
        ChildGenerator("crustacean", probability=0.2),
        ChildGenerator("white hole"),
    ]


class WhiteHole(BlackHole):
    child_generators = [ChildGenerator("universe")]


# new Thing("42",["universe"]);
# new Thing("everything",["universe"]);


class EndOfUniverseNote(Thing):
    child_generators = [ChildGenerator("pasta", probability=0.1)]
    names_data = [
        "Help! I'm trapped in a universe factory!",
        "Okay, you can stop clicking now.",
        "I want to get off Mr Orteil's Wild Ride",
        "my sides"
    ]

# new Thing("orteil",["body","orteil psyche","clothing set","computer"],"Orteil");//I do what I want
# new Thing("god",[".orteil"],"Orteil");//I'm a fucking god
# new Thing("orteil psyche",["orteil thoughts"],"psyche");
# new Thing("orteil thoughts",[],["OH MY GOD WHAT ARE YOU DOING HERE TURN BACK IMMEDIATELY","WHAT IS WRONG WITH YOU","WHAT THE HELL GO AWAY","WHAT ARE YOU DOING OH GOD","WHY THE HELL ARE YOU HERE","I DO WHAT I WANT OKAY","NO I DON'T CARE GO AWAY","WHAT DID I EVEN DO TO YOU","OH NO WHY THIS","OKAY JUST <a href=\"http://orteil.deviantart.com\">GO THERE ALREADY</a>","<a href=\"http://twitter.com/orteil42\">WHATEVER</a>"]);


# ChildGenerator("ghost", probability=0.1),
# ChildGenerator("visitor city", (1, 8)),
# ChildGenerator("visitor installation", (2, 6)),
# ChildGenerator("future continent", (2, 7)),
# ChildGenerator("ocean", (1, 7)),
# ChildGenerator("future sky"),
# ChildGenerator(".future moon", probability=30),
# ChildGenerator("continent", (2, 7)),
# ChildGenerator("terraformed sky"),
# ChildGenerator("medieval continent", (2, 4)),
# ChildGenerator("ancient continent", (0, 3)),
# ChildGenerator("sky"),
# ChildGenerator("pasta", probability=0.1)
# ChildGenerator("future city", (4, 20)),
# ChildGenerator("nanocollector", (12, 20)),


CONTENTS = [
    Multiverse,
    Universe,
    Supercluster,
    Galaxy,
    GalaxyArm,
    GalaxyCenter,
    Nebula,
    InterstellarCloud,
    StarSystem,
    DysonSphere,
    Star,
    BarrenPlanet,
    VisitorPlanet,
    FuturePlanet,
    TerraformedPlanet,
    MedievalPlanet,
    AncientPlanet,
    PlanetComposition,
    Moon,
    TerraformedMoon,
    AsteroidBelt,
    Asteroid,
    GasGiant,
    GasGiantAtmosphere,
    PlanetCore,
    BlackHole,
    InsideTheBlackHole,
    WhiteHole,
    EndOfUniverseNote,
    DysonSurface,
    DysonSegment,
]