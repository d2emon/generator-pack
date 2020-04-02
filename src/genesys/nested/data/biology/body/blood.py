from ...unknown import Bacteria
from genesys.nested.models import Model
from ..cell import Cell


class BloodCell(Cell):
    class NameFactory(Model.NameFactory):
        default = 'blood cells'


class Blood(Model):
    cells = Model.child_property(Cell)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield BloodCell


class BloodVessels(Model):
    blood = Model.child_property(Cell)
    bacterias = Model.children_property(Bacteria)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Bacteria.probable(30)
            yield Blood
