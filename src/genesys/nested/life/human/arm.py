from models.v5 import life
from ..body.body_parts import BodyPartFactory, SoftBodyPartFactory
from ...unsorted_organics import DustFactory, KeratinFactory, SweatFactory

# ???
from ..body.hair import HairFactory


class FingernailFactory(BodyPartFactory):
    model = life.Fingernail

    def children(self):
        yield DustFactory.probable(30)
        yield KeratinFactory.one()


class FingerFactory(BodyPartFactory):
    model = life.Finger

    def children(self):
        yield FingernailFactory.one()
        yield from super().children()


class HandFactory(BodyPartFactory):
    model = life.Hand

    def children(self):
        yield FingerFactory.multiple(5)
        yield from super().children()


class ElbowFactory(BodyPartFactory):
    model = life.Elbow


class ArmpitHairFactory(HairFactory):
    model = life.ArmpitHair


class ArmpitFactory(SoftBodyPartFactory):
    model = life.Armpit

    def children(self):
        yield ArmpitHairFactory.one()
        yield SweatFactory.probable(80)
        yield from super().children()


class ArmFactory(BodyPartFactory):
    model = life.Arm

    def children(self):
        yield HandFactory.one()
        yield ElbowFactory.one()
        yield ArmpitFactory.one()
        yield from super().children()
