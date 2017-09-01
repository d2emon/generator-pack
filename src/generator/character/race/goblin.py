from generator.character.hair import HairGenerator
from generator.character.face import FaceGenerator
from generator.character.promise import PromiseGenerator
from generator.character.name import NameGenerator
from generator.character.race import Race


class GoblinHairGenerator(HairGenerator):
    hairtypes = [
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
        "woods",
        "woodlands",
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


class TrollNameGenerator(NameGenerator):
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


class OrcNameGenerator(NameGenerator):
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


class GoblinNameGenerator(NameGenerator):
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


class Goblinoid(Race):
    name = "Goblinoid"
    plural = "goblinoids"

    hair_generator = GoblinHairGenerator
    face_generator = GoblinFaceGenerator
    promise_generator = GoblinPromiseGenerator


class Troll(Goblinoid):
    name = "Troll"
    plural = "trolls"

    name_generator = TrollNameGenerator


class Orc(Goblinoid):
    name = "Orc"
    plural = "orcs"

    name_generator = OrcNameGenerator


class Goblin(Goblinoid):
    name = "Goblin"
    plural = "goblins"

    name_generator = GoblinNameGenerator
