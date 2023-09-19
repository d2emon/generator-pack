from models.v5 import materials
from factories.thing.nested_factory import NestedFactory as Factory
from .elements import AtomFactory
from .matter import MoleculeFactory
from .minerals import CarbonFactory
from .organics import OrganicFactory


class FireFactory(Factory):
    model = materials.Fire

    def children(self):
        yield from AtomFactory.element_factories('C', 'O')


class AshFactory(Factory):
    model = materials.Ash

    def children(self):
        yield OrganicFactory.one()
        yield CarbonFactory.one()
