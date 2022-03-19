from . import Race
from v1.factories.fng.description.character.hair import MaleHairFactory, FemaleHairFactory
from v1.factories.fng.description.character.face import FaceFactory
from v1.factories.fng.description.character.eyes import EyesFactory
from ..promise import PromiseFactory
from v1.factories.fng.description.character.name import NameFactory


elf_hair_colors = [
    "Purple",
    "Blue",
    "Green",
    "Red",
    "White",
    "Blonde",
    "Brown",
    "Light blue",
    "Light green",
    "Pink",
    "Silver",
    "Golden",
]  # 1


class ElfMaleHairFactory(MaleHairFactory):
    colors = elf_hair_colors
    hairtypes = [
        "perfectly groomed hair",
        "well groomed hair",
        "sleek hair",
        "long hair",
        "curly hair",
        "straight hair",
        "flowing hair",
        "wavy hair",
        "shoulder-length hair",
    ]  # 2


class ElfFemaleHairFactory(FemaleHairFactory):
    colors = elf_hair_colors
    hairtypes = [
        "perfectly groomed hair",
        "well groomed hair",
        "long wavy hair",
        "long layed hair",
        "layered hair",
        "sleek hair",
        "long hair",
        "curly hair",
        "straight hair",
        "flowing hair",
        "wavy hair",
        "shoulder-length hair",
    ]


class ElfFaceFactory(FaceFactory):
    facetypes = [
        "thin",
        "chiseled",
        "craggy",
        "fine",
        "fresh",
        "full",
        "furrowed",
        "handsome",
        "sculpted",
        "strong",
        "long",
        "round",
        "bony",
        "lean",
    ]


class ElfEyesFactory(EyesFactory):
    colors = [
        "blue",
        "brown",
        "hazel",
        "green",
        "amber",
        "gray",
        "sapphire",
        "aquamarine",
        "pink",
        "red",
        "golden",
        "violet",
        "silver",
    ]


class ElfPromiseFactory(PromiseFactory):
    settlements = [
        "village",
        "lands",
        "people",
        "town",
        "families",
        "ships",
        "armies",
        "homes",
        "castle",
        "palace",
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
        "ancestors",
        "children",
        "spirits",
    ]


class ElfMaleNameFactory(NameFactory):
    firstnames = [
        "Wyninn",
        "Ninleyn",
        "Tinlef",
        "Elluin",
        "Elduin",
        "Elmon",
        "Almar",
        "Alas",
        "Alwin",
        "Almer",
        "Alre",
        "Alred",
        "Alen",
        "Alluin",
        "Alduin",
        "Almon",
        "Hagwin",
        "Hagmere",
    ]
    lastnames = [
        "Moonwalker",
        "Dawnwing",
        "Dawnfury",
        "Moonfall",
        "Nightgaze",
        "Dawnthorn",
        "Stagrunner",
        "Wildoak",
        "Lunadancer",
        "Dawnwhisper",
    ]


class ElfFemaleNameFactory(ElfMaleNameFactory):
    firstnames = [
        "Ylsysea",
        "Nilerea",
        "Lelselea",
        "Lelarea",
        "Nafareath",
        "Felerai",
        "Sillaesa",
        "Leadrieth",
        "Yneasia",
        "Iyohara"
    ]


class Elf(Race):
    name = "Elf"
    plural = "elves"

    male_hair_generator = ElfMaleHairFactory
    female_hair_generator = ElfFemaleHairFactory

    face_generator = ElfFaceFactory
    eyes_generator = ElfEyesFactory
    promise_generator = ElfPromiseFactory

    male_name_generator = ElfMaleNameFactory
    female_name_generator = ElfFemaleNameFactory


class NightElf(Elf):
    name = "Night Elf"
    plural = "night elves"


class BloodElf(Elf):
    name = "Blood Elf"
    plural = "blood elves"


class HighElf(Elf):
    name = "High Elf"
    plural = "high elves"


class WoodElf(Elf):
    name = "Wood Elf"
    plural = "wood elves"


class DarkElf(Elf):
    name = "Dark Elf"
    plural = "dark elves"
