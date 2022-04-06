"""
- PlanetCore
"""
from models.nested_model import NestedModel as Model
from ...materials import Rock
from ...life import Life


class PlanetCore(Model):
    life = Model.child_property(Life)
    minerals = Model.children_property(Rock)

    default_name = 'core'
