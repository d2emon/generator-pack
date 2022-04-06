from genesys.nested.child_generator import ChildGenerator
from genesys.nested.factories.thing_factory import Factory as Thing

from models.v5.nested_v2.models import Biome
from genesys.nested.data.unprocessed.room import Building


class Continent(Thing):
    child_generators = [
        ChildGenerator("country", (1, 10)),
        ChildGenerator("sea", (1, 5)),
    ]
    names_data = [
        ["continent of "],
        ["A", "Eu", "Ame", "Ocea", "Anta", "Atla"],
        ["frica", "rtica", "ropa", "rica", "nia", "sia", "ntide"],
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


class Country(Biome):
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


# buildings
class Monument(Thing):
    child_generators = [
        ChildGenerator("tourist", (5, 30)),
        ChildGenerator("souvenir shop", probability=70),
        ChildGenerator("souvenir shop", probability=30),
    ]
    names_data = "*MONUMENT*"


class CommercialArea(Thing):
    child_generators = [
        ChildGenerator("street", (1, 5)),
        ChildGenerator("bargain shop", probability=60),
        ChildGenerator("bargain shop", probability=30),
        ChildGenerator("souvenir shop", probability=10),
        ChildGenerator("fresh produce shop", probability=60),
        ChildGenerator("pet shop", probability=60),
        ChildGenerator("toy shop", probability=60),
        ChildGenerator("game shop", probability=60),
        ChildGenerator("office building", (1, 12)),
    ]


class ResidentialArea(Thing):
    child_generators = [
        ChildGenerator("street", (1, 5)),
        ChildGenerator("house", (5, 20)),
        ChildGenerator("apartment building", (0, 5)),
    ]


class OfficeBuilding(Building):
    child_generators = [
        ChildGenerator("building hall"),
        ChildGenerator("office", (6, 20)),
        ChildGenerator(".building")
    ]
    names_data = [
        [
            "a tall", "a stout", "an unimpressive", "a large", "a humongous", "a modern", "a classic", "a historic",
            "a gray", "a dull", "a white", "a black", "a concrete", "a glass-covered", "an impressive", "a beautiful",
            "an old-fashioned", "a boring", "a newly-built", "a fancy"
        ],
        [" "],
        ["office building", "skyscraper", "building"]
    ]


class House(Building):
    child_generators = [
        ChildGenerator("fire", probability=0.3),
        ChildGenerator("living-room"),
        ChildGenerator("kitchen"),
        ChildGenerator("bathroom", (1, 3)),
        ChildGenerator("bedroom", (2, 5)),
        ChildGenerator("attic"),
        ChildGenerator("study", (0, 2)),
        ChildGenerator("garden", probability=90),
        ChildGenerator("garage", probability=90),
        ChildGenerator(".building"),
    ]
    names_data = [
        ["a small", "a large", "a big", "a cozy", "a bland", "a boring", "an old", "a new", "a freshly-painted",
         "a pretty", "an old-fashioned", "a creepy", "a spooky", "a gloomy", "a tall", "a tiny", "a fine",
         "a happy little"],
        [" pink", " grey", " green", " yellow", " orange", " red", "blue", " white", " brick", " stone", " wooden",
         "", "", ""],
        [" house"]
    ]


class Apartment(Thing):
    child_generators = [
        ChildGenerator("living-room", probability=90),
        ChildGenerator("kitchen"),
        ChildGenerator("bathroom", (1, )),
        ChildGenerator("bedroom", (1, 3)),
        ChildGenerator("study", probability=20),
    ]


class ApartmentBuilding(Building):
    child_generators = [
        ChildGenerator("fire", probability=0.3),
        ChildGenerator("apartment", (6, 20)),
        ChildGenerator(".building"),
    ]


# farms
class Farm(Thing):
    child_generators = [
        ChildGenerator("fire", probability=0.3),
        ChildGenerator("house", (1, 3)),
        ChildGenerator("farmer", (1, 4)),
        ChildGenerator("field", (1, 8)),
        ChildGenerator("horse", probability=30),
        ChildGenerator("horse", probability=30),
        ChildGenerator("horse", probability=30),
        ChildGenerator("poultry", (0, 3)),
        ChildGenerator("grain silo", (0, 2)),
        ChildGenerator("barn", (0, 2)),
        ChildGenerator("warehouse", (0, 2)),
        ChildGenerator("storage shed", (0, 2))
    ]


# new Thing("field",["grain","insect,5%","bird,10%","bird,5%","haystack,30%"],["wheat field","corn field","soy field","rice field","oat field","peanut field","tomato field","grape field","barley field","canola field","rye field","flower field"]);
# new Thing("farmer",[".person"],"*PERSON*| (farmer)");
# new Thing("grain",["plant cell"]);
# new Thing("grain silo",["metal","grain"]);
# new Thing("warehouse",["worker,0-2","small mammal,8%","ghost,0.3%","machine,0-4",".building"]);
# new Thing("barn",[".building"]);
# new Thing("storage shed",[".building"]);
# new Thing("haystack",["grain","insect,10%","needle,0.1%"]);
# new Thing("needle",["metal"]);

# new Thing("factory",["worker,2-12","machine,1-12","pipes,40%","cables,0-1","public bathroom,60%","warehouse,0-2",".building"],[["toy","chocolate","car","yoghurt","processed food","pork products","canned beef","juice","soda","shoe","textile","computer","weapon","hardware"],[" factory"]]);
# new Thing("worker",[".person"],"*PERSON*| (worker)");

# new Thing("public bathroom",[".room","person,10%","person,1%","sink,1-4","toilet,1-4","mirror,0-3"],"restroom");


# services
class FireDepartment(Building):
    child_generators = [
        ChildGenerator("fire", probability=0.2),
        ChildGenerator("firefighter", (3, 6)),
        ChildGenerator("desk", (0, 3)),
        ChildGenerator("chair", (1, 4)),
        ChildGenerator("fridge", probability=60),
        ChildGenerator("tv", probability=60),
        ChildGenerator("fire truck"),
        ChildGenerator(".building")
    ]


# new Thing("firefighter",[".person"],"*PERSON*| (firefighter)");


class PoliceStation(Building):
    child_generators = [
        ChildGenerator("police officer", (2, 6)),
        ChildGenerator("desk", (0, 2)),
        ChildGenerator("tv", probability=40),
        ChildGenerator("small bookshelf", (0, 2)),
        ChildGenerator("chair", (0, 4)),
        ChildGenerator(".building")
    ]


# new Thing("police officer",[".person"],"*PERSON*| (police officer)");


class Library(Building):
    child_generators = [
        ChildGenerator("bookshelf", (10, 30)),
        ChildGenerator("painting", probability=50),
        ChildGenerator("painting", probability=50),
        ChildGenerator("painting", probability=50),
        ChildGenerator("desk", (0, 4)),
        ChildGenerator("computer", (0, 4)),
        ChildGenerator("chair", (0, 4)),
        ChildGenerator("librarian", (1, 4)),
        ChildGenerator("person", (0, 12)),
        ChildGenerator(".building"),
    ]


# new Thing("librarian",[".person"],"*PERSON*| (librarian)");


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
        ["Eu", "A", "O", "E", "Ca", "Ma"],
        ["rt", "lt", "rm", "t", "tr", "tl", "str", "s", "m", "fr"],
        ["a", "o", "e", "i"],
        ["ri", "ni", "ti", "fri", "", ""],
        ["sia", "nia", "ca"]
    ]
    # ["A","Eu","Ame","Ocea","Anta","Atla"],["frica","rtica","ropa","rica","nia","sia","ntide"]


