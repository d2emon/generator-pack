from generated import life
from ..body_parts import BodyPartFactory
from ..skeleton import BonesFactory
from .brain import BrainFactory
from .eye import EyeFactory
from .ear import EarFactory
from .hair import HeadHairFactory
from .nose import NoseFactory
from .mouth import MouthFactory


class SkullFactory(BodyPartFactory):
    default_model = life.Skull

    def children(self):
        yield BrainFactory()
        yield BonesFactory()


class HeadFactory(BodyPartFactory):
    default_model = life.Head

    @classmethod
    def mouth(cls):
        yield MouthFactory()

    @classmethod
    def nose(cls):
        yield NoseFactory()

    @classmethod
    def eyes(cls):
        yield EyeFactory().probable(99)
        yield EyeFactory().probable(99)

    @classmethod
    def ears(cls):
        yield from EarFactory().multiple(2)

    @classmethod
    def skull(cls):
        yield SkullFactory()
        yield HeadHairFactory().probable(85)

    def children(self):
        yield from self.mouth()
        yield from self.nose()
        yield from self.eyes()
        yield from self.ears()
        yield from self.skull()
        yield from super().children()
