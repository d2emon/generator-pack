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


# buildings
# new Thing("monument",["tourist,5-30","souvenir shop,70%","souvenir shop,30%"],"*MONUMENT*");
# new Thing("tourist",[".person"],"*PERSON*| (tourist)");

# new Thing("commercial area",["street,1-5","bargain shop,60%","bargain shop,30%","souvenir shop,10%","fresh produce shop,60%","pet shop,60%","toy shop,60%","game shop,60%","office building,1-12"]);
# new Thing("office building",["building hall","office,6-20",".building"],[["a tall","a stout","an unimpressive","a large","a humongous","a modern","a classic","a historic","a gray","a dull","a white","a black","a concrete","a glass-covered","an impressive","a beautiful","an old-fashioned","a boring","a newly-built","a fancy"],[" "],["office building","skyscraper","building"]]);


class ResidentialArea(Thing):
    child_generators = [
        ChildGenerator("street", (1, 5)),
        ChildGenerator("house", (5, 20)),
        ChildGenerator("apartment building", (0, 5)),
    ]


class Building(Thing):
    child_generators = [
        ChildGenerator("walls"),
        ChildGenerator("roof"),
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


# rooms


# new Thing("roof",["cat,2%","bird,10%","bird,10%","nest,2%","roof tiles"]);
# new Thing("roof tiles",["ceramic"],"tiles");


class Room(Thing):
    child_generators = [
        ChildGenerator("visitor", probability=0.1),
        ChildGenerator("ghost", probability=0.1),
        ChildGenerator("walls"),
    ]


# new Thing("walls",["door,1-4","window,0-6",["wall,4","wall,4-8"]]);
# new Thing("wall",[["plaster","wood"],"dirt,5%"]);
# new Thing("plaster",["calcium","sulfur"]);
# new Thing("marble",["calcium"]);
# new Thing("stone",["rock"]);
# new Thing("concrete",["rock","cement","water"]);
# new Thing("cement",["calcium"]);
# new Thing("marble",["calcium"]);
# new Thing("door",["wood frame","glass,10%"]);
# new Thing("window",["wood frame","glass"]);
# new Thing("living-room",[".room","person,0-4","cat,10%","cat,10%","stuff box,5%","tv,95%","armchair,50%","armchair,50%","couch,90%","living-room table,50%","chair,1-6","painting,70%","painting,20%","mirror,2%","bookshelf,0-3","small bookshelf,0-2","desk,40%","computer,40%"]);
# new Thing("kitchen",[".room","person,40%","person,20%","tv,40%","kitchen sink","cabinet,1-5","fridge","oven","chair,0-3","computer,5%","small bookshelf,5%","painting,30%","painting,10%"]);


class Bedroom(Room):
    child_generators = [
        ChildGenerator(".room"),
        ChildGenerator("person", probability=40),
        ChildGenerator("person", probability=10),
        ChildGenerator("cat", probability=5),
        ChildGenerator("stuff box", probability=5),
        ChildGenerator("tv", probability=60),
        ChildGenerator("bed"),
        ChildGenerator("chair", (0, 4)),
        [
            ChildGenerator("cupboard", probability=90),
            ChildGenerator("closet", probability=90),
        ],
        ChildGenerator("mirror", probability=50),
        ChildGenerator("bookshelf", (0, 2)),
        ChildGenerator("small bookshelf", (0, 3)),
        ChildGenerator("desk", probability=40),
        ChildGenerator("computer", probability=40),
        ChildGenerator("painting", probability=60),
        ChildGenerator("painting", probability=20),
    ]


class Bathroom(Room):
    child_generators = [
        ChildGenerator(".room"),
        ChildGenerator("person", probability=10),
        ChildGenerator("person", probability=1),
        ChildGenerator("cat", probability=1),
        ChildGenerator("sink", probability=95),
        [
            ChildGenerator("bathtub"),
            ChildGenerator("shower")
        ],
        ChildGenerator("toilet"),
        ChildGenerator("painting", probability=20),
        ChildGenerator("mirror", probability=80),
    ]


# new Thing("study",[".room","person,30%","person,5%","stuff box,20%","tv,20%","desk,95%","computer,90%","chair,1-4","bookshelf,0-6","painting,70%","painting,20%","mirror,5%"]);
# new Thing("garden",["person,40%","person,10%","dog,20%","dog,5%","cat,15%","grass","tree,50%","tree,50%","tree,20%","tree,5%","flowers,30%","hole,1%","hole,1%","hole,1%","poultry,1%","bird,20%","bird,10%"],["garden","lawn","backyard"]);
# new Thing("garage",["person,20%","cat,2%","stuff box,30%","stuff box,20%","chair,0-3","car,90%","car,40%","car,5%","bike,40%","bike,30%","bike,10%","computer,5%","small bookshelf,30%","hole,1%","hole,0.5%","small mammal,5%","insect,15%","insect,15%","dirt,50%"]);
# new Thing("hole",["corpse,20%","corpse,5%","blood,20%","shovel,20%","hole,0.5%","insect,25%","insect,15%","dirt"]);


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


# new Thing("castle",["medieval peasant,1-4","medieval noble,0-2","medieval guard,2-8","castle keep","giant monster cage,1%","watchtower,1-6","medieval temple,30%","medieval inn,40%","medieval house,1-4","medieval monument,70%","medieval monument,20%","moat,30%","gatehouse","medieval wall"]);
# new Thing("gatehouse",["medieval guard,1-3","portcullis,1-2","wood","medieval wall"]);
# new Thing("portcullis",["wood","metal"]);
# new Thing("moat",["water,50%","dirt"]);
# new Thing("medieval monument",[["stone","marble"]],["fountain","memorial","statue","well","altar"]);
# new Thing("townwall",["medieval guard,1-8","watchtower,1-6","medieval wall"]);
# new Thing("watchtower",["medieval guard,1-2","medieval chest,30%",".medieval building"]);
# new Thing("castle keep",["great hall","noble medieval living quarters,1-3","noble medieval bedroom,2-5",".medieval building"]);
# new Thing("great hall",["medieval king,90%","medieval queen,90%","throne,2","wizard,0-3","medieval noble,1-6","medieval guard,1-4","medieval servant,1-4","medieval table","medieval table,60%","medieval chair,3-8","medieval chest,1-4","medieval clutter,0-4","medieval meat,30%","sack of medieval food,0-2","medieval food,0-2","sack of grain,50%","medieval fireplace","medieval fireplace,50%","dog,60%","dog,30%","cat,30%",".medieval room"],"throne room");


class MedievalResidentialArea(ResidentialArea):
    child_generators = [ChildGenerator("medieval house", (3, 8))]
    names_data = ["housing district"]


# new Thing("medieval commercial area",["medieval inn,1-2","medieval armor shop,0-2","medieval tool shop,0-2","medieval clothing shop,0-2","medieval butcher shop,0-2","medieval food shop,0-2","medieval apothecary shop,0-2"],"trade district");
# new Thing("medieval mage quarter",["wizard tower,1-5","medieval inn,0-1","medieval apothecary shop,0-3"],"mage district");


class MedievalBuilding(Building):
    child_generators = [
        ChildGenerator("medieval walls"),
        ChildGenerator("roof"),
    ]
    names_data = ["building"]


class MedievalHouse(MedievalBuilding):
    child_generators = [
        ChildGenerator("medieval living quarters"),
        ChildGenerator("medieval bedroom"),
        ChildGenerator("medieval bedroom", probability=50),
        ChildGenerator(".medieval building"),
    ]
    names_data = [
        ["a small","a large","a big","a cozy","a bland","a boring","an old","a new","a freshly-painted","a pretty",
         "an old-fashioned","a creepy","a spooky","a gloomy","a tall","a tiny","a fine","a happy little"],
        [" hovel"]
    ]


class MedievalRoom(Thing):
    child_generators = [
        ChildGenerator("visitor", probability=0.1),
        ChildGenerator("ghost", probability=0.1),
        ChildGenerator("medieval walls"),
    ]
    names_data = [
        "room",
    ]


# new Thing("medieval walls",["door,1-4","window,0-6",["medieval wall,4","medieval wall,4-8"]],"stone walls");
# new Thing("medieval wall",["wood","stone","dirt,20%"],"stone wall");


class MedievalLivingQuarters(MedievalRoom):
    child_generators = [
        ChildGenerator("medieval peasant", (0, 4)),
        ChildGenerator("medieval pantry"),
        ChildGenerator("medieval table"),
        ChildGenerator("medieval table", probability=30),
        ChildGenerator("medieval chair", (1, 6)),
        ChildGenerator("medieval chest", (0, 3)),
        ChildGenerator("medieval clutter", (0, 2)),
        ChildGenerator("medieval meat", probability=30),
        ChildGenerator("sack of medieval food", (0, 2)),
        ChildGenerator("medieval food", (0, 2)),
        ChildGenerator("sack of grain", probability=50),
        ChildGenerator("medieval fireplace", probability=90),
        ChildGenerator("dog", probability=60),
        ChildGenerator("dog", probability=30),
        ChildGenerator("cat", probability=30),
        ChildGenerator("poultry", probability=10),
        ChildGenerator("insect", probability=70),
        ChildGenerator("insect", probability=40),
        ChildGenerator(".medieval room"),
    ]
    names_data = [
        "living quarters",
    ]


class MedievalBedroom(MedievalRoom):
    child_generators = [
        ChildGenerator("medieval peasant", (0, 2)),
        ChildGenerator("medieval bed"),
        ChildGenerator("medieval bed", probability=20),
        ChildGenerator("medieval table", probability=30),
        ChildGenerator("medieval chair", (0, 4)),
        ChildGenerator("medieval chest", (0, 2)),
        ChildGenerator("medieval clutter", (0, 2)),
        ChildGenerator("medieval fireplace", probability=40),
        ChildGenerator("dog", probability=10),
        ChildGenerator("dog", probability=10),
        ChildGenerator("cat", probability=20),
        ChildGenerator("insect", probability=70),
        ChildGenerator("insect", probability=40),
        ChildGenerator(".medieval room"),
    ]
    names_data = ["bedroom"]


# new Thing("medieval pantry",["medieval peasant,10%","medieval meat,0-4","sack of medieval food,0-8","medieval food,0-8","sack of grain,0-6","ale keg,0-3","medieval chest,0-2","medieval clutter,0-2","insect,0-4",".medieval room"],"pantry");
# new Thing("noble medieval living quarters",["wizard,10%","medieval noble,0-4","medieval servant,0-3","medieval pantry,0-2","medieval table","medieval table,60%","medieval chair,1-8","medieval chest,1-4","medieval clutter,0-4","medieval meat,30%","sack of medieval food,0-2","medieval food,0-2","sack of grain,50%","medieval fireplace","medieval fireplace,50%","dog,60%","dog,30%","cat,30%",".medieval room"],"living quarters");
# new Thing("noble medieval bedroom",["medieval noble,0-2","medieval servant,0-2","medieval bed","medieval bed,20%","medieval table,50%","medieval chair,0-4","medieval chest,1-3","medieval clutter,0-3","medieval fireplace,80%","dog,10%","dog,10%","cat,20%",".medieval room"],"bedroom");
# new Thing("medieval fireplace",["fire","ash","wood","stone"],"fireplace");
# new Thing("medieval temple",["medieval priest,1-3","medieval noble,0-2","medieval peasant,0-4","medieval altar,1-2","medieval table,70%","medieval bench,2-6","medieval chair,1-3","medieval chest,1-4","medieval clutter,0-4","medieval fireplace,20%",".medieval room"],[["temple of the","church of the","chapel of the","house of the","abbey of the","cathedral of the","shrine of the","sanctuary of the","priory of the"],[" "],["blinding","sacred","holy","unholy","bloody","cursed","marvellous","wondrous","pious","miraculous","endless","unending","undying","infinite","unworldly","worldly","divine","demonic","ghostly","monstrous","tentacled","all-knowing","rational","pretty good","vengeful","hallowed"],[" "],["light","star","beam","sphere","goddess","god","lords","sisterhood","brotherhood","skies","pact","sect","harmony","discord","child","entity","ghost","builders","makers","guide","wit","story","tale","unicorn","flame","fountain","locust","squid","gembaby","father","mother"]]);
# new Thing("giant monster cage",[["dragon","sea monster"]],"giant cage");


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
# new Thing("future gizmo",["nanoplasm"],[["trans","nano","micro","tele","sprowse","corvo","mega","multi","aqua","mind","brain","body","nutri","auto","laser"],["ponder","glasses","phone","watch","phraser","gizmo","matic","morpher","torch","pass","dex","pedia","guide","twister","key","limb"]]);


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

    ResidentialArea,
    House,
    Apartment,
    ApartmentBuilding,

    Building,

    Room,

    Bedroom,
    Bathroom,

    MedievalContinent,
    MedievalLand,
    MedievalRegion,
    MedievalVillage,
    MedievalCapital,

    MedievalResidentialArea,

    MedievalHouse,
    MedievalBuilding,
    MedievalRoom,

    MedievalLivingQuarters,
    MedievalBedroom,

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