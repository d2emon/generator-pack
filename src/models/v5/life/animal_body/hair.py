"""
- Hair
- Fur
- Whiskers
"""
from models.tree_model import TreeModel as Model
from ...materials import Keratin
from ..single_celled import Bacteria


class Hair(Model):
    bacterias = Model.child_property(Bacteria)
    keratin = Model.child_property(Keratin)


class Fur(Hair):
    pass


class Whiskers(Hair):
    pass
