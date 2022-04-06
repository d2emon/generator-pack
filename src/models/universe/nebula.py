"""
- InterstellarCloud
- Nebula
"""
from models.nested_model import NestedModel
# from models.v5.materials import Gas
# from models.v5.life import Life
from .star import StarSystem


# class InterstellarCloud(Gas):
class InterstellarCloud:
    pass


class Nebula(NestedModel):
    # life = NestedModel.child_property(Life)
    stars = NestedModel.children_property(StarSystem)
    clouds = NestedModel.children_property(InterstellarCloud)
