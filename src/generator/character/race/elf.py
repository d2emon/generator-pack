from generator.character.hair import HairGenerator
from generator.character.face import FaceGenerator
from generator.character.eyes import EyesGenerator
from generator.character.promise import PromiseGenerator
from generator.character.name import NameGenerator
from generator.character.race import Race


class ElfHairGenerator(HairGenerator):
    colors = [
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


class ElfNameGenerator(NameGenerator):
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


class Elf(Race):
    name = "Elf"
    plural = "elves"

    hair_generator = ElfHairGenerator
    face_generator = ElfFaceGenerator
    eyes_generator = ElfEyesGenerator
    promise_generator = ElfPromiseGenerator
    name_generator = ElfNameGenerator


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