class FutureCity(City):
    child_generators = [
        ChildGenerator("spaceport", (1, 3)),
        ChildGenerator("living center", (5, 20)),
        ChildGenerator("spending center", (5, 20)),
    ]
    names_data = "citadion"


class LivingCenter(ResidentialArea):
    child_generators = [ChildGenerator("future building", (20, 30))]


# new Thing("spaceport", ["sprowseship,4-12", "future person,6-20", "future commercial building,2-6"]);
# new Thing("spending center", ["future commercial building,20-30"]);


# new Thing("nanojuice",[".nanostuff"]);
# new Thing("food pill",["nanojuice"],[["plum","coconut","sirloin steak","roastbeef","mint","banana","lime","grape","cat","guinea pig","pineapple","apple","yoghurt","salmon","purple","blue","pink","green","smoke","toothpaste","chocolate","vanilla","biscuit","bread","onion","pinecone","shrimp","turkey","jellyfish","raspberry cake","grass","glass","pain","flavor","pill","food","mouth","water","air","old","internet","video game","egg","ham","people","clam","disappointment","friendship"],["-flavored pill"]]);
# new Thing("nanobrick",[".nanostuff"]);
# new Thing("nanopipe",[".nanostuff"]);
# new Thing("nanocarpet",[".nanostuff"]);
# new Thing("nanobookshelf",["book,2-20","nanoplasm"]);
# new Thing("nanocupboard",["future outfit,0-6","future hat,0-4","nanoplasm"]);


