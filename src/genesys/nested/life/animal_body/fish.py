from models.v5 import life
from factories.nested_factory import NestedFactory as Factory
from .skeleton import MuscleFactory
from .skin import SkinFactory, ScalesFactory


class FishFinFactory(Factory):
    default_model = life.FishFin

    def children(self):
        yield MuscleFactory()
        yield ScalesFactory()


class FishTailFactory(Factory):
    default_model = life.FishTail

    def children(self):
        yield MuscleFactory()
        yield ScalesFactory()


class FishSkinFactory(SkinFactory):
    default_model = life.FishSkin

    def children(self):
        yield ScalesFactory()
