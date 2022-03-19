from generated import life
from ...materials import SweatFactory, KeratinFactory
from ..animal_body.body_parts import BodyPartFactory, SoftBodyPartFactory
from ..animal_body.hair import HairFactory


class ArmpitHairFactory(HairFactory):
    default_model = life.ArmpitHair


class ArmpitFactory(SoftBodyPartFactory):
    default_model = life.Armpit

    def children(self):
        yield ArmpitHairFactory()
        yield SweatFactory().probable(80)
        yield from super().children()


class ElbowFactory(BodyPartFactory):
    default_model = life.Elbow


class FingernailFactory(BodyPartFactory):
    default_model = life.Fingernail

    def children(self):
        # yield Dust.probable(30)
        yield KeratinFactory()


class FingerFactory(BodyPartFactory):
    default_model = life.Finger

    def children(self):
        yield FingernailFactory()
        yield from super().children()


class HandFactory(BodyPartFactory):
    default_model = life.Hand

    def children(self):
        yield from FingerFactory().multiple(5)
        yield from super().children()


class ArmFactory(BodyPartFactory):
    default_model = life.Arm

    def children(self):
        yield HandFactory()
        yield ElbowFactory()
        yield ArmpitFactory()
        yield from super().children()
