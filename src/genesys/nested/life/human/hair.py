from genesys.nested.factories.nested_factory import NestedFactory
from models.v5 import life
from ..body.skin import DeadSkinFactory

from ...unsorted_organics import KeratinFactory
# ???
from ..single_celled import BacteriaFactory


class HairFactory(NestedFactory):
    model = life.Hair

    def children(self):
        yield BacteriaFactory.probable(30)
        yield KeratinFactory.one()


class FurFactory(HairFactory):
    # TODO: Refactor it
    default_model = life.Fur

    def children(self):
        yield KeratinFactory()


class WhiskersFactory(FurFactory):
    # TODO: Refactor it
    default_model = life.Whiskers
