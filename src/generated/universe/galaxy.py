from genesys.model.model import Model
from .nebula import Nebula
# from .black_hole import BlackHole
# from .life import GalaxyArmLife, GalaxyCenterLife, Habitat
# from .star import StarSystem, DysonSphere


class GalaxyPart(Model):
    # Habitat
    # stars = Habitat.children_property(StarSystem)
    nebulas = Model.children_property(Nebula)
    # black_holes = Habitat.children_property(BlackHole)


class GalaxyArm(GalaxyPart):
    default_name = 'arm'


class GalaxyCenter(GalaxyPart):
    # eye = Model.child_property(BlackHole)

    default_name = 'galactic center'


class Galaxy(Model):
    center = Model.child_property(GalaxyCenter)
    arms = Model.children_property(GalaxyArm)
