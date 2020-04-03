from genesys.nested.models.models.unknown import GalacticLife
from genesys.nested.models import Model
from genesys.nested.models.mixins import EncounteredMixin
from .nebula import Nebula
from .star import StarSystem, DysonSphere
from .black_hole import BlackHole


class GalaxyPart(Model, EncounteredMixin):
    stars = Model.children_property(StarSystem)
    nebulas = Model.children_property(Nebula)
    black_holes = Model.children_property(BlackHole)

    class ChildrenFactory(Model.ChildrenFactory):
        life_probability = 0
        dyson_sphere_probabilities = 4, 2
        min_star_systems = 20
        max_star_systems = 20
        min_nebula = 20
        max_nebula = 50

        def black_holes(self):
            yield None

        def children_classes(self):
            yield GalacticLife.probable(self.life_probability)
            yield from [DysonSphere.probable(probability) for probability in self.dyson_sphere_probabilities]
            yield from StarSystem.multiple(self.min_star_systems, self.max_star_systems)
            yield from Nebula.multiple(self.min_nebula, self.max_nebula)
            yield from self.black_holes()


class GalaxyArm(GalaxyPart):
    class NameFactory(GalaxyPart.NameFactory):
        default = 'arm'

    class ChildrenFactory(GalaxyPart.ChildrenFactory):
        life_probability = 5
        min_nebula = 20
        max_nebula = 50

        def black_holes(self):
            yield BlackHole.probable(20)
            yield BlackHole.probable(20)


class GalaxyCenter(GalaxyPart):
    central_black_hole = Model.child_property(BlackHole)

    class NameFactory(GalaxyPart.NameFactory):
        default = 'galactic center'

    class ChildrenFactory(GalaxyPart.ChildrenFactory):
        life_probability = 10
        min_nebula = 0
        max_nebula = 12

        def black_holes(self):
            yield BlackHole


class Galaxy(Model):
    center = Model.child_property(GalaxyCenter)
    arm = Model.children_property(GalaxyArm)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield GalaxyCenter
            yield from GalaxyArm.multiple(2, 6)
