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


class Person(Thing):
    child_generators = [
        ChildGenerator("body"),
        ChildGenerator("psyche"),
        ChildGenerator("clothing set"),
    ]
    names_data = ["*PERSON*"]


class Man(Person):
    child_generators = [ChildGenerator(".person")]
    names_data = ["*MAN"]


class Woman(Person):
    child_generators = [ChildGenerator(".person")]
    names_data = ["*WOMAN"]


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


class Bellybutton(Thing):
    child_generators = [
        ChildGenerator("skin"),
        ChildGenerator("lint", (0, 1))
    ]


class Nipple(Thing):
    child_generators = [ChildGenerator("skin")]


class Pelvis(Thing):
    child_generators = [
        ChildGenerator("naughty bits"),
        ChildGenerator("butt"),
        ChildGenerator(".body part"),
    ]


class NaughtyBits(Thing):
    child_generators = [ChildGenerator(".soft body part")]


class Butt(Thing):
    child_generators = [
        ChildGenerator("pasta", probability=0.01),
        ChildGenerator("sweat", probability=50),
        ChildGenerator(".body part"),
    ]


class Arm(Thing):
    child_generators = [
        ChildGenerator("hand"),
        ChildGenerator("elbow"),
        ChildGenerator("armpit"),
        ChildGenerator(".body part"),
    ]


class Hand(Thing):
    child_generators = [
        ChildGenerator("finger", (5, )),
        ChildGenerator(".body part"),
    ]


class Finger(Thing):
    child_generators = [
        ChildGenerator("fingernail"),
        ChildGenerator(".body part"),
    ]


class Fingernail(Thing):
    child_generators = [
        ChildGenerator("dust", probability=30),
        ChildGenerator("keratin"),
    ]


class Elbow(Thing):
    child_generators = [
        ChildGenerator(".body part"),
    ]


class Armpit(Thing):
    child_generators = [
        ChildGenerator("armpit hair"),
        ChildGenerator("sweat", probability=80),
        ChildGenerator(".soft body part"),
    ]


class ArmpitHair(Thing):
    names_data = "hair"
    child_generators = [
        ChildGenerator(".hair"),
    ]


class Leg(Thing):
    child_generators = [
        ChildGenerator("foot"),
        ChildGenerator("knee"),
        ChildGenerator(".body part"),
    ]


class Foot(Thing):
    child_generators = [
        ChildGenerator("toe", (5,)),
        ChildGenerator("sweat", probability=30),
        ChildGenerator(".body part"),
    ]


class Toe(Thing):
    child_generators = [
        ChildGenerator("toenail"),
        ChildGenerator(".body part"),
    ]


class Toenail(Thing):
    child_generators = [
        ChildGenerator("dust", probability=40),
        ChildGenerator("keratin"),
    ]


class Knee(Thing):
    child_generators = [
        ChildGenerator(".body part"),
    ]


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


class FutureMan(Man):
    child_generators = [
        ChildGenerator(".future person")
    ]
    names_data = ["*FUTURE MAN*"]


class FutureWoman(Man):
    child_generators = [
        ChildGenerator(".future person")
    ]
    names_data = ["*FUTURE WOMAN*"]


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


class Tourist(Person):
    child_generators = [ChildGenerator(".person"),]
    names_data = "*PERSON*| (tourist)"


CONTENTS = [
    ClothingSet,

    Man,
    Woman,
    Person,

    Body,
    Torso,
    Chest,
    Bellybutton,
    Nipple,
    Pelvis,
    NaughtyBits,
    Butt,
    Arm,
    Hand,
    Finger,
    Fingernail,
    Elbow,
    Armpit,
    ArmpitHair,
    Leg,
    Foot,
    Toe,
    Toenail,
    Knee,
    Head,

    FutureClothingSet,

    FutureMan,
    FutureWoman,
    FuturePerson,

    Tourist,
]