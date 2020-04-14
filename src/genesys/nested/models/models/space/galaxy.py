from genesys.nested.models import Model
from .black_hole import BlackHole
from .life import GalaxyArmLife, GalaxyCenterLife, Habitat
from .nebula import Nebula
from .star import StarSystem, DysonSphere


class GalaxyPart(Habitat):
    stars = Habitat.children_property(StarSystem)
    nebulas = Habitat.children_property(Nebula)
    black_holes = Habitat.children_property(BlackHole)

    class Factory(Habitat.Factory):
        dyson_sphere_probabilities = 4, 2
        min_star_systems = 20
        max_star_systems = 20
        min_nebula = 20
        max_nebula = 50

        @classmethod
        def black_holes(cls):
            yield None

        @classmethod
        def life(cls):
            yield None

        @classmethod
        def nebulas(cls):
            yield from Nebula.multiple(cls.min_nebula, cls.max_nebula)

        @classmethod
        def stars(cls):
            yield from [DysonSphere.probable(probability) for probability in cls.dyson_sphere_probabilities]
            yield from StarSystem.multiple(cls.min_star_systems, cls.max_star_systems)

        def children(self):
            yield from self.life()
            yield from self.stars()
            yield from self.nebulas()
            yield from self.black_holes()


class GalaxyArm(GalaxyPart):
    default_name = 'arm'

    class Factory(GalaxyPart.Factory):
        min_nebula = 20
        max_nebula = 50

        @classmethod
        def life(cls):
            yield GalaxyArmLife

        @classmethod
        def black_holes(cls):
            yield BlackHole.probable(20)
            yield BlackHole.probable(20)


class GalaxyCenter(GalaxyPart):
    eye = Model.child_property(BlackHole)

    default_name = 'galactic center'

    class Factory(GalaxyPart.Factory):
        min_nebula = 0
        max_nebula = 12

        @classmethod
        def life(cls):
            yield GalaxyCenterLife

        @classmethod
        def black_holes(cls):
            yield BlackHole


class Galaxy(Model):
    center = Model.child_property(GalaxyCenter)
    arms = Model.children_property(GalaxyArm)

    class Factory(Model.Factory):
        def children(self):
            yield GalaxyCenter
            yield from GalaxyArm.multiple(2, 6)
