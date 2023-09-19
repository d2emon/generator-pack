from factories.thing.nested_factory import NestedFactory as Factory
from models.v5 import materials
from .elements import AtomFactory


class MoleculeFactory(Factory):
    contents = []
    model = materials.Molecule

    @classmethod
    def element_factory(cls, element):
        return AtomFactory.element_factory(element)

    @classmethod
    def element_factories(cls, *elements):
        return AtomFactory.element_factories(*elements)

    def children(self):
        yield from self.element_factories(*self.contents)


class SaltFactory(MoleculeFactory):
    model = materials.Salt
    contents = 'Na', 'Cl'


class SilicaFactory(MoleculeFactory):
    model = materials.Silica
    contents = 'Si', 'O'
