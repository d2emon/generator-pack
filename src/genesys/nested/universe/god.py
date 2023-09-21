from genesys.nested.factories.nested_factory import NestedFactory
from models.v5 import universe
from utils.nested import select_item
from ..cloth import ClothingSetFactory
from ..life import BodyFactory
from ..temporary import ComputerFactory


class D2emonThoughtsFactory(NestedFactory):
    model = universe.GodThoughts

    def name_factory(self, data, *args, **kwargs):
        return select_item(*data.d2emon_thoughts)


class D2emonPsycheFactory(NestedFactory):
    model = universe.GodPsyche

    def children(self):
        yield D2emonThoughtsFactory.one()


class D2emonFactory(NestedFactory):
    default_name = 'D2emon'
    model = universe.God

    def children(self):
        yield BodyFactory.one()
        yield D2emonPsycheFactory.one()
        yield ClothingSetFactory.one()
        yield ComputerFactory.one()


class GodFactory(D2emonFactory):
    # TODO: Refactor it
    pass
