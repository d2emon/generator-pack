from genesys.nested.models.models.unknown import Bacteria
from ..body_parts import SoftBodyPart
from ..skeleton import Bones
from ...cell import Cell


class BrainCell(Cell):
    class NameFactory(Cell.NameFactory):
        default = 'brain cells'


class Brain(SoftBodyPart):
    bacterias = SoftBodyPart.children_property(Bacteria)
    cells = SoftBodyPart.child_property(BrainCell)

    class ChildrenFactory(SoftBodyPart.ChildrenFactory):
        def children_classes(self):
            yield Bacteria.probable(20)
            yield BrainCell


class Skull(Bones):
    brain = Bones.child_property(Brain)

    class ChildrenFactory(Bones.ChildrenFactory):
        def children_classes(self):
            yield Brain
            yield from super().children_classes()
