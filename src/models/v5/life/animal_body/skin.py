"""
- Skin Cell
- DeadSkin
- Pores
- Scar
- Skin
- Scales
- Exoskeleton
"""
from models.nested_model import NestedModel as Model
from models.materials.organics import Chitin
from ...materials import Sweat, Keratin
from ..cell import Cell
from ..single_celled import Bacteria


class SkinCell(Cell):
    default_name = 'skin cells'


class DeadSkin(SkinCell):
    default_name = 'skin cell'


class Pores(Model):
    bacterias = Model.children_property(Bacteria)
    cells = Model.children_property(Cell)
    sweat = Model.child_property(Sweat)


class Scar(Model):
    cells = Model.child_property(Cell)


class Skin(Model):
    # bacterias = Model.children_property(Bacteria)
    scar = Model.child_property(Scar)
    pores = Model.child_property(Pores)
    cells = Model.children_property(Cell)
    # dust = Model.child_property(Dust)
    sweat = Model.child_property(Sweat)


class Scales(Model):
    keratin = Model.child_property(Keratin)


class Exoskeleton(Skin):
    chitin = Skin.child_property(Chitin)
