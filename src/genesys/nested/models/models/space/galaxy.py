from genesys.nested.models import Model
from genesys.nested.models.mixins import EncounteredMixin
from .black_hole import BlackHole
from .nebula import Nebula
from .star import StarSystem, DysonSphere
# from ..biology import GalacticLife


class GalaxyPart(Model, EncounteredMixin):
    stars = Model.children_property(StarSystem)
    nebulas = Model.children_property(Nebula)
    black_holes = Model.children_property(BlackHole)

    class Factory(Model.Factory):
        life_probability = 0
        dyson_sphere_probabilities = 4, 2
        min_star_systems = 20
        max_star_systems = 20
        min_nebula = 20
        max_nebula = 50

        def black_holes(self):
            yield None

        def life(self):
            # yield GalacticLife.probable(self.life_probability)
            yield None

        def nebulas(self):
            yield from Nebula.multiple(self.min_nebula, self.max_nebula)

        def stars(self):
            yield from [DysonSphere.probable(probability) for probability in self.dyson_sphere_probabilities]
            yield from StarSystem.multiple(self.min_star_systems, self.max_star_systems)

        def children(self):
            yield from self.life()
            yield from self.stars()
            yield from self.nebulas()
            yield from self.black_holes()


class GalaxyArm(GalaxyPart):
    default_name = 'arm'

    class Factory(GalaxyPart.Factory):
        life_probability = 5
        min_nebula = 20
        max_nebula = 50

        def black_holes(self):
            yield BlackHole.probable(20)
            yield BlackHole.probable(20)


class GalaxyCenter(GalaxyPart):
    eye = Model.child_property(BlackHole)

    default_name = 'galactic center'

    class Factory(GalaxyPart.Factory):
        life_probability = 10
        min_nebula = 0
        max_nebula = 12

        def black_holes(self):
            yield BlackHole


class Galaxy(Model):
    center = Model.child_property(GalaxyCenter)
    arms = Model.children_property(GalaxyArm)

    class Factory(Model.Factory):
        def children(self):
            yield GalaxyCenter
            yield from GalaxyArm.multiple(2, 6)
