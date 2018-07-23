from ..thing import Thing
from ..children import ChildGenerator


class ClothingSet(Thing):
    child_generators = [
        ChildGenerator("hat", probability=2),
        ChildGenerator("glasses", probability=20),
        ChildGenerator("pants", probability=98),
        ChildGenerator("shirt", probability=98),
        ChildGenerator("coat", probability=50),
        ChildGenerator("socks", probability=80),
        ChildGenerator("shoes", probability=80),
        ChildGenerator("underwear", probability=99)
    ]
    names_data = "clothing"


# new Thing("man",[".person"],"*MAN*");
# new Thing("woman",[".person"],"*WOMAN*");


class Person(Thing):
    child_generators = [
        ChildGenerator("body"),
        ChildGenerator("psyche"),
        ChildGenerator("clothing set"),
    ]
    names_data = ["*PERSON*"]


# new Thing("corpse",["body","clothing set","blood,35%","worm,20%","worm,10%"],"*PERSON*| (dead)");


class Body(Thing):
    child_generators = [
        ChildGenerator("head"),
        ChildGenerator("torso"),
        ChildGenerator("arm", probability=99),
        ChildGenerator("arm", probability=99),
        ChildGenerator("leg", probability=99),
        ChildGenerator("leg", probability=99),
    ]
    names_data = "body"


class Torso(Thing):
    child_generators = [
        ChildGenerator("chest"),
        ChildGenerator("pelvis"),
        ChildGenerator(".body part"),
    ]


class Chest(Thing):
    child_generators = [
        ChildGenerator("nipple", (2, )),
        ChildGenerator("bellybutton"),
        ChildGenerator(".body part"),
    ]


# new Thing("bellybutton",["skin","lint,0-1"]);
# new Thing("nipple",["skin"]);


class Pelvis(Thing):
    child_generators = [
        ChildGenerator("naughty bits"),
        ChildGenerator("butt"),
        ChildGenerator(".body part"),
    ]


# new Thing("naughty bits",[".soft body part"]);
# new Thing("butt",["pasta,0.01%","sweat,50%",".body part"]);
# new Thing("arm",["hand","elbow","armpit",".body part"],"arm");
# new Thing("hand",["finger,5",".body part"]);
# new Thing("finger",["fingernail",".body part"],"finger");
# new Thing("fingernail",["dust,30%","keratin"],"fingernail");
# new Thing("elbow",[".body part"]);
# new Thing("armpit",["armpit hair","sweat,80%",".soft body part"]);
# new Thing("armpit hair",[".hair"],"hair");
# new Thing("leg",["foot","knee",".body part"],"leg");
# new Thing("foot",["toe,5","sweat,30%",".body part"]);
# new Thing("toe",["toenail",".body part"],"toe");
# new Thing("toenail",["dust,40%","keratin"],"toenail");
# new Thing("knee",[".body part"],"knee");


class Head(Thing):
    child_generators = [
        ChildGenerator("mouth"),
        ChildGenerator("nose"),
        ChildGenerator("eye", probability=99),
        ChildGenerator("eye", probability=99),
        ChildGenerator("ear", (2, )),
        ChildGenerator("skull"),
        ChildGenerator("head hair", probability=85),
        ChildGenerator(".body part"),
    ]
    names_data = "head"


# new Thing("eye",["eyelashes","eye flesh","tear,2%"],"eye");
# new Thing("eye flesh",["water","blood vessels","fat"],"eyeball");
# new Thing("eyelashes",[".hair"],"eyelashes");
# new Thing("tear",["water","salt"]);
# new Thing("ear",[".soft body part"],"ear");
# new Thing("brain",["bacteria,20%","brain cell"],"brain");
# new Thing("skull",["brain",".bones"]);
# new Thing("head hair",[".hair","dandruff,10%"],[["brown","black","gray","light","blonde","red","dark"],[" hair"]]);
# new Thing("hair",["bacteria,30%","keratin"],"hair");
# new Thing("nose",["nostril,2",".body part"],"nose");
# new Thing("nostril",["nostril hair","boogers,0-1",".soft body part"],"nostril");
# new Thing("nostril hair",[".hair"],"nostril hair");
# new Thing("boogers",["organic matter"]);
# new Thing("mouth",["teeth","tongue"],"mouth");
# new Thing("teeth",["calcium","phosphorus"],"teeth");
# new Thing("tongue",["muscles"],"tongue");


# medieval people
class MedievalClothingSet(ClothingSet):
    child_generators = [
        ChildGenerator("medieval hat", probability=30),
        ChildGenerator("medieval pants", probability=98),
        ChildGenerator("medieval shirt", probability=98),
        ChildGenerator("medieval coat", probability=50),
        ChildGenerator("medieval shoes", probability=80),
        ChildGenerator("medieval underwear", probability=99),
    ]
    names_data = ["clothing"]


# new Thing("medieval man",[".medieval person"],"*MEDIEVAL MAN*");
# new Thing("medieval woman",[".medieval person"],"*MEDIEVAL WOMAN*");


class MedievalPerson(Person):
    child_generators = [
        ChildGenerator("body"),
        ChildGenerator("medieval psyche"),
        ChildGenerator("medieval clothing set"),
    ]
    names_data = ["*MEDIEVAL PERSON*"]


