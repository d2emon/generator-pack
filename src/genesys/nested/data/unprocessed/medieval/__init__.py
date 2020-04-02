from genesys.nested.factories import Thing

from genesys.nested.data.unprocessed.state import Continent, Country, Region, City, Village, ResidentialArea, Building

from .person import CONTENTS as PERSON_CONTENTS


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


CONTENTS = [
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
] + PERSON_CONTENTS