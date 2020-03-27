from factories.generator import MaleHairGenerator, FemaleHairGenerator
from factories.generator import FaceGenerator
from factories.generator import PromiseGenerator
from factories.generator import NameGenerator
from factories.generator import Race


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


class GoblinMaleHairGenerator(MaleHairGenerator):
    hairtypes = goblin_hairtypes


class GoblinFemaleHairGenerator(FemaleHairGenerator):
    hairtypes = goblin_hairtypes


class GoblinFaceGenerator(FaceGenerator):
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


class GoblinPromiseGenerator(PromiseGenerator):
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


class TrollMaleNameGenerator(NameGenerator):
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


class TrollFemaleNameGenerator(TrollMaleNameGenerator):
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


class OrcMaleNameGenerator(NameGenerator):
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


class OrcFemaleNameGenerator(OrcMaleNameGenerator):
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


class GoblinMaleNameGenerator(NameGenerator):
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


class GoblinFemaleNameGenerator(GoblinMaleNameGenerator):
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

    male_hair_generator = GoblinMaleHairGenerator
    female_hair_generator = GoblinFemaleHairGenerator

    face_generator = GoblinFaceGenerator
    promise_generator = GoblinPromiseGenerator


class Troll(Goblinoid):
    name = "Troll"
    plural = "trolls"

    male_name_generator = TrollMaleNameGenerator
    female_name_generator = TrollFemaleNameGenerator


class Orc(Goblinoid):
    name = "Orc"
    plural = "orcs"

    male_name_generator = OrcMaleNameGenerator
    female_name_generator = OrcFemaleNameGenerator


class Goblin(Goblinoid):
    name = "Goblin"
    plural = "goblins"

    male_name_generator = GoblinMaleNameGenerator
    female_name_generator = GoblinFemaleNameGenerator
