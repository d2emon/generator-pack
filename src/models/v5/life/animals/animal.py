"""
- AnimalBody
- Animal
"""
from models.nested_model import NestedModel as Model
from ...mind import Psyche
from ..animal_body.head.eye import SimpleEye
from ..animal_body.head.mouth import SimpleMouth
from ..animal_body.skin import Exoskeleton
from ..animal_body.body_parts import Flesh
from ..animal_body.jelly import Jelly


class AnimalBody(Model):
    default_name = 'body'

    eyes = Model.children_property(SimpleEye)
    mouths = Model.children_property(SimpleMouth)
    exoskeleton = Model.children_property(Exoskeleton)
    flesh = Model.children_property(Flesh)
    jelly = Model.children_property(Jelly)


class Animal(Model):
    body = Model.child_property(AnimalBody)
    psyche = Model.child_property(Psyche)
