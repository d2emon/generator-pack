"""
- BrainCell
- Brain
"""
from ...cell import Cell
from ...single_celled import Bacteria
from ..body_parts import BodyPart


class BrainCell(Cell):
    default_name = 'mind cells'


class Brain(BodyPart):
    bacterias = BodyPart.children_property(Bacteria)
    cells = BodyPart.child_property(BrainCell)
