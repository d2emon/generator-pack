"""
- Pocket
- Clothing
- Pants
- Shirt
- Underwear
- Coat
    - Cozy von Pocketworth (Unused)
- Socks
- Shoes
- Hat
- Glasses
"""
from models.tree_model import TreeModel as Model
from ..materials import Sweat, Plastic
from models.v5.life.animal_body.skin import DeadSkin
from .fabric import Cloth


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


class Socks(Clothing):
    pass


class Shoes(Clothing):
    plastic = Cloth.children_property(Plastic)


class Hat(Clothing):
    pass


class Glasses(Clothing):
    plastic = Cloth.children_property(Plastic)
    # glass = Cloth.children_property(Glass)
    # metal = Cloth.children_property(Metal)
