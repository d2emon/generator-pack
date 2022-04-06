"""
- Plate
"""
from models.nested_model import NestedModel
from models.v5.materials import Rock, Ice


class Plate(NestedModel):
    minerals = NestedModel.children_property(Rock)
    ice = NestedModel.children_property(Ice)
