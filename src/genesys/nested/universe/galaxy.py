from genesys.nested.factories.nested_factory import NestedFactory
from models.universe import galaxy
from .black_hole import BlackHoleFactory
from .nebula import NebulaFactory
from .star import DysonSphereFactory, StarSystemFactory

from ..unsorted_life import GalacticLifeFactory


class GalaxyPartFactory(NestedFactory):
    model = galaxy.GalaxyPart

    dyson_sphere_probabilities = 4, 2

    min_star_systems = 20
    max_star_systems = 50

    min_nebulas = 0
    max_nebulas = 12

    child_groups = {
        'black_holes': [],
        'life': [],
        'stars': [],
        'nebulas': [],
    }

    def black_holes(self):
        yield None

    def life(self):
        yield None

    def stars(self):
        for probability in self.dyson_sphere_probabilities:
            yield from DysonSphereFactory.probable(probability)

        yield from StarSystemFactory.multiple(self.min_star_systems, self.max_star_systems)

    def nebulas(self):
        yield from NebulaFactory.multiple(self.min_nebulas, self.max_nebulas)

    def groups_factory(self, *args, **kwargs):
        data = super().groups_factory(*args, **kwargs)

        data['black_holes'] = list(self.black_holes())
        data['life'] = list(self.life())
        data['stars'] = list(self.stars())
        data['nebulas'] = list(self.nebulas())

        return data

class GalaxyArmFactory(GalaxyPartFactory):
    model = galaxy.GalaxyArm

    def black_holes(self):
        yield from BlackHoleFactory.probable(20)
        yield from BlackHoleFactory.probable(20)

    def life(self):
        yield from GalacticLifeFactory.probable(5)


class GalaxyCenterFactory(GalaxyPartFactory):
    model = galaxy.GalaxyCenter

    def black_holes(self):
        yield from BlackHoleFactory.one()

    def life(self):
        yield from GalacticLifeFactory.probable(10)


class GalaxyFactory(NestedFactory):
    model = galaxy.Galaxy
    child_groups = {
        'center': GalaxyCenterFactory.one(),
        'arms': GalaxyArmFactory.multiple(2, 6),
    }
