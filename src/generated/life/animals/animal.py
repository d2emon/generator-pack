"""
- AnimalBody
- Animal
"""
from genesys.model.model import Model
from ...mind import Psyche
from ..animal_body import SimpleEye, SimpleMouth, Exoskeleton, Flesh, Jelly


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
