from v1.factories.fng.description.character.hair import MaleHairFactory, FemaleHairFactory
from v1.factories.fng.description.character.face import FaceFactory
from v1.factories.fng.description.character.eyes import EyesFactory
from ..promise import PromiseFactory
from v1.factories.fng.description.character.name import MaleNameFactory, FemaleNameFactory
from ..attitude import MaleAttitudeFactory, FemaleAttitudeFactory


class RacialGenerators:
    hair = MaleHairFactory
    face = FaceFactory
    eyes = EyesFactory
    promise = PromiseFactory
    name = MaleNameFactory
    attitude = MaleAttitudeFactory


class Race:
    name = "Race"
    plural = "races"

    male_hair_generator = MaleHairFactory
    female_hair_generator = FemaleHairFactory

    face_generator = FaceFactory
    eyes_generator = EyesFactory
    promise_generator = PromiseFactory

    male_name_generator = MaleNameFactory
    female_name_generator = FemaleNameFactory

    male_attitude_generator = MaleAttitudeFactory
    female_attitude_generator = FemaleAttitudeFactory

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
