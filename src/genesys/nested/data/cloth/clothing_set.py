from genesys.nested.models import Model
from .clothing import Hat, Glasses, Pants, Shirt, Coat, Socks, Shoes, Underwear


class ClothingSet(Model):
    hat = Model.child_property(Hat)
    glasses = Model.child_property(Glasses)
    pants = Model.child_property(Pants)
    shirt = Model.child_property(Shirt)
    coat = Model.child_property(Coat)
    socks = Model.child_property(Socks)
    shoes = Model.child_property(Shoes)
    underwear = Model.child_property(Underwear)

    class NameFactory(Model.NameFactory):
        default = 'clothing'

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Hat.probable(2)
            yield Glasses.probable(20)
            yield Pants.probable(98)
            yield Shirt.probable(98)
            yield Coat.probable(50)
            yield Socks.probable(80)
            yield Shoes.probable(80)
            yield Underwear.probable(99)
