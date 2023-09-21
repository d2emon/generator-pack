from models.v5 import life
from factories.thing.nested_factory import NestedFactory as Factory
from utils.nested import select_item
from ...body.skin import DeadSkinFactory
from ...body.hair import HairFactory, DandruffFactory
from ...body.head import NoseFactory, EyeFactory
from ...body.mammal import MammalHeadFactory


class HeadHairFactory(HairFactory):
    default_model = life.HeadHair
    names = ["brown", "black", "gray", "light", "blonde", "red", "dark"]

    def generate_name(self):
        return f"{select_item(*self.names)} hair"

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
