from factories.thing.nested_factory import NestedFactory as Factory
from models.v5 import materials
from .elements import AtomFactory
from .minerals import CarbonFactory
from .organics import OrganicFactory


class FireFactory(Factory):
    model = materials.Fire

    def children(self):
        yield AtomFactory.element_factory('C')
        yield AtomFactory.element_factory('O')


class AshFactory(Factory):
    model = materials.Ash

    def children(self):
        yield OrganicFactory.one()
        yield CarbonFactory.one()
