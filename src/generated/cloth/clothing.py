from genesys.model.model import Model
from ..materials import Sweat
from ..life.body.skin import DeadSkin
from .fabric import Cloth, Textile, Leather



"""
new Thing("clothing",["textile","DeadSkin,40%","sweat,15%"]);
new Thing("pocket",["dust,20%","crumbs,20%","lint,30%","donut,1%","coin,20%","coin,20%","coin,10%","pen,10%","pen,2%","button,10%","button,5%","button,1%","note,15%","note,5%","handgun,0.4%","pasta,0.2%","textile"]);
"""


class Pocket(Model):
    pass


class Clothing(Cloth):
    pockets = Cloth.children_property(Pocket)
    dirt = Cloth.children_property(DeadSkin, Sweat)


class Pants(Clothing):
    pass


class Shirt(Clothing):
    pass


class Underwear(Clothing):
    pass


class Coat(Clothing):
    pass


class CozyVonPocketworth(Clothing):
    pass
    class ChildrenFactory(Clothing.ChildrenFactory):
        class NameFactory(Clothing.NameFactory):
            default = 'Cozy von Pocketworth'

        @classmethod
        def children_classes(cls):
            yield Pocket.multiple(20, 40)
            yield from super().children_classes()
            yield Leather.probable(30)


class Socks(Clothing):
    pass


class Shoes(Clothing):
    pass
    class ChildrenFactory(Clothing.ChildrenFactory):
        class BaseFactory(Clothing.BaseFactory):
            default = ['shoes', 'boots', 'sneakers', 'sandals']

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
