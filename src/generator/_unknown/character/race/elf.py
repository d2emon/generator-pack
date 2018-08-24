from generator._unknown.character.hair import MaleHairGenerator, FemaleHairGenerator
from generator._unknown.character.face import FaceGenerator
from generator._unknown.character.eyes import EyesGenerator
from generator._unknown.character.promise import PromiseGenerator
from generator._unknown.character.name import NameGenerator
from generator._unknown.character.race import Race


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

class ElfMaleHairGenerator(MaleHairGenerator):
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


class ElfFemaleHairGenerator(FemaleHairGenerator):
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


class ElfFaceGenerator(FaceGenerator):
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


class ElfEyesGenerator(EyesGenerator):
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


class ElfPromiseGenerator(PromiseGenerator):
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


class ElfMaleNameGenerator(NameGenerator):
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


class ElfFemaleNameGenerator(ElfMaleNameGenerator):
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

    male_hair_generator = ElfMaleHairGenerator
    female_hair_generator = ElfFemaleHairGenerator

    face_generator = ElfFaceGenerator
    eyes_generator = ElfEyesGenerator
    promise_generator = ElfPromiseGenerator

    male_name_generator = ElfMaleNameGenerator
    female_name_generator = ElfFemaleNameGenerator


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
