from genesys.nested.models import Model
from ...chemistry import elements, Lipids
from ..cell import Cell


class BoneCell(Cell):
    class NameFactory(Cell.NameFactory):
        default = 'bone cells'


class Bones(Model):
    cells = Model.child_property(Cell)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield BoneCell
            yield elements['Ca']


class Bone(Bones):
    pass


class MuscleCell(Cell):
    class NameFactory(Cell.NameFactory):
        default = 'muscle cells'


class Muscles(Model):
    cells = Model.child_property(Cell)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield MuscleCell


class Fat(Model):
    lipids = Model.child_property(Lipids)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Lipids
