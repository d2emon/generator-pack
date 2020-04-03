from genesys.nested.models import Model
from .torso import Torso
from .arm import Arm
from .leg import Leg
from .head import Head


class Body(Model):
    heads = Model.children_property(Head)
    torso = Model.child_property(Torso)
    arm = Model.children_property(Arm)
    leg = Model.children_property(Leg)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Head
            yield Torso
            yield Arm.probable(99)
            yield Arm.probable(99)
            yield Leg.probable(99)
            yield Leg.probable(99)
