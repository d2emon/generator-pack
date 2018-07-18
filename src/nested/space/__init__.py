from ..thing import Thing
from ..children import ChildGenerator


class Multiverse(Thing):
    type_name = "multiverse"
    child_generators = [ChildGenerator("universe", (10, 30))]
    names_data = ["multiverse","lasagnaverse","doughnutverse","towelverse","baconverse","sharkverse","nestedverse","tastyverse","upverse","downverse","layerverse","clusterverse","metaverse","quantiverse","paraverse","epiverse","alterverse","hypoverse","dimensioverse","planiverse","pluriverse","polyverse","maniverse","stackoverse","antiverse","superverse","upperverse","maxiverse","megaverse","babyverse","tinyverse","retroverse","ultraverse","topoverse","otherverse","bubbleverse","esreverse","versiverse","'verse","cookieverse","grandmaverse"]


class Universe(Thing):
    type_name = "universe"
    child_generators = [ChildGenerator("supercluster", (10, 30))]


class Supercluster(Thing):
    type_name = "supercluster"
    child_generators = [ChildGenerator("galaxy", (10, 30))]
    names_data = "galactic supercluster"


class Galaxy(Thing):
    type_name = "galaxy"
    child_generators = [
        ChildGenerator("galaxy center"),
        ChildGenerator("galaxy arm", (2, 6)),
    ]


class GalaxyArm(Thing):
    type_name = "galaxy arm"
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
    type_name = "galaxy center"
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
    type_name = "nebula"
    child_generators = [
        ChildGenerator("galactic life", probability=15),
        ChildGenerator("star", probability=2),
        ChildGenerator("star", probability=2),
        ChildGenerator("star", probability=2),
        ChildGenerator("interstellar cloud", (1, 6)),
    ]


class InterstellarCloud(Thing):
    type_name = "interstellar cloud"
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
    type_name = "star system"
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


class DysonSphere(Thing):
    type_name = "dyson sphere"
    child_generators = [
        ChildGenerator("star"),
        ChildGenerator("star", probability=3),
        ChildGenerator("dyson surface"),
        ChildGenerator("future planet", (1, 8)),
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
    type_name = "star"
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


# ChildGenerator("galactic life", probability=5),
# ChildGenerator("nebula", (0, 12)),
# ChildGenerator("black hole", probability=20),
# ChildGenerator("star"),
# ChildGenerator("dyson surface"),
# ChildGenerator("visitor planet", probability=5),
# ChildGenerator("future planet", (1, 8)),
# ChildGenerator("terraformed planet", probability=50),
# ChildGenerator("medieval planet", probability=30),
# ChildGenerator("ancient planet", probability=50),
# ChildGenerator("barren planet", probability=60),
# ChildGenerator("gas giant", probability=60),
# ChildGenerator("asteroid belt", (0, 2)),
# ChildGenerator("ghost", probability=0.1),
# ChildGenerator("space monster", probability=0.2),

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
]