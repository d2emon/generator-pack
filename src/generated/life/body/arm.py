"""
- ArmpitHair
- Armpit
- Elbow
- Fingernail
- Finger
- Hand
- Arm
"""
from ...materials import Sweat, Keratin
from .body_parts import BodyPart
from .head import Hair


class ArmpitHair(Hair):
    default_name = 'hair'


class Armpit(BodyPart):
    hair = BodyPart.child_property(Hair)


class Elbow(BodyPart):
    pass


class Fingernail(BodyPart):
    # dust = BodyPart.child_property(Dust)
    keratin = BodyPart.child_property(Keratin)


class Finger(BodyPart):
    nail = BodyPart.child_property(Fingernail)


class Hand(BodyPart):
    fingers = BodyPart.children_property(Finger)


class Arm(BodyPart):
    hand = BodyPart.child_property(Hand)
    elbow = BodyPart.child_property(Elbow)
    armpit = BodyPart.child_property(Armpit)
