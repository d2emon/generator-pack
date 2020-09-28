"""
- Knee
- Toenail
- Toe
- Foot
- Leg
"""
from .body_parts import BodyPart


class Knee(BodyPart):
    pass


class Toenail(BodyPart):
    # dust = BodyPart.child_property(Dust)
    # keratin = BodyPart.child_property(Keratin)
    pass


class Toe(BodyPart):
    nail = BodyPart.child_property(Toenail)


class Foot(BodyPart):
    toes = BodyPart.children_property(Toe)
    # sweat = BodyPart.child_property(Sweat)


class Leg(BodyPart):
    foot = BodyPart.child_property(Foot)
    knee = BodyPart.child_property(Knee)
