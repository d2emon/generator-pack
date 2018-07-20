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


# ChildGenerator("ancient land", (1, 5)),
# ChildGenerator("future city", (20, 50))
# ChildGenerator("battlefield", probability=10),
# ChildGenerator("medieval battlefield", probability=10),
# ChildGenerator(".biome"),
# ChildGenerator("capital"),
# ChildGenerator("city", (1, 10)),
# ChildGenerator("village", (2, 15)),
# ChildGenerator("medieval capital"),
# ChildGenerator("medieval village", (2, 6)),
# ChildGenerator("dungeon", probability=15),
# ChildGenerator("ancient plain", (0, 5)),
# ChildGenerator("ancient forest", (0, 4)),
# ChildGenerator("ancient jungle", (0, 4)),
# ChildGenerator("mountain", (0, 3)),


CONTENTS = [
    Continent,
    Country,
    Region,

    MedievalContinent,
    MedievalLand,
    MedievalRegion,

    AncientContinent,
    AncientLand,

    FutureContinent,
]