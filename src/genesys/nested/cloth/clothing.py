from models.v5 import cloth
from factories.thing.nested_factory import NestedFactory as Factory
from ..materials import SweatFactory, PlasticFactory
from genesys.nested.factories.life.animal_body.skin import DeadSkinFactory
from .fabric import TextileFactory, LeatherFactory


class ClothingFactory(Factory):
    default_model = cloth.Clothing

    def children(self):
        yield TextileFactory()
        yield DeadSkinFactory().probable(40)
        yield SweatFactory().probable(15)


class PocketFactory(Factory):
    default_model = cloth.Pocket

    def children(self):
        # yield Dust.probable(20)
        # yield Crumbs.probable(20)
        # yield Lint.probable(30)
        # yield Donut.probable(1)
        # yield Coin.probable(20)
        # yield Coin.probable(20)
        # yield Coin.probable(10)
        # yield Pen.probable(10)
        # yield Pen.probable(2)
        # yield Button.probable(10)
        # yield Button.probable(5)
        # yield Button.probable(1)
        # yield Note.probable(15)
        # yield Note.probable(5)
        # yield Handgun.probable(0.4)
        # yield Pasta.probable(0.2)
        yield TextileFactory()


class PantsFactory(ClothingFactory):
    default_model = cloth.Pants
    names = [
        'pants', 'trousers', 'sweatpants', 'bermuda shorts', 'shorts', 'jeans', 'cargo pants',
    ]

    def generate_name(self):
        return self.select_item(*self.names)

    def children(self):
        yield PocketFactory().multiple(0, 4)
        yield from super().children()


class ShirtFactory(ClothingFactory):
    default_model = cloth.Shirt
    names = [
        'shirt', 'sweater', 't-shirt',
    ]

    def generate_name(self):
        return self.select_item(*self.names)


class UnderwearFactory(ClothingFactory):
    default_model = cloth.Underwear


class CoatFactory(ClothingFactory):
    default_model = cloth.Coat
    names = [
        'coat', 'jacket', 'hoodie',
    ]

    def generate_name(self):
        return self.select_item(*self.names)

    def children(self):
        yield PocketFactory().multiple(0, 4)
        yield LeatherFactory().probable(30)
        yield from super().children()


class CozyVonPocketworthFactory(CoatFactory):
    default_name = 'Cozy von Pocketworth'

    def children(self):
        yield PocketFactory().multiple(20, 40)
        yield LeatherFactory().probable(30)
        yield from super().children()


class SocksFactory(ClothingFactory):
    default_model = cloth.Socks


class ShoesFactory(ClothingFactory):
    default_model = cloth.Shoes
    names = [
        'shoes', 'boots', 'sneakers', 'sandals',
    ]

    def generate_name(self):
        return self.select_item(*self.names)

    def children(self):
        yield LeatherFactory().probable(40)
        yield PlasticFactory()


class HatFactory(ClothingFactory):
    default_model = cloth.Hat
    names = [
        'cap', 'hat', 'hat', 'hat', 'hat', 'beret', 'party hat', 'top-hat',
    ]

    def generate_name(self):
        return self.select_item(*self.names)


class GlassesFactory(ClothingFactory):
    default_model = cloth.Glasses
    names = [
        'glasses', 'glasses', 'glasses', 'sunglasses', 'monocle', 'ski mask',
    ]

    def generate_name(self):
        return self.select_item(*self.names)

    def children(self):
        yield PlasticFactory()
        # yield Glass
        # yield Metal.probable(10)
