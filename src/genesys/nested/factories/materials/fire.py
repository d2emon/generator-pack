from generated import materials
from factories.nested_factory import NestedFactory as Factory
from .matter import MoleculeFactory
from .minerals import CarbonFactory
from .organics import OrganicFactory


class FireFactory(Factory):
    default_model = materials.Fire

    def children(self):
        yield from MoleculeFactory.elements('C', 'O')


class AshFactory(Factory):
    default_model = materials.Ash

    def children(self):
        yield OrganicFactory()
        yield CarbonFactory()
