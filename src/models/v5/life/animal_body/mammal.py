"""
- MammalLeg
- MammalHead
- MammalBody
"""
from .body_parts import BodyPart, Flesh
from .limb import Limb, Tail
from .hair import Fur, Whiskers
from .head import Mouth, Nose, Eye, Ear, Skull


class MammalLeg(Limb):
    default_name = 'leg'

    fur = Limb.child_property(Fur)


class MammalHead(BodyPart):
    default_name = 'head'

    mouths = BodyPart.children_property(Mouth)
    noses = BodyPart.children_property(Nose)
    whiskers = BodyPart.child_property(Whiskers)
    eyes = BodyPart.children_property(Eye)
    ears = BodyPart.children_property(Ear)
    skull = BodyPart.child_property(Skull)
    fur = Limb.child_property(Fur)


class MammalBody(BodyPart):
    default_name = 'body'

    heads = BodyPart.children_property(MammalHead)
    leg = BodyPart.children_property(MammalLeg)
    tails = BodyPart.children_property(Tail)
    flesh = BodyPart.child_property(Flesh)
    fur = Limb.child_property(Fur)
