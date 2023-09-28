from models.v5 import life
from .brain import BrainFactory
from ...body.body_parts import BodyPartFactory
from ...body.skeleton import BonesFactory


class SkullFactory(BodyPartFactory):
    # model = life.Skull

    def children(self):
        yield BrainFactory.one()
        yield BonesFactory.one()
