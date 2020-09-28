from generated import life
from ....factory import Factory


class ClothingSetFactory(Factory):
    default_model = life.ClothingSet

    def children(self):
        # yield Hat.probable(2)
        # yield Glasses.probable(20)
        # yield Pants.probable(98)
        # yield Shirt.probable(98)
        # yield Coat.probable(50)
        # yield Socks.probable(80)
        # yield Shoes.probable(80)
        # yield Underwear.probable(99)
        yield None
