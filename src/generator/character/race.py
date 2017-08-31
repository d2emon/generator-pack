from generator.character.hair import HairGenerator
from generator.character.face import FaceGenerator
from generator.character.eyes import EyesGenerator
from generator.character.promise import PromiseGenerator


class Race():
    name = "Race"
    plural = "races"

    hair_generator = HairGenerator
    face_generator = FaceGenerator
    eyes_generator = EyesGenerator
    promise_generator = PromiseGenerator

    # first_names = []
    # last_names = []


class Human(Race):
    name = "Human"
    plural = "humans"


class ElfHairGenerator(HairGenerator):
    colors = [
        "Elf",
    ]  # 1
    hairtypes = [
        "Elf",
    ]  # 2


class ElfFaceGenerator(FaceGenerator):
    facetypes = [
        "elf",
    ]


class ElfEyesGenerator(EyesGenerator):
    colors = [
        "Elf",
    ]


class ElfPromiseGenerator(PromiseGenerator):
    settlements = [
        "elf",
    ]


class Elf(Race):
    name = "Elf"
    plural = "elves"

    hair_generator = ElfHairGenerator
    face_generator = ElfFaceGenerator
    eyes_generator = ElfEyesGenerator
    promise_generator = ElfPromiseGenerator

    first_names = []
    last_names = []

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

class GnomeHairGenerator(HairGenerator):
    colors = [
        "Gnome",
    ]  # 1
    hairtypes = [
        "Gnome",
    ]  # 2


class GnomeFaceGenerator(FaceGenerator):
    facetypes = [
        "gnome",
    ]


class Gnome(Race):
    name = "Gnome"
    plural = "gnomes"

    hair_generator = GnomeHairGenerator
    face_generator = GnomeFaceGenerator
    first_names = []
    last_names = []


class GoblinHairGenerator(HairGenerator):
    hairtypes = [
        "Goblin",
    ]  # 2


class GoblinFaceGenerator(FaceGenerator):
    facetypes = [
        "goblin",
    ]


class GoblinPromiseGenerator(PromiseGenerator):
    settlements = [
        "goblin",
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

    first_names = []
    last_names = []


class Orc(Goblinoid):
    name = "Orc"
    plural = "orcs"

    first_names = []
    last_names = []


class Goblin(Goblinoid):
    name = "Goblin"
    plural = "goblins"

    first_names = []
    last_names = []


class GiantHairGenerator(HairGenerator):
    hairtypes = [
        "Giant",
    ]  # 2


class GiantFaceGenerator(FaceGenerator):
    facetypes = [
        "giant",
    ]


class Giant(Race):
    name = "Giant"
    plural = "giants"

    hair_generator = GiantHairGenerator
    face_generator = GiantFaceGenerator


class Dwarf(Giant):
    name = "Dwarf"
    plural = "dvarves"

    first_names = []
    last_names = []


class Halfling(Race):
    name = "Halfling"
    plural = "halflings"


class Vampire(Race):
    name = "Vampire"
    plural = "vampires"


class Werewolf(Race):
    name = "Werewolf"
    plural = "werewolves"
