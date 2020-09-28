from generated.nested_v2.models import Dust
from genesys.nested.factories.v2.thing_builder import ThingBuilder
from genesys.nested.models import Model
from generated.life.cell import Cell
from ..single_celled import Bacteria
from generated.materials.chemistry import Sweat


class SkinCell(Cell):
    default_name = 'skin cells'


class DeadSkin(SkinCell):
    default_name = 'skin cell'


class Pores(Model):
    bacterias = Model.children_property(Bacteria)
    cells = Model.children_property(Cell)
    sweat = Model.child_property(Sweat)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield Bacteria.multiple(1, 3)
                yield SkinCell
                yield DeadSkin.probable(50)
                yield Sweat.probable(40)


class Scar(Model):
    cells = Model.child_property(Cell)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield DeadSkin


class Skin(Model):
    bacterias = Model.children_property(Bacteria)
    scar = Model.child_property(Scar)
    pores = Model.child_property(Pores)
    cells = Model.children_property(Cell)
    dust = Model.child_property(Dust)
    sweat = Model.child_property(Sweat)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield Bacteria.multiple(1, 3)
                yield Scar.probable(0.5)
                yield Pores
                yield SkinCell
                yield DeadSkin
                yield Dust.probable(20)
                yield Sweat.probable(20)


class Dandruff(Model):
    cells = Model.child_property(Cell)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield DeadSkin
