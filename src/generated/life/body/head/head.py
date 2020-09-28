"""
- Skull
- Head
"""
from ..body_parts import BodyPart
from .brain import Brain
from .eye import Eye
from .ear import Ear
from .hair import Hair
from .nose import Nose
from .mouth import Mouth


class Skull(BodyPart):
    brain = BodyPart.child_property(Brain)


class Head(BodyPart):
    mouths = BodyPart.children_property(Mouth)
    noses = BodyPart.children_property(Nose)
    eyes = BodyPart.children_property(Eye)
    ears = BodyPart.children_property(Ear)
    skull = BodyPart.child_property(Skull)
    hair = BodyPart.child_property(Hair)
