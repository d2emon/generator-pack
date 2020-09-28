from generated import life
from ...factory import Factory
from .torso import TorsoFactory
from .arm import ArmFactory
from .leg import LegFactory
from .head import HeadFactory


class BodyFactory(Factory):
    default_model = life.Body

    def children(self):
        yield HeadFactory()
        yield TorsoFactory()
        yield ArmFactory().probable(99)
        yield ArmFactory().probable(99)
        yield LegFactory().probable(99)
        yield LegFactory().probable(99)
