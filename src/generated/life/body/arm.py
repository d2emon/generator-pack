"""
- ArmpitHair
- Armpit
- Elbow
- Fingernail
- Finger
- Hand
- Arm
"""
from ...materials import Keratin
from ..animal_body.body_parts import BodyPart
from ..animal_body.hair import Hair
from ..animal_body.limb import Limb


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


class Arm(Limb):
    hand = BodyPart.child_property(Hand)
    elbow = BodyPart.child_property(Elbow)
    armpit = BodyPart.child_property(Armpit)
