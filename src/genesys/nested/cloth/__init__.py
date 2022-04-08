from .clothing_set import ClothingSetFactory
from .fabric import ClothFactory, LeatherFactory, TextileFactory, TextileFibreFactory
from ..materials import KeratinFactory, SweatFactory
from .clothing import ClothingFactory, PocketFactory, PantsFactory, ShirtFactory, UnderwearFactory, CoatFactory, \
    CozyVonPocketworthFactory, SocksFactory, ShoesFactory, HatFactory, GlassesFactory


FACTORIES = {
    'cloth': ClothFactory(),
    'leather': LeatherFactory(),
    'textile': TextileFactory(),
    'textile fibre': TextileFibreFactory(),
    'keratin': KeratinFactory(),
    'sweat': SweatFactory(),
    'clothing': ClothingFactory(),
    'pocket': PocketFactory(),

    'pants': PantsFactory(),
    'shirt': ShirtFactory(),
    'underwear': UnderwearFactory(),
    'coat': CoatFactory(),
    'cozy von pocketworth': CozyVonPocketworthFactory(),
    'socks': SocksFactory(),
    'shoes': ShoesFactory(),
    'hat': HatFactory(),
    'glasses': GlassesFactory(),
}
