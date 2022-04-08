from models.v5 import cloth
from factories.nested_factory import NestedFactory as Factory
from .clothing import HatFactory, GlassesFactory, PantsFactory, ShirtFactory, CoatFactory, SocksFactory, \
    ShoesFactory, UnderwearFactory


class ClothingSetFactory(Factory):
    default_model = cloth.ClothingSet

    def children(self):
        yield HatFactory().probable(2)
        yield GlassesFactory().probable(20)
        yield PantsFactory().probable(98)
        yield ShirtFactory().probable(98)
        yield CoatFactory().probable(50)
        yield SocksFactory().probable(80)
        yield ShoesFactory().probable(80)
        yield UnderwearFactory().probable(99)
