from generator.character.hair import MaleHairGenerator, FemaleHairGenerator
from generator.character.face import FaceGenerator
from generator.character.eyes import EyesGenerator
from generator.character.promise import PromiseGenerator
from generator.character.name import MaleNameGenerator, FemaleNameGenerator


class Race():
    name = "Race"
    plural = "races"

    male_hair_generator = MaleHairGenerator
    female_hair_generator = FemaleHairGenerator

    face_generator = FaceGenerator
    eyes_generator = EyesGenerator
    promise_generator = PromiseGenerator

    male_name_generator = MaleNameGenerator
    female_name_generator = FemaleNameGenerator


    @classmethod
    def hair_generator(cls, sex=0):
        if sex == 1:
            return cls.female_hair_generator
        else:
            return cls.male_hair_generator

    @classmethod
    def name_generator(cls, sex=0):
        if sex == 1:
            return cls.female_name_generator
        else:
            return cls.male_name_generator


class Human(Race):
    name = "Human"
    plural = "humans"


class Vampire(Race):
    name = "Vampire"
    plural = "vampires"


class Werewolf(Race):
    name = "Werewolf"
    plural = "werewolves"
