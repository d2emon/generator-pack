from factories.thing.nested_factory import NestedFactory
from models.universe import galaxy
# from ..life import GalaxyArmLifeFactory, GalaxyCenterLifeFactory
from .black_hole import BlackHoleFactory
from .nebula import NebulaFactory
from .star import DysonSphereFactory, StarSystemFactory


class GalaxyPartFactory(NestedFactory):
    dyson_sphere_probabilities = 4, 2

    min_star_systems = 20
    max_star_systems = 50

    min_nebulas = 0
    max_nebulas = 12

    def black_holes(self):
        yield None

    def life(self):
        yield None

    def stars(self):
        for probability in self.dyson_sphere_probabilities:
            yield DysonSphereFactory.probable(probability)

        yield StarSystemFactory.multiple(self.min_star_systems, self.max_star_systems)

    def nebulas(self):
        yield NebulaFactory.multiple(self.min_nebulas, self.max_nebulas)

    def children(self):
        yield from self.black_holes()
        yield from self.life()
        yield from self.stars()
        yield from self.nebulas()


class GalaxyArmFactory(GalaxyPartFactory):
    model = galaxy.GalaxyArm

    def black_holes(self):
        yield BlackHoleFactory.probable(20)
        yield BlackHoleFactory.probable(20)

    def life(self):
        # galactic life,5%
        # # yield GalaxyArmLifeFactory.one()
        # yield GalacticLifeFactory.probable(5)
        yield None


class GalaxyCenterFactory(GalaxyPartFactory):
    model = galaxy.GalaxyCenter

    def black_holes(self):
        yield BlackHoleFactory.one()

    def life(self):
        # galactic life,10%
        # # yield GalaxyCenterLifeFactory()
        # yield GalacticLifeFactory.probable(10)
        yield None


class GalaxyFactory(NestedFactory):
    model = galaxy.Galaxy

    def children(self):
        yield GalaxyCenterFactory.one()
        yield GalaxyArmFactory.multiple(2, 6)
