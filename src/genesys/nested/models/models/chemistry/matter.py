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
from genesys.nested.models import Model
from .elements import elements
from .particles import Atom


class Molecule(Model):
    atoms = Model.child_property(Atom)

    default_name = 'molecules'

    class Factory(Model.Factory):
        def children(self):
            yield Atom

    @classmethod
    def from_atoms(cls, *components):
        return map(lambda component: elements.get(component), components)


class Matter(Molecule):
    molecules = Model.child_property(Atom, Molecule)

    default_name = None


class Ammonia(Matter):
    class Factory(Matter.Factory):
        def children(self):
            yield from Matter.from_atoms('N', 'H')


class Salt(Matter):
    class Factory(Matter.Factory):
        def children(self):
            yield from Matter.from_atoms('Na', 'Cl')


class Silica(Matter):
    class Factory(Matter.Factory):
        def children(self):
            yield from Matter.from_atoms('Si', 'O')


class Steel(Matter):
    class Factory(Matter.Factory):
        def children(self):
            yield from Matter.from_atoms('Fe', 'C')
