"""
- Landscape
- Plain
- Forest
- Jungle
- Cave
- Mountain
"""
from models.v4.model import Model
from ..materials import Fire, Snow, Rock
from ..life import Grass, Trees, Life
from .water import River, Lake
from .soil import Soil


class Landscape(Model):
    fire = Model.child_property(Fire)
    life = Model.child_property(Life)
    rivers = Model.children_property(River)
    lakes = Model.children_property(Lake)
    grass = Model.children_property(Grass)
    trees = Model.children_property(Trees)
    soil = Model.children_property(Soil)
    snow = Model.child_property(Snow)
    rock = Model.child_property(Rock)


class Plain(Landscape):
    pass


class Forest(Landscape):
    pass


class Jungle(Forest):
    pass


class Cave(Landscape):
    # yield DragonLair
    pass


class Mountain(Landscape):
    cave = Model.child_property(Cave)
