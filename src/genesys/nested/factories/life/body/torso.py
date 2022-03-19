from generated import life
from ...materials import SweatFactory
from ..animal_body.body_parts import BodyPartFactory, SoftBodyPartFactory
from ..animal_body.skin import SkinFactory


class ButtFactory(BodyPartFactory):
    def children(self):
        # yield Pasta.probable(0.01)
        yield SweatFactory().probable(50)
        yield from super().children()


class NaughtyBitsFactory(SoftBodyPartFactory):
    default_model = life.NaughtyBits


class PelvisFactory(BodyPartFactory):
    default_model = life.Pelvis

    def children(self):
        yield NaughtyBitsFactory()
        yield ButtFactory()
        yield from super().children()


class NippleFactory(BodyPartFactory):
    default_model = life.Nipple

    def children(self):
        yield SkinFactory()


class BellybuttonFactory(BodyPartFactory):
    default_model = life.Bellybutton

    def children(self):
        yield SkinFactory()
        # yield from Lint.multiple(0, 1)


class ChestFactory(BodyPartFactory):
    default_model = life.Chest

    def children(self):
        yield from NippleFactory().multiple(2)
        yield BellybuttonFactory()
        yield from super().children()


class TorsoFactory(BodyPartFactory):
    default_model = life.Torso

    @classmethod
    def chest(cls):
        yield ChestFactory()

    @classmethod
    def pelvis(cls):
        yield PelvisFactory()

    def children(self):
        yield from self.chest()
        yield from self.pelvis()
        yield from super().children()
