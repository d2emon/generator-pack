from genesys.nested.factories.nested_factory import NestedFactory
from models.universe import god
from utils.nested import select_item
from ..life.human.body import BodyFactory
from ..temporary import ComputerFactory

from ..unsorted_cloth import ClothingSetFactory


class D2emonThoughtsFactory(NestedFactory):
    model = god.GodThoughts

    def name_factory(self, data, *args, **kwargs):
        return select_item(*data.d2emon_thoughts)


class D2emonPsycheFactory(NestedFactory):
    model = god.GodPsyche

    def children(self):
        yield D2emonThoughtsFactory.one()


class D2emonFactory(NestedFactory):
    default_name = 'D2emon'
    model = god.God

    def children(self):
        yield BodyFactory.one()
        yield D2emonPsycheFactory.one()
        yield ClothingSetFactory.one()
        yield ComputerFactory.one()


class GodFactory(D2emonFactory):
    pass
