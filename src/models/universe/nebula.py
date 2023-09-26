"""
- InterstellarCloud
- Nebula
"""
from models.nested_model import TreeModel
# from models.v5.materials import Gas
# from models.v5.life import Life
from .star import StarSystem


# class InterstellarCloud(Gas):
class InterstellarCloud:
    pass


class Nebula(TreeModel):
    # life = TreeModel.child_property(Life)
    stars = TreeModel.children_property(StarSystem)
    clouds = TreeModel.children_property(InterstellarCloud)