class FutureBathroomStuff(Thing):
    child_generators = [
        ChildGenerator("water"),
        ChildGenerator("nanoplasm"),
        ChildGenerator("nanopipe", (1, 2)),
    ]
    names_data = ["bathtub", "toilet", "sink", "shower", "scrubber", "steamomatic", "steamheater"]


# new Thing("future living-room stuff",["nanoplasm"],["chair","armchair","couch","table","shelf","lamp","endtable"]);


class FutureBedroomStuff(Thing):
    child_generators = [
        ChildGenerator("nanoplasm"),
    ]
    names_data = ["bed", "chair", "desk", "lamp", "endtable"]


# new Thing("future decoration stuff",["nanoplasm"],["potted plant","rug","statue","lamp","glowlamp","ceiling lamp"]);
# new Thing("future gizmo",["nanoplasm"],[["trans","nano","micro","tele","sprowse","corvo","mega","multi","aqua","mind","mind","body","nutri","auto","laser"],["ponder","glasses","phone","watch","phraser","gizmo","matic","morpher","torch","pass","dex","pedia","guide","twister","key","limb"]]);


class FutureBuilding(Building):
    child_generators = [ChildGenerator("future home room", (1, 4))]
    names_data = ["home dome"]


# new Thing("future tv",["tv show","nanoplasm"],["wallscreen","microscreen","glowscreen","floorscreen","ceilingscreen","windowscreen"]);


class FutureRoom(Thing):
    child_generators = [
        ChildGenerator("future door", (1, 2)),
        ChildGenerator("nanocarpet"),
        ChildGenerator("future wall", (4, )),
    ]
    names_data = "room"


class FutureHomeRoom(FutureRoom):
    child_generators = [
        ChildGenerator("future person", (0, 3)),
        ChildGenerator("cat", probability=2),
        ChildGenerator("dog", probability=2),
        ChildGenerator("future gizmo", probability=20),
        ChildGenerator("future gizmo", probability=20),
        ChildGenerator("future tv", probability=40),
        ChildGenerator("future tv", probability=40),
        ChildGenerator("future tv", probability=20),
        [
            ChildGenerator("future bathroom stuff", (2, 4)),
            ChildGenerator("future living-room stuff", (3, 7)),
            ChildGenerator("future bedroom stuff", (2, 6)),
        ],
        ChildGenerator("future decoration stuff", (0, 3)),
        ChildGenerator(".future room"),
    ]
    names_data = ["room"]


