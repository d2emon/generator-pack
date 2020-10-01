"""
- Body
"""
from genesys.model.model import Model
from ..animals.animal import AnimalBody
from .torso import Torso
from .arm import Arm
from .leg import Leg
from .head import Head


class Body(AnimalBody):
    heads = Model.children_property(Head)
    torso = Model.child_property(Torso)
    arm = Model.children_property(Arm)
    leg = Model.children_property(Leg)

    @property
    def __eyes(self):
        for head in self.heads:
            yield from head.eyes

    @property
    def __mouths(self):
        for head in self.heads:
            yield from head.mouths

    @property
    def eyes(self):
        return list(self.__eyes)

    @property
    def mouths(self):
        return list(self.__mouths)
