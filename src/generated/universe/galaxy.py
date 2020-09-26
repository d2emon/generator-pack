from genesys.model.model import Model
from .nebula import Nebula
from .star import StarSystem
from .black_hole import BlackHole
# from .life import GalaxyArmLife, GalaxyCenterLife, Habitat


class GalaxyPart(Model):
    # Habitat
    stars = Model.children_property(StarSystem)
    nebulas = Model.children_property(Nebula)
    black_holes = Model.children_property(BlackHole)


class GalaxyArm(GalaxyPart):
    default_name = 'arm'


class GalaxyCenter(GalaxyPart):
    eye = GalaxyPart.child_property(BlackHole)

    default_name = 'galactic center'


class Galaxy(Model):
    center = Model.child_property(GalaxyCenter)
    arms = Model.children_property(GalaxyArm)
