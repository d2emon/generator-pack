from ..unknown import Dust, Crumbs, Lint, Donut, Coin, Pen, Button, Note, Handgun, Pasta, Glass, Metal
from genesys.nested.models import Model
from .fabric import Cloth, Textile, Leather
from ..biology import DeadSkin
from ..chemistry import Sweat, Plastic


class Clothing(Cloth):
    class ChildrenFactory(Cloth.ChildrenFactory):
        def children_classes(self):
            yield Textile
            yield DeadSkin.probable(40)
            yield Sweat.probable(15)


class Pocket(Model):
    class ChildrenFactory(Cloth.ChildrenFactory):
        def children_classes(self):
            yield Dust.probable(20)
            yield Crumbs.probable(20)
            yield Lint.probable(30)
            yield Donut.probable(1)
            yield Coin.probable(20)
            yield Coin.probable(20)
            yield Coin.probable(10)
            yield Pen.probable(10)
            yield Pen.probable(2)
            yield Button.probable(10)
            yield Button.probable(5)
            yield Button.probable(1)
            yield Note.probable(15)
            yield Note.probable(5)
            yield Handgun.probable(0.4)
            yield Pasta.probable(0.2)
            yield Textile


class Pants(Clothing):
    class BaseFactory(Clothing.BaseFactory):
        default = ['pants', 'trousers', 'sweatpants', 'bermuda shorts', 'shorts', 'jeans', 'cargo pants']

    class ChildrenFactory(Clothing.ChildrenFactory):
        def children_classes(self):
            yield Pocket.multiple(0, 4)
            yield from super().children_classes()


class Shirt(Clothing):
    class BaseFactory(Clothing.BaseFactory):
        default = ['shirt', 'sweater', 't-shirt']


class Underwear(Clothing):
    pass


class Coat(Clothing):
    class BaseFactory(Clothing.BaseFactory):
        default = ['coat', 'jacket', 'hoodie']

    class ChildrenFactory(Clothing.ChildrenFactory):
        @classmethod
        def children_classes(cls):
            yield Pocket.multiple(0, 4)
            yield from super().children_classes()
            yield Leather.probable(30)


class CozyVonPocketworth(Clothing):
    class NameFactory(Clothing.NameFactory):
        default = 'Cozy von Pocketworth'

    class ChildrenFactory(Clothing.ChildrenFactory):
        @classmethod
        def children_classes(cls):
            yield Pocket.multiple(20, 40)
            yield from super().children_classes()
            yield Leather.probable(30)


class Socks(Clothing):
    pass


class Shoes(Clothing):
    class BaseFactory(Clothing.BaseFactory):
        default = ['shoes', 'boots', 'sneakers', 'sandals']

    class ChildrenFactory(Clothing.ChildrenFactory):
        @classmethod
        def children_classes(cls):
            yield Leather.probable(40)
            yield Plastic


class Hat(Clothing):
    class BaseFactory(Clothing.BaseFactory):
        default = ['cap', 'hat', 'hat', 'hat', 'hat', 'beret', 'party hat', 'top-hat']


class Glasses(Clothing):
    class BaseFactory(Clothing.BaseFactory):
        default = ['glasses', 'glasses', 'glasses', 'sunglasses', 'monocle', 'ski mask']

    class ChildrenFactory(Clothing.ChildrenFactory):
        @classmethod
        def children_classes(cls):
            yield Plastic
            yield Glass
            yield Metal.probable(10)
