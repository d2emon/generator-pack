from genesys.nested.factories.nested_factory import NestedFactory
from models.v5 import life
from .skin import DeadSkinFactory

# ???
from ...materials import KeratinFactory
# ???
from ..single_celled import BacteriaFactory


class DandruffFactory(NestedFactory):
    model = life.Dandruff

    def children(self):
        yield DeadSkinFactory()


class HairFactory(NestedFactory):
    # TODO: Refactor it
    default_model = life.Hair

    def children(self):
        yield BacteriaFactory().probable(30)
        yield KeratinFactory()


class FurFactory(HairFactory):
    # TODO: Refactor it
    default_model = life.Fur

    def children(self):
        yield KeratinFactory()


class WhiskersFactory(FurFactory):
    # TODO: Refactor it
    default_model = life.Whiskers
