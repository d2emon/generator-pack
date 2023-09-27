from models.nested_model import NestedModel
from models.v5.life import Life
from models.materials.matter import Matter
from .star import StarSystem


class InterstellarCloud(Matter):
    state = Matter.GAS


class Nebula(NestedModel):
    life = NestedModel.child_property(Life)
    stars = NestedModel.children_property(StarSystem)
    clouds = NestedModel.children_property(InterstellarCloud)
