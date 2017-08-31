from generator.character.hair import HairGenerator
from generator.character.face import FaceGenerator
from generator.character.eyes import EyesGenerator
from generator.character.promise import PromiseGenerator


class Race():
    name = "Race"

    hair_generator = HairGenerator
    face_generator = FaceGenerator
    eyes_generator = EyesGenerator
    promise_generator = PromiseGenerator

    # first_names = []
    # last_names = []


class Human(Race):
    name = "Human"


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

    hair_generator = ElfHairGenerator
    face_generator = ElfFaceGenerator
    eyes_generator = ElfEyesGenerator
    promise_generator = ElfPromiseGenerator

    first_names = []
    last_names = []


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
    name = "Goblinioid"

    hair_generator = GoblinHairGenerator
    face_generator = GoblinFaceGenerator
    promise_generator = GoblinPromiseGenerator


class Troll(Goblinoid):
    name = "Troll"

    first_names = []
    last_names = []


class Orc(Goblinoid):
    name = "Orc"

    first_names = []
    last_names = []


class Goblin(Goblinoid):
    name = "Goblin"

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

    hair_generator = GiantHairGenerator
    face_generator = GiantFaceGenerator


class Dwarf(Giant):
    name = "Dwarf"

    first_names = []
    last_names = []
