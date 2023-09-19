from factories.thing.nested_factory import NestedFactory
from models.v5 import materials
from .elements import AtomFactory
from .minerals import CarbonFactory
from .organics import OrganicFactory


class FireFactory(NestedFactory):
    model = materials.Fire

    def children(self):
        yield AtomFactory.element_factory('C')
        yield AtomFactory.element_factory('O')


class AshFactory(NestedFactory):
    model = materials.Ash

    def children(self):
        yield OrganicFactory.one()
        yield CarbonFactory.one()
