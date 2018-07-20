from ..thing import Thing
from ..children import ChildGenerator


class Continent(Thing):
    child_generators = [
        ChildGenerator("country", (1, 10)),
        ChildGenerator("sea", (1, 5)),
    ]
    names_data = [
        ["continent of "],
        ["A","Eu","Ame","Ocea","Anta","Atla"],
        ["frica","rtica","ropa","rica","nia","sia","ntide"],
    ]
    """
    [
        ["Eu","A","O","E"],
        ["rt","lt","rm","t","tr","tl","str","s","m","fr"],
        ["a","o","e","i"],
        ["ri","ni","ti","fri","",""],
        ["sia","nia","ca"]
    ]
    """


class Country(Thing):
    child_generators = [
        ChildGenerator("region", (1, 10)),
        ChildGenerator("battlefield", probability=10),
        ChildGenerator(".biome"),
    ]
    names_data = [
        ["country of "],
        ["Li","Arme","Le","Molda","Slove","Tur","Afgha","Alba","Alge","Tu","Fran","Baha","Su","Austra","Germa","In","Ara","Austri","Be","Ba","Bra","Ru","Chi","Ja","Tai","Bangla","Gha","Bou","Bo","Tas","Ze","Mon","Mo","Ne","Neder","Spai","Portu","Po","Por","Mol","Bul","Bru","Bur","Gro","Syl","Gui","Da","Gree","Bri","Ita"],
        ["ly","dania","mas","vania","ce","nea","nau","topia","garia","gal","laska","golia","nisia","land","snia","livia","mania","than","nin","pan","wan","zil","ssia","na","rein","lgium","bia","ny","ce","stan","distan","nistan","dan","lia","nia","via","sia","tia","key","desh","dia"]
    ]


class Region(Thing):
    child_generators = [
        ChildGenerator("capital"),
        ChildGenerator("city", (1, 10)),
        ChildGenerator("village", (2, 15)),
    ]
    names_data = [
        ["north ","east ","south ","west ","north-west ","north-east ","south-west ","south-east ","center ","oversea "],
        ["hilly","rainy","lush","foggy","desertic","green","tropical","rich","barren","scorched"],
        [" region"],
    ]


class City(Thing):
    child_generators = [
        ChildGenerator("monument", probability=15),
        ChildGenerator("monument", probability=5),
        ChildGenerator("residential area", (4, 9)),
        ChildGenerator("commercial area", (1, 5)),
        ChildGenerator("police station"),
        ChildGenerator("police station", probability=50),
        ChildGenerator("fire department"),
        ChildGenerator("fire department", probability=50),
        ChildGenerator("museum", probability=40),
        ChildGenerator("library", probability=60),
        ChildGenerator("hospital"),
        ChildGenerator("farm", (0, 3)),
        ChildGenerator("factory", (1, 4)),
        ChildGenerator("cemetery"),
        ChildGenerator("research facility", probability=2),
    ]
    names_data = "city"


class Village(City):
    child_generators = [
        ChildGenerator("residential area", (1, 4)),
        ChildGenerator("commercial area", probability=90),
        ChildGenerator("police station", probability=50),
        ChildGenerator("fire department", probability=40),
        ChildGenerator("museum", probability=5),
        ChildGenerator("library", probability=40),
        ChildGenerator("farm", (0, 6)),
        ChildGenerator("factory", (0, 2)),
        ChildGenerator("cemetery", probability=60),
        ChildGenerator("research facility", probability=4),
    ]
    names_data = "village"


class Capital(Thing):
    child_generators = [
        ChildGenerator("monument", probability=70),
        ChildGenerator("monument", probability=40),
        ChildGenerator("monument", probability=10),
        ChildGenerator("residential area", (7, 15)),
        ChildGenerator("commercial area", (3, 9)),
        ChildGenerator("police station", (2, 5)),
        ChildGenerator("fire department", (1, 3)),
        ChildGenerator("museum", (1, 2)),
        ChildGenerator("library", (1, 3)),
        ChildGenerator("hospital", (1, 3)),
        ChildGenerator("farm", (0, 2)),
        ChildGenerator("factory", (2, 6)),
        ChildGenerator("cemetery"),
        ChildGenerator("cemetery", probability=50),
        ChildGenerator("research facility", probability=1),
    ]
    names_data = "capital city"


class MedievalContinent(Continent):
    child_generators = [
        ChildGenerator("medieval land", (1, 6)),
        ChildGenerator("sea", (1, 5)),
    ]
    names_data = ["explored continent"]


class MedievalLand(Country):
    child_generators = [
        ChildGenerator("medieval region", (1, 10)),
        ChildGenerator("medieval battlefield", probability=10),
        ChildGenerator(".biome"),
    ]
    names_data = [
        ["realm","kingdom","empire","dominion"],
        [" of "],
        ["G","P","S","St","Sh","B","F","K","Z","Az","Oz"],
        ["","","","r","l"],
        ["u","o","a","e"],
        ["r","sh","nd","st","sd","kl","kt","pl","fr","ck","sh","ff","gg","l","lig","rag","sha","pta","lir","limd","lim","shim","stel"],
        ["i","u","o","oo","e","ee","y","a"],
        ["ll","th","h","k","lm","r","g","gh","n","m","p","s","rg","lg"],
    ]


