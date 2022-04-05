"""
- Skull
"""
from ..body_parts import BodyPart
from .brain import Brain


class Skull(BodyPart):
    brain = BodyPart.child_property(Brain)
