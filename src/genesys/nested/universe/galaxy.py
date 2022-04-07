from models.universe.galaxy import Galaxy, GalaxyArm, GalaxyCenter
from factories.nested_factory import NestedFactory
# from ..life import GalaxyArmLifeFactory, GalaxyCenterLifeFactory
from .black_hole import BlackHoleFactory
from .nebula import NebulaFactory
from .star import DysonSphereFactory, StarSystemFactory


# Galaxy
# GalaxyArm
# GalaxyCenter


class GalaxyFactory(NestedFactory):
    default_model = Galaxy

    def children(self):
        yield GalaxyCenterFactory.as_child()
        yield GalaxyArmFactory.multiple(2, 6)


class GalaxyPartFactory(NestedFactory):
    dyson_sphere_probabilities = 4, 2
    min_star_systems = 20
    max_star_systems = 50
    min_nebula = 0
    max_nebula = 12

    def black_holes(self):
        yield None

    def life(self):
        yield None

    def stars(self):
        # # yield from [DysonSphereFactory().probable(probability) for probability in self.dyson_sphere_probabilities]
        yield DysonSphereFactory.probable(4)
        yield DysonSphereFactory.probable(2)
        yield StarSystemFactory.multiple(self.min_star_systems, self.max_star_systems)

    def nebulas(self):
        yield NebulaFactory.multiple(self.min_nebula, self.max_nebula)

    def children(self):
        yield from self.black_holes()
        yield from self.life()
        yield from self.stars()
        yield from self.nebulas()


class GalaxyArmFactory(GalaxyPartFactory):
    default_model = GalaxyArm
    default_name = "arm"

    def black_holes(self):
        yield BlackHoleFactory.probable(20)
        yield BlackHoleFactory.probable(20)

    def life(self):
        # # yield GalaxyArmLifeFactory.as_child()
        # yield GalacticLifeFactory.probable(5)
        yield None


class GalaxyCenterFactory(GalaxyPartFactory):
    default_model = GalaxyCenter
    default_name = "galactic center"

    def black_holes(self):
        yield BlackHoleFactory.as_child()

    def life(self):
        # # yield GalaxyCenterLifeFactory()
        # yield GalacticLifeFactory.probable(10)
        yield None


"""
new Thing("galaxy arm",[
    "black hole,20%",
    "black hole,20%"
    ####
    "galactic life,5%",
    ####
    "dyson sphere,4%",
    "dyson sphere,2%",
    "star system,20-50",
    ####
    "nebula,0-12",
],"arm");
new Thing("galaxy center",[
    "black hole",
    ####
    "galactic life,10%",
    ####
    "dyson sphere,4%",
    "dyson sphere,2%",
    "star system,20-50",
    ####
    "nebula,0-12"
],"galactic center");
"""
