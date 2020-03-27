from . import Race
from ..hair import MaleHairFactory, FemaleHairFactory
from ..face import FaceFactory
from ..name import NameFactory


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


class DwarfMaleHairFactory(MaleHairFactory):
    hairtypes = dwarf_hairtypes


class DwarfFemaleHairFactory(FemaleHairFactory):
    hairtypes = dwarf_hairtypes


class DwarfFaceFactory(FaceFactory):
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


class DwarfMaleNameFactory(NameFactory):
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


class DwarfFemaleNameFactory(DwarfMaleNameFactory):
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

    male_hair_generator = DwarfMaleHairFactory
    female_hair_generator = DwarfFemaleHairFactory

    face_generator = DwarfFaceFactory

    male_name_generator = DwarfMaleNameFactory
    female_name_generator = DwarfFemaleNameFactory


class Giant(Dwarf):
    name = "Giant"
    plural = "giants"


class Halfling(Dwarf):
    name = "Halfling"
    plural = "halflings"
