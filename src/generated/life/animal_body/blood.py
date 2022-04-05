"""
- BloodCell
- Blood
- BloodVessels
"""
from models.v4.model import Model
from ..cell import Cell
from ..single_celled import Bacteria


class BloodCell(Cell):
    default_name = 'blood cells'


class Blood(Model):
    cells = Model.child_property(Cell)


class BloodVessels(Model):
    blood = Model.child_property(Cell)
    bacterias = Model.children_property(Bacteria)
