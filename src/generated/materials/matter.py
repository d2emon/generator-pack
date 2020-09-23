"""
- Molecule
- Diamond
- Magma
- Rock
- Silica
- Salt
- Fire
- Steel
"""
from genesys.model.model import Model
from .elements import Atom


class Molecule(Model):
    default_name = 'molecules'

    atoms = Model.children_property(Atom)


class Matter(Molecule):
    SOLID = 0
    LIQUID = 1
    GAS = 2

    state = SOLID

    molecules = Model.children_property(Atom, Molecule)


class Gas(Matter):
    state = Matter.GAS


class Ammonia(Gas):
    pass


class Steel(Matter):
    pass