# new Thing("future wall",["nanopipe,0-2","nanobrick,10-20"],"wall");
# new Thing("future door",["nanoplasm"],"door");
# new Thing("pill rack",["food pill,10-25","nanoplasm"]);
# new Thing("future food room",["pill rack,4-12","future person,1-6",".future room"],"pill store");
# new Thing("future goods room",[["nanocupboard,2-6","future bathroom stuff,4-12","future living-room stuff,4-12","future bedroom stuff,4-12","future decoration stuff,4-12","future gizmo,4-12","future tv,3-8","nanobookshelf,4-12"],"future person,1-6",".future room"],["furniture store","interior store","accessory store","stuff store"]);
# new Thing("future commercial building",[["future food room,1-6","future goods room,1-6"]],[["blobb","blubb","glorb","glob","mechat","transmogr","flumox","flapp","flubb","steam","plasm","plast","nan","gramm","sprows"],["oid","iffic","astic","eristic","y","ies","otronic","etical","arium","eteria"],[" "],["united","customization","education","megastore","megashop","understore","bodyware","augmentations","tasteful wares","entertainment","domotics","home improvement","incorporated","emporium","public","& co.","things and stuff","stuff","things","edible gizmos","essentials","nanobotics","all sizes and shapes","all shapes all colors","for all ages","for fun and enrichment","center","globular"]]);



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

# ChildGenerator("museum", probability=40),
# ChildGenerator("hospital"),
# ChildGenerator("farm", (0, 3)),
# ChildGenerator("factory", (1, 4)),
# ChildGenerator("cemetery"),
# ChildGenerator("research facility", probability=2),
# ChildGenerator("souvenir shop", probability=70),
# ChildGenerator("street", (1, 5)),
# "bargain shop,30%",
# "fresh produce shop,60%",
# "pet shop,60%",
# "toy shop,60%",
# "game shop,60%",

# ChildGenerator("fire", probability=0.3),
# ChildGenerator("living-room"),
# ChildGenerator("kitchen"),
# ChildGenerator("attic"),
# ChildGenerator("study", (0, 2)),
# ChildGenerator("garden", probability=90),
# ChildGenerator("garage", probability=90),
# ChildGenerator("visitor", probability=0.1),
# ChildGenerator("ghost", probability=0.1),
# ChildGenerator("wood")
# ChildGenerator("dirt", probability=5),
# ChildGenerator("calcium"),
# ChildGenerator("wood frame"),
# ChildGenerator("glass"),
# ChildGenerator("cat", probability=5),
# ChildGenerator("bird", probability=10),
# ChildGenerator("nest", probability=2),
# ChildGenerator("stuff box", probability=5),
# ChildGenerator("tv", probability=60),
# ChildGenerator("bed"),
# ChildGenerator("chair", (0, 4)),
# ChildGenerator("cupboard", probability=90),
# ChildGenerator("closet", probability=90),
# ChildGenerator("mirror", probability=50),
# ChildGenerator("bookshelf", (0, 2)),
# ChildGenerator("small bookshelf", (0, 3)),
# ChildGenerator("desk", probability=40),
# ChildGenerator("computer", probability=40),
# ChildGenerator("painting", probability=60),
# ChildGenerator("sink", probability=95),
# ChildGenerator("bathtub"),
# ChildGenerator("shower")
# ChildGenerator("toilet"),

# ChildGenerator("medieval battlefield", probability=10),
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

    Monument,

    ResidentialArea,
    CommercialArea,
    OfficeBuilding,
    House,
    Apartment,
    ApartmentBuilding,

    Farm,

    Building,

    FireDepartment,

    PoliceStation,

    Library,

    AncientContinent,
    AncientLand,

    FutureContinent,
    FutureCity,

    LivingCenter,

    FutureBathroomStuff,

    FutureBedroomStuff,

    FutureBuilding,

    FutureRoom,
    FutureHomeRoom,

    VisitorCity,
]