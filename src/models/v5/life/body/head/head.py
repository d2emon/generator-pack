"""
- Skull
- Head
- HeadHair
- Dandruff
"""
from models.nested_model import NestedModel as Model
from ...animal_body.body_parts import BodyPart
from ...animal_body.hair import Hair
from ...animal_body.head import Nose, Ear, Eye, Mouth, Skull
from ...cell import Cell


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
