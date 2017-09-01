from generator.character.hair import HairGenerator
from generator.character.face import FaceGenerator
from generator.character.eyes import EyesGenerator
from generator.character.promise import PromiseGenerator
from generator.character.name import NameGenerator


class Race():
    name = "Race"
    plural = "races"

    hair_generator = HairGenerator
    face_generator = FaceGenerator
    eyes_generator = EyesGenerator
    promise_generator = PromiseGenerator
    name_generator = NameGenerator


class Human(Race):
    name = "Human"
    plural = "humans"


class Vampire(Race):
    name = "Vampire"
    plural = "vampires"


class Werewolf(Race):
    name = "Werewolf"
    plural = "werewolves"
