from generated import life
from ....factory import Factory
from ...animal_body.body_parts import BodyPartFactory
from ...animal_body.skeleton import BonesFactory
from ...animal_body.skin import DeadSkinFactory
from ...animal_body.hair import HairFactory
from .brain import BrainFactory
from .eye import EyeFactory
from .ear import EarFactory
from .nose import NoseFactory
from .mouth import MouthFactory


class DandruffFactory(Factory):
    default_model = life.Dandruff

    def children(self):
        yield DeadSkinFactory()


class HeadHairFactory(HairFactory):
    default_model = life.HeadHair
    names = ["brown", "black", "gray", "light", "blonde", "red", "dark"]

    def generate_name(self):
        return f"{self.select_item(*self.names)} hair"

    def children(self):
        yield DandruffFactory()
        yield from super().children()


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
