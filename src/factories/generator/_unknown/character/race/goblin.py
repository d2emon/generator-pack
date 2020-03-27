from . import Race
from ..hair import MaleHairFactory, FemaleHairFactory
from ..face import FaceFactory
from ..promise import PromiseFactory
from ..name import NameFactory


goblin_hairtypes = [
    "short hair",
    "short hair",
    "short hair",
    # "perfectly groomed hair",
    # "well groomed hair",
    # "sleek hair",
    "long hair",
    "curly hair",
    "straight hair",
    # "flowing hair",
    # "wavy hair",
    "coily hair",
    "shaggy hair",
    "greasy hair",
    "oily hair",
    "frizzy hair",
    "shoulder-length hair",
    "dreadlocks",
]  # 2


class GoblinMaleHairFactory(MaleHairFactory):
    hairtypes = goblin_hairtypes


class GoblinFemaleHairFactory(FemaleHairFactory):
    hairtypes = goblin_hairtypes


class GoblinFaceFactory(FaceFactory):
    facetypes = [
        "thin",
        "chiseled",
        "craggy",
        "fine",
        "fresh",
        "full",
        "furrowed",
        # "handsome",
        # "sculpted",
        "strong",
        "long",
        "round",
        "bony",
        "lean",
        "skinny",
    ]


class GoblinPromiseFactory(PromiseFactory):
    settlements = [
        "village",
        "city",
        "lands",
        "people",
        "town",
        "families",
        "ships",
        "armies",
        "homes",
        "stronghold",
        # "castle",
        # "palace",
        "natives",
        "wildlife",
        "farms",
        "country",
        "haven",
        "mountains",
        "rivers",
        "river",
        "sea",
        # "woods",
        # "woodlands",
        "clan",
        "folk",
        "tribe",
        "tribes",
        "ancestors",
        "children",
        "deserts",
        "mines",
        "spirits",
    ]


class TrollMaleNameFactory(NameFactory):
    firstnames = [
        "Ekon",
        "Erasto",
        "Haijen",
        "Hamedi",
        "Hokima",
        "Jaafan",
        "Jabir",
        "Jalai",
        "Javyn",
        "Jijel",
        "Juma",
        "Jumoke",
        "Kaijin",
        "Kazko",
        "Maalik",
        "Makas",
        "Malak",
        "Nyabingi",
        "Rahjin",
        "Rakash",
        "Rashi",
        "Razi",
    ]
    lastnames = [
        "Xueshi",
        "Vintish",
        "Zalaahoku",
        "Valkeiki",
        "Hakjel",
        "Hanalaji",
        "Zebnanji",
        "Tesh'Rimon",
        "Junbir",
        "Zenunjo",
    ]


class TrollFemaleNameFactory(TrollMaleNameFactory):
    firstnames = [
        "Gir'Enji",
        "Yahuja",
        "Feyini",
        "Ziruja",
        "Zeyra",
        "Zuladur",
        "Zujula",
        "Sonayo",
        "Vulino",
        "Yaonji",
    ]


class OrcMaleNameFactory(NameFactory):
    firstnames = [
        "Gnarg",
        "Gnarlug",
        "Gnorl",
        "Gnorth",
        "Gnoth",
        "Gnurl",
        "Golag",
        "Golub",
        "Gomatug",
        "Gomoku",
        "Gorgu",
        "Gorlag",
        "Grikug",
        "Grug",
        "Grukag",
        "Grukk",
        "Grung",
        "Gruul",
    ]
    lastnames = [
        "Wolfbasher",
        "Burningfury",
        "Firesong",
        "Goreseeker",
        "Hellsplitter",
        "Deatheye",
        "Burninghorn",
        "Gorebasher",
        "Wolfhammer",
        "Boneslayer",
    ]


class OrcFemaleNameFactory(OrcMaleNameFactory):
    firstnames = [
        "Umoda",
        "Zonkaja",
        "Goredo",
        "Umakuma",
        "Groanu",
        "Zunala",
        "Gredula",
        "Sheeda",
        "Greras",
        "Elgudo",
    ]


class GoblinMaleNameFactory(NameFactory):
    firstnames = [
        "Karax",
        "Baxeek",
        "Soxart",
        "Rezikmez",
        "Fizink",
        "Wimax",
        "Jexmelyx",
        "Grexmex",
        "Tinkbelex",
        "Greekeels",
    ]
    lastnames = [
        "Greaseblast",
        "Haggletooth",
        "Deadnozzle",
        "Fizfingers",
        "Gearnozzle",
        "Shadowgleam",
        "Copperbuttons",
        "Deadsprocket",
        "Greasebottom",
        "Toptwister",
    ]


class GoblinFemaleNameFactory(GoblinMaleNameFactory):
    firstnames = [
        "Amizenee",
        "Nexlee",
        "Pybilope",
        "Nalleex",
        "Glelee",
        "Glyxi",
        "Linxie",
        "Minzi",
        "Glebizee",
        "Fluxinky",
    ]


class Goblinoid(Race):
    name = "Goblinoid"
    plural = "goblinoids"

    male_hair_generator = GoblinMaleHairFactory
    female_hair_generator = GoblinFemaleHairFactory

    face_generator = GoblinFaceFactory
    promise_generator = GoblinPromiseFactory


class Troll(Goblinoid):
    name = "Troll"
    plural = "trolls"

    male_name_generator = TrollMaleNameFactory
    female_name_generator = TrollFemaleNameFactory


class Orc(Goblinoid):
    name = "Orc"
    plural = "orcs"

    male_name_generator = OrcMaleNameFactory
    female_name_generator = OrcFemaleNameFactory


class Goblin(Goblinoid):
    name = "Goblin"
    plural = "goblins"

    male_name_generator = GoblinMaleNameFactory
    female_name_generator = GoblinFemaleNameFactory
