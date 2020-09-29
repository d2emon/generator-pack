"""
- BrainCell
- Brain
"""
from ...cell import Cell
from ...animal_body.body_parts import BodyPart


class BrainCell(Cell):
    default_name = 'mind cells'


class Brain(BodyPart):
    # bacterias = SoftBodyPart.children_property(Bacteria)
    cells = BodyPart.child_property(BrainCell)
