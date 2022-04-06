"""
- Plate
"""
from models.v4.model import Model
from ...materials import Rock, Ice


class Plate(Model):
    minerals = Model.children_property(Rock)
    ice = Model.children_property(Ice)