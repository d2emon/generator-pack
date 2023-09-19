from models.v5 import materials
from factories.thing.nested_factory import NestedFactory as Factory
from .elements import build_elements


class MoleculeFactory(Factory):
    # TODO: Refactor it
    contents = 'N', 'H'
    default_model = materials.Molecule

    def children(self):
        yield from self.elements(*self.contents)

    @classmethod
    def elements(cls, *elements):
        for element in build_elements(*elements):
            yield element.one()

    @classmethod
    def from_atoms(cls, *atoms):
        return cls(placeholders=atoms).one()

    @classmethod
    def from_elements(cls, *elements):
        atoms = build_elements(*elements)
        return cls(placeholders=atoms).one()


class SteelFactory(Factory):
    model = materials.Steel
    contents = ['Fe', 'C']
