"""
- ClothingSet
"""
from models.tree_model import TreeModel as Model
from .clothing import Hat, Glasses, Pants, Shirt, Coat, Socks, Shoes, Underwear


class ClothingSet(Model):
    default_name = 'Clothing'

    hat = Model.child_property(Hat)
    glasses = Model.child_property(Glasses)
    pants = Model.child_property(Pants)
    shirt = Model.child_property(Shirt)
    coat = Model.child_property(Coat)
    socks = Model.child_property(Socks)
    shoes = Model.child_property(Shoes)
    underwear = Model.child_property(Underwear)
