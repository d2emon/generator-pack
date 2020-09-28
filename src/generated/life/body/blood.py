"""
- BloodCell
- Blood
- BloodVessels
"""
from genesys.model.model import Model
from ..cell import Cell


class BloodCell(Cell):
    default_name = 'blood cells'


class Blood(Model):
    cells = Model.child_property(Cell)


class BloodVessels(Model):
    blood = Model.child_property(Cell)
    # bacterias = Model.children_property(Bacteria)
