"""
- ReptileBodyPart
- ReptileWing
- ReptileHead
- ReptileLeg
- ReptileBody
"""
from .body_parts import BodyPart, Flesh
from .limb import Wing, Tail
from .skin import Scales


class ReptileBodyPart(BodyPart):
    scales = BodyPart.child_property(Scales)


class ReptileWing(Wing):
    default_name = 'wing'
    scales = Wing.child_property(Scales)


class ReptileHead(ReptileBodyPart):
    default_name = 'head'


class ReptileLeg(ReptileBodyPart):
    default_name = 'leg'


class ReptileBody(ReptileBodyPart):
    default_name = 'body'

    heads = ReptileBodyPart.children_property(ReptileHead)
    legs = ReptileBodyPart.children_property(ReptileLeg)
    wings = ReptileBodyPart.children_property(ReptileWing)
    tails = ReptileBodyPart.children_property(Tail)
    flesh = ReptileBodyPart.child_property(Flesh)
