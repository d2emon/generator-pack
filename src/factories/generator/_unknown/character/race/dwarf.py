from factories.generator import MaleHairGenerator, FemaleHairGenerator
from factories.generator import FaceGenerator
from factories.generator import NameGenerator
from factories.generator import Race


dwarf_hairtypes = [
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
]

class DwarfMaleHairGenerator(MaleHairGenerator):
    hairtypes = dwarf_hairtypes


class DwarfFemaleHairGenerator(FemaleHairGenerator):
    hairtypes = dwarf_hairtypes


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


class DwarfMaleNameGenerator(NameGenerator):
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


class DwarfFemaleNameGenerator(DwarfMaleNameGenerator):
    firstnames = [
        "Belianyss",
        "Daerahniss",
        "Dearirwyn",
        "Brenunwyn",
        "Gwenirnys",
        "Bretianura",
        "Einormyl",
        "Breteodiel",
        "Bellores",
        "Brylilen",
    ]


class Dwarf(Race):
    name = "Dwarf"
    plural = "dwarves"

    male_hair_generator = DwarfMaleHairGenerator
    female_hair_generator = DwarfFemaleHairGenerator

    face_generator = DwarfFaceGenerator

    male_name_generator = DwarfMaleNameGenerator
    female_name_generator = DwarfFemaleNameGenerator


class Giant(Dwarf):
    name = "Giant"
    plural = "giants"


class Halfling(Dwarf):
    name = "Halfling"
    plural = "halflings"
