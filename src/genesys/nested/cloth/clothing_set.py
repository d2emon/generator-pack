from genesys.nested.factories.nested_factory import NestedFactory
from models.v5 import cloth

# ???
from .clothing import HatFactory, GlassesFactory, PantsFactory, ShirtFactory, CoatFactory, SocksFactory, \
    ShoesFactory, UnderwearFactory


class ClothingSetFactory(NestedFactory):
    model = cloth.ClothingSet

    def children(self):
        yield HatFactory.probable(2)
        yield GlassesFactory.probable(20)
        yield PantsFactory.probable(98)
        yield ShirtFactory.probable(98)
        yield CoatFactory.probable(50)
        yield SocksFactory.probable(80)
        yield ShoesFactory.probable(80)
        yield UnderwearFactory.probable(99)
