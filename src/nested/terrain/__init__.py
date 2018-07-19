from ..thing import Thing
from ..children import ChildGenerator


"""
//terrain stuff
new Thing("ocean",["sea water","sea life","beach,10-20",["iceberg,2-6","","","",""],"abyss"]);
new Thing("sea",["sea water","sea life","beach,2-6"],[["great","wide","big","old","young","large","small","dead","shallow","deep","red","yellow","green","blue","orange","brown","grey","black","white","purple","shady","bright","silver"],[" sea"]]);
new Thing("sea water",["water","salt"]);
new Thing("iceberg",["bear,30%","bear,10%","ice"]);
new Thing("beach",["beach life","sand"]);
new Thing("abyss",["sand","abyss life"]);
new Thing("sand",["silica"]);
new Thing("soil",[["worm,0-2","",""],["insect,0-2","",""],"silica"],"dirt");
new Thing("mud",[["worm,0-2","",""],["insect,0-2","",""],"water","silica"]);

new Thing("river",["river life","water","soil","mud"],["river","stream","brook","creek"]);
new Thing("lake",["lake life","water","soil","mud"],["lake","lagoon","pond","marsh","creek","cove"]);
new Thing("plain",["fire,0.3%","land life","river,0-3","lake,0-1","grass","soil","snow,5%"],["plain","steppe","valley","canyon","flatland","moor","grassland","prairie","desert","savannah","tundra","wasteland"]);
new Thing("forest",["fire,0.5%","forest life","river,0-2","trees","grass","humus","soil","snow,5%"],["forest","woods","copse"]);
new Thing("jungle",["fire,0.5%","jungle life","river,0-2","jungle trees","grass","humus","soil"],["jungle","rainforest"]);
new Thing("mountain",["mountain life","river,0-3","lake,0-1","cave,30%","cave,30%","cave,20%","trees","soil","rock","snow,40%"],["mountain","peak","hill","volcano","bluff","cliff","mesa","plateau"]);
new Thing("cave",["cave life","dragon lair,1%","river,20%","lake,10%","rock","iron,2%"],["cave","cavern","grotto"]);

new Thing("ancient plain",["fire,0.3%","caveman settlement,40%","ancient land life","river,0-3","lake,0-1","grass","soil","snow,5%"],["plain","steppe","valley","canyon","flatland","moor","grassland","prairie","desert","savannah","tundra","wasteland"]);
new Thing("ancient forest",["fire,0.5%","caveman settlement,40%","ancient forest life","river,0-2","trees","grass","humus","soil","snow,5%"],["forest","woods","copse"]);
new Thing("ancient jungle",["fire,0.5%","caveman settlement,40%","ancient jungle life","river,0-2","jungle trees","grass","humus","soil"],["jungle","rainforest"]);
new Thing("ancient mountain",["caveman settlement,40%","ancient mountain life","ancient cave,30%","ancient cave,20%","ancient cave,10%","river,0-3","lake,0-1","trees","soil","rock","snow,40%"],["mountain","peak","hill","volcano","bluff","cliff","mesa","plateau"]);
new Thing("ancient cave",["caveman settlement,65%","wall painting,50%","wall painting,30%","wall painting,30%",".cave"],["cave","cavern","grotto"]);
"""


class Sky(Thing):
    child_generators = [
        ChildGenerator("visitor ship", probability=10),
        ChildGenerator("meteorite", probability=3),
        ChildGenerator("sky life"),
        ChildGenerator("precipitation", probability=50),
        ChildGenerator("cloud", (2, 8)),
        ChildGenerator("oxygen"),
        ChildGenerator("carbon"),
        ChildGenerator("ozone"),
    ]
    names_data = "sky"


class TerraformedSky(Sky):
    child_generators = [
        ChildGenerator("plane", (1, 8)),
        ChildGenerator("rocketship", probability=20),
        ChildGenerator(".sky"),
    ]


class FutureSky(Sky):
    child_generators = [
        ChildGenerator("sprowseship", (4, 12)),
        ChildGenerator(".sky"),
    ]


class Meteorite(Thing):
    child_generators = [
        ChildGenerator("space animal", probability=6),
        ChildGenerator("ice", probability=60),
        ChildGenerator("rock"),
        ChildGenerator("iron", probability=40),
    ]
    names_data = "meteorite"


class Ozone(Thing):
    child_generators = [ChildGenerator("oxygen")]


class Cloud(Thing):
    child_generators = [ChildGenerator("water")]


class Precipitation(Cloud):
    names_data = [
        "rain",
        "snow",
        "hail",
        "mist",
        "fog",
        "drizzle",
        "storm",
    ]


CONTENTS = [
    FutureSky,
    TerraformedSky,
    Sky,
    Ozone,
    Cloud,
    Precipitation,
]