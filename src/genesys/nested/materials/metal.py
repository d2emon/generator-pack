from factories.thing.nested_factory import NestedFactory as Factory
from models.v5 import materials
from .elements import AtomFactory


class MetalFactory(Factory):
    contents = []

    def children(self):
        for element in self.contents:
            yield AtomFactory.element_factory(element)


class IronFactory(MetalFactory):
    model = materials.Iron
    contents = 'Fe',


class SteelFactory(MetalFactory):
    model = materials.Steel
    contents = 'Fe', 'C',
