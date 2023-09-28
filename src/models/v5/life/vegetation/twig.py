"""
- PlantCell
- Twig
"""
from models.nested_model import NestedModel as Model
from ...materials import Dew
from ..cell import Cell


class PlantCell(Cell):
    default_name = 'plant cells'


class Twig(Model):
    dew = Model.child_property(Dew)
    # worms = Model.children_property(Worm)
    # insects = Model.children_property(Insect)
    cells = Model.child_property(PlantCell)
