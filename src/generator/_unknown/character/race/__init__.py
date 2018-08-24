from generator._unknown.character.hair import MaleHairGenerator, FemaleHairGenerator
from generator._unknown.character.face import FaceGenerator
from generator._unknown.character.eyes import EyesGenerator
from generator._unknown.character.promise import PromiseGenerator
from generator._unknown.character.name import MaleNameGenerator, FemaleNameGenerator
from generator._unknown.character import MaleAttitudeGenerator, FemaleAttitudeGenerator


class RacialGenerators():
    hair = MaleHairGenerator
    face = FaceGenerator
    eyes = EyesGenerator
    promise = PromiseGenerator
    name = MaleNameGenerator
    attitude = MaleAttitudeGenerator


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

    male_attitude_generator = MaleAttitudeGenerator
    female_attitude_generator = FemaleAttitudeGenerator

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

    @classmethod
    def attitude_generator(cls, sex=0):
        if sex == 1:
            return cls.female_attitude_generator
        else:
            return cls.male_attitude_generator

    @classmethod
    def generators(cls, sex=0):
        g = RacialGenerators()
        g.hair = cls.hair_generator(sex)
        g.face = cls.face_generator
        g.eyes = cls.eyes_generator
        g.promise = cls.promise_generator
        g.name = cls.name_generator(sex)
        g.attitude = cls.attitude_generator(sex)
        return g


class Human(Race):
    name = "Human"
    plural = "humans"


class Vampire(Race):
    name = "Vampire"
    plural = "vampires"


class Werewolf(Race):
    name = "Werewolf"
    plural = "werewolves"
