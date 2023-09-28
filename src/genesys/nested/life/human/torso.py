from models.v5 import life
from ..body.body_parts import BodyPartFactory, SoftBodyPartFactory
from ..body.skin import SkinFactory
from ...unsorted_life import PastaFactory
from ...unsorted_organics import LintFactory, SweatFactory


class NaughtyBitsFactory(SoftBodyPartFactory):
    # model = life.NaughtyBits
    pass


class ButtFactory(BodyPartFactory):
    def children(self):
        yield PastaFactory.probable(0.01)
        yield SweatFactory.probable(50)
        yield from super().children()


class PelvisFactory(BodyPartFactory):
    # model = life.Pelvis

    def children(self):
        yield NaughtyBitsFactory.one()
        yield ButtFactory.one()
        yield from super().children()


class NippleFactory(BodyPartFactory):
    # model = life.Nipple

    def children(self):
        yield SkinFactory.one()


class BellybuttonFactory(BodyPartFactory):
    # model = life.Bellybutton

    def children(self):
        yield SkinFactory.one()
        yield LintFactory.multiple(0, 1)


class ChestFactory(BodyPartFactory):
    # model = life.Chest

    def children(self):
        yield NippleFactory.multiple(2)
        yield BellybuttonFactory.one()
        yield from super().children()


class TorsoFactory(BodyPartFactory):
    # model = life.Torso

    def chest(self):
        yield ChestFactory.one()

    def pelvis(self):
        yield PelvisFactory.one()

    def children(self):
        yield from self.chest()
        yield from self.pelvis()
        yield from super().children()
