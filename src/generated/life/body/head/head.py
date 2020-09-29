"""
- Skull
- Head
- HeadHair
- Dandruff
"""
from genesys.model.model import Model
from ...animal_body.body_parts import BodyPart
from ...animal_body.hair import Hair
from ...cell import Cell
from .brain import Brain
from .eye import Eye
from .ear import Ear
from .nose import Nose
from .mouth import Mouth


class Skull(BodyPart):
    brain = BodyPart.child_property(Brain)


class Dandruff(Model):
    cells = Model.child_property(Cell)


class HeadHair(Hair):
    default_name = 'hair'

    dandruff = Hair.children_property(Dandruff)


class Head(BodyPart):
    mouths = BodyPart.children_property(Mouth)
    noses = BodyPart.children_property(Nose)
    eyes = BodyPart.children_property(Eye)
    ears = BodyPart.children_property(Ear)
    skull = BodyPart.child_property(Skull)
    hair = BodyPart.child_property(Hair)
