from models.v5 import life
from factories.thing.nested_factory import NestedFactory as Factory
from .skeleton import MuscleFactory
from .skin import SkinFactory


class CetaceanFinFactory(Factory):
    default_model = life.CetaceanFin

    def children(self):
        yield MuscleFactory()
        yield SkinFactory()


class CetaceanFlipperFactory(Factory):
    default_model = life.CetaceanFlipper

    def children(self):
        yield MuscleFactory()
        yield SkinFactory()
