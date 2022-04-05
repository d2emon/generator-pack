"""
- PlanetCore
"""
from models.v4.model import Model
from ...materials import Rock
from ...life import Life


class PlanetCore(Model):
    life = Model.child_property(Life)
    minerals = Model.children_property(Rock)

    default_name = 'core'
