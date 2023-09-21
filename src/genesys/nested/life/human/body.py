from genesys.nested.factories.nested_factory import NestedFactory
from models.v5 import life
from .torso import TorsoFactory
from .arm import ArmFactory
from .leg import LegFactory
from .head import HeadFactory


class BodyFactory(NestedFactory):
    # TODO: Make child of AnimalBodyFactory
    model = life.Body

    def children(self):
        yield HeadFactory.one()
        yield TorsoFactory.one()
        yield ArmFactory.probable(99)
        yield ArmFactory.probable(99)
        yield LegFactory.probable(99)
        yield LegFactory.probable(99)
