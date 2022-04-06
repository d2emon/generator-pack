"""
- PlanetCore
"""
from models.nested_model import NestedModel
from models.v5.materials import Rock
from models.v5.life import Life


class PlanetCore(NestedModel):
    life = NestedModel.child_property(Life)
    minerals = NestedModel.children_property(Rock)

    default_name = 'core'
