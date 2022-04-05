from models.v5 import universe
from factories.nested_factory import NestedFactory as Factory
from ..life import GalaxyArmLifeFactory, GalaxyCenterLifeFactory
from .nebula import NebulaFactory
from .star import StarSystemFactory, DysonSphereFactory
from .black_hole import BlackHoleFactory


class SpaceFactory(Factory):
    dyson_sphere_probabilities = 4, 2
    min_star_systems = 20
    max_star_systems = 50
    min_nebula = 0
    max_nebula = 12

    def black_holes(self):
        yield None

    def life(self):
        yield None

    @classmethod
    def nebulas(cls):
        yield from NebulaFactory().multiple(cls.min_nebula, cls.max_nebula)

    def stars(self):
        yield from [DysonSphereFactory().probable(probability) for probability in self.dyson_sphere_probabilities]
        yield from StarSystemFactory().multiple(self.min_star_systems, self.max_star_systems)

    def children(self):
        yield from self.life()
        yield from self.stars()
        yield from self.nebulas()
        yield from self.black_holes()


class GalaxyArmFactory(SpaceFactory):
    default_model = universe.GalaxyArm

    def life(self):
        yield GalaxyArmLifeFactory()

    def black_holes(self):
        yield BlackHoleFactory().probable(20)
        yield BlackHoleFactory().probable(20)


class GalaxyCenterFactory(SpaceFactory):
    default_model = universe.GalaxyCenter

    def life(self):
        yield GalaxyCenterLifeFactory()

    def black_holes(self):
        yield BlackHoleFactory()


class GalaxyFactory(Factory):
    default_model = universe.Galaxy

    def children(self):
        yield GalaxyCenterFactory()
        yield from GalaxyArmFactory().multiple(2, 6)
