"""
- Knee
- Toenail
- Toe
- Foot
- Leg
"""
from ...materials import Keratin
from ..animal_body.body_parts import BodyPart
from ..animal_body.limb import Limb


class Knee(BodyPart):
    pass


class Toenail(BodyPart):
    # dust = BodyPart.child_property(Dust)
    keratin = BodyPart.child_property(Keratin)


class Toe(BodyPart):
    nail = BodyPart.child_property(Toenail)


class Foot(BodyPart):
    toes = BodyPart.children_property(Toe)


class Leg(Limb):
    foot = BodyPart.child_property(Foot)
    knee = BodyPart.child_property(Knee)
