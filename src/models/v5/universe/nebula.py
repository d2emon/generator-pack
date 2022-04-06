"""
- InterstellarCloud
- Nebula
"""
from models.nested_model import NestedModel as Model
from ..materials import Gas
from ..life import Life
from .star import StarSystem


class InterstellarCloud(Gas):
    pass


class Nebula(Model):
    life = Model.child_property(Life)
    stars = Model.children_property(StarSystem)
    clouds = Model.children_property(InterstellarCloud)
