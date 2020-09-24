from generated.materials import Molecule, Ammonia, Silica, Steel
from ..factory import Factory
from .elements import element_factories


class MoleculeFactory(Factory):
    default_model = Molecule

    @classmethod
    def elements(cls, *elements):
        return (element_factories.get(element, lambda: None)() for element in elements)

    @classmethod
    def from_atoms(cls, *atoms):
        return cls(placeholders=atoms)

    @classmethod
    def from_elements(cls, *elements):
        return cls.from_atoms(*cls.elements(*elements))


class AmmoniaFactory(Factory):
    default_model = Ammonia

    def children(self):
        yield MoleculeFactory.from_elements('N', 'H')


class SteelFactory(Factory):
    default_model = Steel

    def children(self):
        yield MoleculeFactory.from_elements('Fe', 'C')
