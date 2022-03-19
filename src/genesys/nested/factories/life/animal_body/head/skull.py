from generated import life
from ..body_parts import BodyPartFactory
from ..skeleton import BonesFactory
from ..head import BrainFactory


class SkullFactory(BodyPartFactory):
    default_model = life.Skull

    def children(self):
        yield BrainFactory()
        yield BonesFactory()
