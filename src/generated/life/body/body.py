"""
- Body
"""
from genesys.model.model import Model
from .torso import Torso
from .arm import Arm
from .leg import Leg
from .head import Head


class Body(Model):
    heads = Model.children_property(Head)
    torso = Model.child_property(Torso)
    arm = Model.children_property(Arm)
    leg = Model.children_property(Leg)
