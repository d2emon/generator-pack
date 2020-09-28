"""
- Dandruff
- Hair
- HeadHair
"""
from genesys.model.model import Model
from ...cell import Cell


class Dandruff(Model):
    cells = Model.child_property(Cell)


class Hair(Model):
    # bacterias = Model.child_property(Bacteria)
    # keratin = Model.child_property(Keratin)
    pass


class HeadHair(Hair):
    default_name = 'hair'

    dandruff = Model.children_property(Dandruff)
