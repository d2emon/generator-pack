from generated import cloth
from ..factory import Factory
from ..materials import SweatFactory
from ..life.body.skin import DeadSkinFactory
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

    # class BaseFactory(Clothing.BaseFactory):
    #      default = ['pants', 'trousers', 'sweatpants', 'bermuda shorts', 'shorts', 'jeans', 'cargo pants']

    def children(self):
        yield PocketFactory().multiple(0, 4)
        yield from super().children()


class ShirtFactory(ClothingFactory):
    default_model = cloth.Shirt

    # class BaseFactory(Clothing.BaseFactory):
    #     default = ['shirt', 'sweater', 't-shirt']


class UnderwearFactory(ClothingFactory):
    default_model = cloth.Underwear


class CoatFactory(ClothingFactory):
    # class BaseFactory(Clothing.BaseFactory):
    #     default = ['coat', 'jacket', 'hoodie']

    @classmethod
    def children_classes(cls):
        yield PocketFactory().multiple(0, 4)
        yield LeatherFactory().probable(30)
        yield from super().children()
