from models.v5 import life
from factories.nested_factory import NestedFactory as Factory
from ...materials import KeratinFactory
from ..single_celled import BacteriaFactory


class HairFactory(Factory):
    default_model = life.Hair

    def children(self):
        yield BacteriaFactory().probable(30)
        yield KeratinFactory()


class FurFactory(HairFactory):
    default_model = life.Fur

    def children(self):
        yield KeratinFactory()


class WhiskersFactory(FurFactory):
    default_model = life.Whiskers
