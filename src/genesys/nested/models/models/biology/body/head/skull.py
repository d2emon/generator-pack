from genesys.nested.models.models.unknown import Bacteria
from ..body_parts import SoftBodyPart
from ..skeleton import Bones
from ...cell import Cell


class BrainCell(Cell):
    default_name = 'mind cells'


class Brain(SoftBodyPart):
    bacterias = SoftBodyPart.children_property(Bacteria)
    cells = SoftBodyPart.child_property(BrainCell)

    class Factory(SoftBodyPart.Factory):
        class ChildrenFactory(SoftBodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Bacteria.probable(20)
                yield BrainCell


class Skull(Bones):
    brain = Bones.child_property(Brain)

    class Factory(Bones.Factory):
        class ChildrenFactory(Bones.Factory.ChildrenFactory):
            def builders(self):
                yield Brain
                yield from super().builders()
