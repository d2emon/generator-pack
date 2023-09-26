from genesys.nested.factories.nested_factory import NestedFactory
from models.materials import fire
from .elements import AtomFactory
from .minerals import CarbonFactory
from .organics import OrganicFactory


class FireFactory(NestedFactory):
    model = fire.Fire

    def children(self):
        yield AtomFactory.element_factory('C')
        yield AtomFactory.element_factory('O')


class AshFactory(NestedFactory):
    model = fire.Ash

    def children(self):
        yield OrganicFactory.one()
        yield CarbonFactory.one()
