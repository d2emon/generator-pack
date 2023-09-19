from models.v5 import materials
from factories.thing.nested_factory import NestedFactory as Factory
from .elements import AtomFactory


class MoleculeFactory(Factory):
    contents = 'N', 'H'
    default_name = 'molecules'
    model = materials.Molecule

    @classmethod
    def element_factory(cls, element):
        return AtomFactory.element_factory(element)

    @classmethod
    def element_factories(cls, *elements):
        return AtomFactory.element_factories(*elements)

    def children(self):
        yield from self.element_factories(*self.contents)


class SteelFactory(Factory):
    model = materials.Steel
    contents = 'Fe', 'C'
