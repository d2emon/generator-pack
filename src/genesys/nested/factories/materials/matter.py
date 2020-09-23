from generated.materials import Molecule, Ammonia, Silica, Steel
from ..factory import Factory
from .elements import element_factories


class MoleculeFactory(Factory):
    default_model = Molecule

    @classmethod
    def from_atoms(cls, *atoms):
        print(cls, atoms)
        return cls(placeholders=atoms)

    @classmethod
    def from_elements(cls, *elements):
        return cls(placeholders=(element_factories.get(element, lambda: None)() for element in elements))


class AmmoniaFactory(Factory):
    default_model = Ammonia

    def children(self):
        yield MoleculeFactory.from_elements('N', 'H')


class SilicaFactory(Factory):
    default_model = Silica

    def children(self):
        yield MoleculeFactory.from_elements('Si', 'O')


class SteelFactory(Factory):
    default_model = Steel

    def children(self):
        yield MoleculeFactory.from_elements('Fe', 'C')
