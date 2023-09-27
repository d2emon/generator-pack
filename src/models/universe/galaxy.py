from models.nested_model import NestedModel
from models.v5.life import Life
from .black_hole import BlackHole
from .nebula import Nebula
from .star import StarSystem


class GalaxyPart(NestedModel):
    life = NestedModel.child_property(Life)
    stars = NestedModel.children_property(StarSystem)
    nebulas = NestedModel.children_property(Nebula)
    black_holes = NestedModel.children_property(BlackHole)


class GalaxyArm(GalaxyPart):
    default_name = 'arm'


class GalaxyCenter(GalaxyPart):
    default_name = 'galactic center'

    eye = GalaxyPart.child_property(BlackHole)


class Galaxy(NestedModel):
    center = NestedModel.child_property(GalaxyCenter)
    arms = NestedModel.children_property(GalaxyArm)
