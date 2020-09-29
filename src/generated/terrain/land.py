"""
- Landscape
- Plain
- Forest
- Jungle
- Cave
- Mountain
"""
from genesys.model.model import Model
from ..materials import Fire, Snow, Rock
from ..life import Grass, Trees
from .water import River, Lake
from .soil import Soil


class Landscape(Model):
    fire = Model.child_property(Fire)
    # yield LandLife
    rivers = Model.children_property(River)
    lakes = Model.children_property(Lake)
    grass = Model.children_property(Grass)
    trees = Model.children_property(Trees)
    soil = Model.children_property(Soil)
    snow = Model.child_property(Snow)


class Plain(Landscape):
    pass


class Forest(Landscape):
    pass


class Jungle(Forest):
    pass


class Cave(Model):
    # yield CaveLife
    # yield DragonLair
    rivers = Model.children_property(River)
    lakes = Model.children_property(Lake)
    rock = Model.children_property(Rock)


class Mountain(Landscape):
    cave = Model.child_property(Cave)
    rock = Model.child_property(Rock)
