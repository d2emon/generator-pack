"""
- GalaxyPart
- GalaxyArm
- GalaxyCenter
- Galaxy
"""
from models.nested_model import TreeModel
# from models.v5.life import Life
from .black_hole import BlackHole
from .nebula import Nebula
from .star import StarSystem


class GalaxyPart(TreeModel):
    # life = TreeModel.child_property(Life)
    stars = TreeModel.children_property(StarSystem)
    nebulas = TreeModel.children_property(Nebula)
    black_holes = TreeModel.children_property(BlackHole)


class GalaxyArm(GalaxyPart):
    default_name = 'arm'


class GalaxyCenter(GalaxyPart):
    default_name = 'galactic center'

    eye = GalaxyPart.child_property(BlackHole)


class Galaxy(TreeModel):
    center = TreeModel.child_property(GalaxyCenter)
    arms = TreeModel.children_property(GalaxyArm)
