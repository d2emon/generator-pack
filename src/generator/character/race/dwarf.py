from generator.character.hair import HairGenerator
from generator.character.face import FaceGenerator
from generator.character.name import NameGenerator
from generator.character.race import Race


class DwarfHairGenerator(HairGenerator):
    hairtypes = [
        "short hair",
        "short hair",
        "short hair",
        # "perfectly groomed hair",
        # "well groomed hair",
        # "sleek hair",
        "long hair",
        "curly hair",
        # "straight hair",
        # "flowing hair",
        # "wavy hair",
        # "sleek hair",
        "coily hair",
        "greasy hair",
        "shaggy hair",
        "oily hair",
        "frizzy hair",
        # "shaggy hair",
        "shoulder-length hair",
    ]  # 2


class DwarfFaceGenerator(FaceGenerator):
    facetypes = [
        # "thin",
        # "chiseled",
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
        # "bony",
        # "lean",
        # "skinny",
        "fat",
    ]


class DwarfNameGenerator(NameGenerator):
    firstnames = [
        "Bengahdar",
        "Banbrek",
        "Drumdus",
        "Dulgarn",
        "Galirg",
        "Kharnur",
        "Iromuador",
        "Ragorhdrom",
        "Urmbrek",
        "Theledon",
    ]
    lastnames = [
        "Longmantle",
        "Highbeard",
        "Frostpike",
        "Boulderstone",
        "Bouldergem",
        "Frostshaper",
        "Bouldershout",
        "Blackaxe",
        "Goldstone",
        "Battlefist",
    ]


class Dwarf(Race):
    name = "Dwarf"
    plural = "dwarves"

    hair_generator = DwarfHairGenerator
    face_generator = DwarfFaceGenerator
    name_generator = DwarfNameGenerator


class Giant(Dwarf):
    name = "Giant"
    plural = "giants"


class Halfling(Dwarf):
    name = "Halfling"
    plural = "halflings"
