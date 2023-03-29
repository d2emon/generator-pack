"""
- TextileFibre
- Textile
- Fabric
- Leather
- Cloth
"""
from models.tree_model import TreeModel as Model
from ..life.cell import Cell
from ..materials import Keratin


class TextileFibre(Model):
    default_name = 'textile fibres'

    keratin = Model.child_property(Keratin)


class Textile(Model):
    fibres = Model.child_property(TextileFibre)


class Fabric(Model):
    pass


class Leather(Fabric):
    cells = Fabric.child_property(Cell)


class Cloth(Fabric):
    textile = Fabric.child_property(Textile)
    leather = Fabric.child_property(Leather)
