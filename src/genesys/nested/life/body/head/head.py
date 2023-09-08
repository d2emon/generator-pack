from models.v5 import life
from factories.thing.nested_factory import NestedFactory as Factory
from ...animal_body.skin import DeadSkinFactory
from ...animal_body.hair import HairFactory
from ...animal_body.head import NoseFactory, EyeFactory
from ...animal_body.mammal import MammalHeadFactory


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


class HeadFactory(MammalHeadFactory):
    default_model = life.Head

    @classmethod
    def nose(cls):
        yield NoseFactory()

    @classmethod
    def eyes(cls):
        yield EyeFactory().probable(99)
        yield EyeFactory().probable(99)

    @classmethod
    def fur(cls):
        yield HeadHairFactory().probable(85)