# new Thing("medieval psyche",["medieval thoughts","medieval memories"],"psyche");
# new Thing("medieval thoughts",["black hole,0.01%",["medieval thought,2-3"]],"thoughts");
# new Thing("medieval thought",[],["*MEDIEVAL THOUGHT*"]);
# new Thing("medieval memories",["medieval memory,2-4"],"memories");
# new Thing("medieval memory",[],["*MEDIEVAL MEMORY*"]);

# new Thing("medieval clothing",[["leather","cloth"]],["clothing"]);
# new Thing("medieval pants",[".medieval clothing"],["pants"]);
# new Thing("medieval shirt",[".medieval clothing"],["shirt"]);
# new Thing("medieval underwear",[".medieval clothing"],["underwear"]);
# new Thing("medieval coat",[".medieval clothing"],["coat","cloak","cape","robe","mantle"]);
# new Thing("medieval shoes",["leather,50%","wood"],["shoes","clogs"]);
# new Thing("medieval hat",[".medieval clothing"],["hat","hood","headdress"]);
# new Thing("armor",["metal"],["chain-mail armor","plate armor","lamellar armor","scale armor","brigandine","cuirass","gauntlets","pauldrons","spaulders","vambraces","greaves"]);
# new Thing("helmet",["metal"],["helm","helmet"]);
# new Thing("medieval weapon",["metal","wood"],["sword","longsword","rapier","bow","shortbow","longbow","crossbow","mace","spear","dagger","pole axe","knife","halberd","axe","javelin","hatchet","battleaxe","warhammer","maul","staff","harpoon","scimitar","cleaver","morningstar","club"]);


class MedievalPeasant(MedievalPerson):
    child_generators = [ChildGenerator(".medieval person"),]
    names_data = ["*MEDIEVAL PERSON*| (peasant)"]


# new Thing("medieval priest",[".medieval person"],"*MEDIEVAL PERSON*| (priest)");
# new Thing("medieval servant",[".medieval person"],"*MEDIEVAL PERSON*| (servant)");
# new Thing("medieval noble",[".medieval person"],"*MEDIEVAL PERSON*| (noble)");
# new Thing("medieval guard",[".medieval person"],"*MEDIEVAL PERSON*| (guard)");
# new Thing("medieval shopkeeper",[".medieval person"],"*MEDIEVAL PERSON*| (shopkeeper)");
# new Thing("medieval innkeeper",[".medieval person"],"*MEDIEVAL PERSON*| (innkeeper)");
# new Thing("medieval king",[".medieval person"],[["*MEDIEVAL MAN*| ("],["king","emperor","prince"],[")"]]);
# new Thing("medieval queen",[".medieval person"],[["*MEDIEVAL WOMAN*| ("],["queen","empress","princess"],[")"]]);
# new Thing("wizard",[".medieval person"],[["*MEDIEVAL PERSON*| ("],["court","battle","rogue","corrupt","druid","bard","adept","thaumaturgist","shaman","healing","ice","frost","snow","arcane","lightning","thunder","earth","earthquake","nature","animal","shape-shifting","death","undeath","spark","fire","lava","locust","poison","rainbow","mist","fog","dust","air","wind","cloud","tornado","shark","punch","kick","song","skeleton","psycho","illusion","flying","summoner","thief","barbarian","dragon","gem","sky","star","dark","paladin","luck","time","space","blade"],[" "],["mage","magician","wizard"],[")"]]);
# new Thing("medieval gravedigger",[".medieval person","shovel,30%"],"*MEDIEVAL PERSON*| (gravedigger)");
# new Thing("medieval corpse",["body","medieval clothing set","blood,35%","worm,20%","worm,10%"],"*MEDIEVAL PERSON*| (dead)");


# future stuff


class FutureClothingSet(ClothingSet):
    child_generators = [
        ChildGenerator("future gizmo", probability=10),
        ChildGenerator("future gizmo", probability=10),
        ChildGenerator("future gizmo", probability=10),
        ChildGenerator("future hat", probability=10),
        ChildGenerator("future outfit", probability=99.8),
    ]
    names_data = ["clothing"]


# new Thing("future man",[".future person"],"*FUTURE MAN*");
# new Thing("future woman",[".future person"],"*FUTURE WOMAN*");


class FuturePerson(Person):
    child_generators = [
        ChildGenerator("body"),
        ChildGenerator("future psyche"),
        ChildGenerator("future clothing set")
    ]
    names_data = "*FUTURE PERSON*"


# new Thing("future psyche",["future thoughts","future memories"],"psyche");
# new Thing("future thoughts",["black hole,0.01%",["future thought,2-3"]],"thoughts");
# new Thing("future thought",[],["*FUTURE THOUGHT*"]);
# new Thing("future memories",["future memory,2-4"],"memories");
# new Thing("future memory",[],["*FUTURE MEMORY*"]);


CONTENTS = [
    ClothingSet,

    Person,

    Body,
    Torso,
    Chest,

    Pelvis,

    Head,

    MedievalClothingSet,

    MedievalPerson,

    MedievalPeasant,

    FutureClothingSet,

    FuturePerson,
]