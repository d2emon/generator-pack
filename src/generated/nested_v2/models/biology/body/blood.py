from genesys.nested.factories.v2.thing_builder import ThingBuilder
from genesys.nested.models import Model
from ..cell import Cell
from ..single_celled import Bacteria


class BloodCell(Cell):
    default_name = 'blood cells'


class Blood(Model):
    cells = Model.child_property(Cell)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield BloodCell


class BloodVessels(Model):
    blood = Model.child_property(Cell)
    bacterias = Model.children_property(Bacteria)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield Bacteria.probable(30)
                yield Blood
