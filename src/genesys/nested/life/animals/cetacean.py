from models.v5 import life
from factories.thing.nested_factory import NestedFactory as Factory
from ..body.skeleton import MuscleFactory
from ..body.skin import SkinFactory


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