class MedievalRegion(Region):
    child_generators = [
        ChildGenerator("medieval capital"),
        ChildGenerator("medieval village", (2, 6)),
        ChildGenerator("dungeon", probability=15),
        ChildGenerator("dungeon", probability=5),
    ]
    names_data = [
        ["hilly","rainy","lush","foggy","desertic","green","tropical","rich","barren","scorched"],
        [" "],
        ["shire","province","county","parish","pale"],
    ]


class MedievalVillage(Village):
    child_generators = [
        ChildGenerator("townwall", probability=20),
        ChildGenerator("watchtower", probability=15),
        ChildGenerator("medieval monument", probability=50),
        ChildGenerator("medieval residential area", (1, 4)),
        ChildGenerator("medieval commercial area", (1, 2)),
        ChildGenerator("medieval temple", (0, 2)),
        ChildGenerator("medieval farm", (4, 8)),
        ChildGenerator("medieval cemetery", probability=50),
        ChildGenerator("wizard tower", probability=5),
    ]
    names_data = "village"


class MedievalCapital(City):
    child_generators = [
        ChildGenerator("castle"),
        ChildGenerator("townwall"),
        ChildGenerator("medieval monument", probability=70),
        ChildGenerator("medieval monument", probability=20),
        ChildGenerator("medieval residential area", (3, 12)),
        ChildGenerator("medieval mage quarter", probability=50),
        ChildGenerator("medieval mage quarter", probability=20),
        ChildGenerator("medieval temple", (1, 3)),
        ChildGenerator("medieval commercial area", (2, 6)),
        ChildGenerator("medieval farm", (2, 6)),
        ChildGenerator("medieval cemetery"),
    ]
    names_data = [
        "stronghold",
        "fortress",
        "fort",
        "hold",
        "palace",
        "main city",
        "citadel",
    ]


class AncientContinent(Continent):
    child_generators = [
        ChildGenerator("ancient land", (1, 5)),
        ChildGenerator("sea", (1, 5)),
    ]
    names_data = ["continent"]


class AncientLand(Country):
    child_generators = [
        ChildGenerator("ancient plain", (0, 5)),
        [
            ChildGenerator("ancient forest", (0, 4)),
            ChildGenerator("ancient jungle", (0, 4)),
        ],
        ChildGenerator("mountain", (0, 3)),
    ]
    names_data = [
        ["hilly", "rainy", "lush", "foggy", "desertic", "green", "tropical", "rich", "barren", "scorched"],
        [" land"]
    ]


class FutureContinent(Continent):
    child_generators = [ChildGenerator("future city", (20, 50))]
    names_data = [
        ["united continent of "],
        ["Eu","A","O","E","Ca","Ma"],
        ["rt","lt","rm","t","tr","tl","str","s","m","fr"],
        ["a","o","e","i"],
        ["ri","ni","ti","fri","",""],
        ["sia","nia","ca"]
    ]
    # ["A","Eu","Ame","Ocea","Anta","Atla"],["frica","rtica","ropa","rica","nia","sia","ntide"]


class FutureCity(City):
    child_generators = [
        ChildGenerator("spaceport", (1, 3)),
        ChildGenerator("living center", (5, 20)),
        ChildGenerator("spending center", (5, 20)),
    ]
    names_data = "citadion"


class VisitorCity(City):
    child_generators = [
        ChildGenerator("named visitor", (0, 8)),
        [
            ChildGenerator("space animal", (0, 3)),
            ChildGenerator(),
        ],
        ChildGenerator("visitor neighborhood", (1, 8)),
    ]
    names_data = "visitor city"


# ChildGenerator("battlefield", probability=10),
# ChildGenerator("medieval battlefield", probability=10),
# ChildGenerator(".biome"),
# ChildGenerator("medieval capital"),
# ChildGenerator("medieval village", (2, 6)),
# ChildGenerator("dungeon", probability=15),
# ChildGenerator("ancient plain", (0, 5)),
# ChildGenerator("ancient forest", (0, 4)),
# ChildGenerator("ancient jungle", (0, 4)),
# ChildGenerator("mountain", (0, 3)),
# ChildGenerator("named visitor", (0, 8)),
# ChildGenerator("visitor neighborhood", (1, 8)),
# ChildGenerator("spaceport", (1, 3)),
# ChildGenerator("living center", (5, 20)),
# ChildGenerator("spending center", (5, 20)),


CONTENTS = [
    Continent,
    Country,
    Region,

    Village,
    City,
    Capital,

    MedievalContinent,
    MedievalLand,
    MedievalRegion,
    MedievalVillage,
    MedievalCapital,

    AncientContinent,
    AncientLand,

    FutureContinent,
    FutureCity,

    VisitorCity,
]