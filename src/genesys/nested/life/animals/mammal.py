from models.v5 import life
from factories.thing.nested_factory import NestedFactory as Factory
from ..body.body_parts import BodyPartFactory, FleshFactory
from ..body.head import MouthFactory, SnoutFactory, EyeFactory, EarFactory, SkullFactory
from ..human.hair import FurFactory, WhiskersFactory
from .limb import TailFactory


class MammalLegFactory(BodyPartFactory):
    default_model = life.MammalLeg

    def children(self):
        yield FurFactory()
        yield from super().children()


class MammalHeadFactory(BodyPartFactory):
    default_model = life.MammalHead

    @classmethod
    def mouth(cls):
        yield MouthFactory()

    @classmethod
    def nose(cls):
        yield SnoutFactory()

    @classmethod
    def eyes(cls):
        yield from EyeFactory().multiple(2)

    @classmethod
    def ears(cls):
        yield from EarFactory().multiple(2)

    @classmethod
    def skull(cls):
        yield SkullFactory()

    @classmethod
    def fur(cls):
        yield FurFactory()
        yield WhiskersFactory()

    def children(self):
        yield from self.mouth()
        yield from self.nose()
        yield from self.eyes()
        yield from self.ears()
        yield from self.skull()
        yield from self.fur()
        yield from super().children()


class MammalBodyFactory(Factory):
    default_model = life.MammalBody

    def children(self):
        yield MammalHeadFactory()
        yield FurFactory()
        yield from MammalLegFactory().multiple(4)
        yield TailFactory()
        yield FleshFactory()
