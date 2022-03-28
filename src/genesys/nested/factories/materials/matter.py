from generated import materials
from factories.nested_factory import NestedFactory as Factory
from .elements import element_factories


class MoleculeFactory(Factory):
    default_model = materials.Molecule

    @classmethod
    def elements(cls, *elements):
        return (element_factories.get(element, lambda: None)() for element in elements)

    @classmethod
    def from_atoms(cls, *atoms):
        return cls(placeholders=atoms)

    @classmethod
    def from_elements(cls, *elements):
        return cls.from_atoms(*cls.elements(*elements))


class SteelFactory(Factory):
    default_model = materials.Steel

    def children(self):
        yield MoleculeFactory.from_elements('Fe', 'C')
