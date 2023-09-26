"""
- Fire
- Ash
"""
from models.tree_model import TreeModel as Model
from .elements import Atom
from .matter import Matter


class Fire(Model):
    atoms = Model.children_property(Atom)


class Ash(Matter):
    contents = Matter.children_property(Matter)
