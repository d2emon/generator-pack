"""
- Molecule
- Matter
- Gas
- Ammonia
- Steel
"""
from models.nested_model import NestedModel as Model
from .elements import Atom


class Molecule(Model):
    default_name = 'molecules'

    atoms = Model.children_property(Atom)


class Matter(Model):
    SOLID = 0
    LIQUID = 1
    GAS = 2

    state = SOLID

    molecules = Model.children_property(Atom, Molecule)


class Gas(Matter):
    state = Matter.GAS


class Steel(Matter):
    pass
