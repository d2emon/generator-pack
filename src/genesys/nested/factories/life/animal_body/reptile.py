from generated import life
from ...factory import Factory
from .body_parts import BodyPartFactory, FleshFactory
from .limb import WingFactory, TailFactory
from .skin import ScalesFactory


class ReptileWingFactory(WingFactory):
    default_model = life.ReptileWing

    @classmethod
    def feathers(cls):
        yield ScalesFactory()


class ReptileHeadFactory(BodyPartFactory):
    default_model = life.ReptileHead

    def children(self):
        yield ScalesFactory()
        yield from super().children()


class ReptileLegFactory(BodyPartFactory):
    default_model = life.ReptileLeg

    def children(self):
        yield ScalesFactory()
        yield from super().children()


class ReptileBodyFactory(Factory):
    default_model = life.ReptileBody

    def children(self):
        yield ReptileHeadFactory()
        yield ScalesFactory()
        yield from ReptileLegFactory().multiple(4)
        yield TailFactory()
        yield FleshFactory()


class SnakeBodyFactory(Factory):
    default_model = life.ReptileBody

    def children(self):
        yield ReptileHeadFactory()
        yield ScalesFactory()
        yield TailFactory()
        yield FleshFactory()
