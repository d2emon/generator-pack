"""
- Limb
- Wing
- Tentacle
- Tail
"""
from .body_parts import BodyPart


class Limb(BodyPart):
    pass


class Wing(BodyPart):
    # feathers = BodyPart.child_property(Feathers)
    pass


class Tentacle(Limb):
    pass


class Tail(BodyPart):
    pass
