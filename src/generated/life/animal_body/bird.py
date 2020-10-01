"""
- Bird Limb
- Bird Wing
- Bird Leg
- Bird Tail
- Beak
- BirdHead
- BirdBody
"""
from .body_parts import BodyPart, Flesh
from .limb import Limb, Wing
from .head import Eye, Skull


class BirdLimb(Limb):
    # feathers = Limb.child_property(Feathers)
    pass


class BirdWing(BirdLimb):
    default_name = 'wing'


class BirdLeg(BirdLimb):
    default_name = 'leg'


class BirdTail(BirdLimb):
    default_name = 'tail'


class Beak(BodyPart):
    pass


class BirdHead(BodyPart):
    default_name = 'head'

    # feathers = Limb.child_property(Feathers)
    beaks = BodyPart.children_property(Beak)
    eyes = BodyPart.children_property(Eye)
    skull = BodyPart.child_property(Skull)


class BirdBody(BodyPart):
    default_name = 'body'

    # feathers = Limb.child_property(Feathers)
    heads = BodyPart.children_property(BirdHead)
    legs = BodyPart.children_property(BirdLeg)
    wings = BodyPart.children_property(Wing)
    tails = BodyPart.children_property(BirdTail)
    flesh = BodyPart.child_property(Flesh)
