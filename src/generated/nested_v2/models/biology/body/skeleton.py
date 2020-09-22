from genesys.nested.factories.thing_builder import ThingBuilder
from genesys.nested.models import Model
from generated.chemistry import elements, Lipids
from ..cell import Cell


class BoneCell(Cell):
    default_name = 'bone cells'


class Bones(Model):
    cells = Model.child_property(Cell)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield BoneCell
                yield elements['Ca']


class Bone(Bones):
    pass


class MuscleCell(Cell):
    default_name = 'muscle cells'


class Muscles(Model):
    cells = Model.child_property(Cell)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield MuscleCell


class Fat(Model):
    lipids = Model.child_property(Lipids)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield Lipids
