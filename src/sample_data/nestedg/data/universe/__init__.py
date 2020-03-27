"""
Universe stuff
"""
from nestedg.mixins import EncounteredMixin
from nestedg.model import Model
from nestedg.data import unknown, materials, lookups
from nestedg.data.materials import elements
from . import star


class GlobalItem(Model):
    universe = Model.child_property(unknown.Model)

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield Universe


class Answer42(GlobalItem):
    def answer(self):
        return self.universe


class Everything(GlobalItem):
    def get_everything(self):
        return self.universe


class Portal(GlobalItem):
    def enter(self):
        return self.universe


class WhiteHole(Portal):
    pass


class EndOfUniverseNote(Model):
    contents = Model.children_property(unknown.Model)

    class BaseGenerator(Model.BaseGenerator):
        default = lookups.end_of_universe_notes

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield unknown.Pasta.probable(0.1)

    def read(self):
        return self.BaseGenerator.next()


class BlackHole(Portal, EncounteredMixin):
    white_hole = Model.child_property(WhiteHole)

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield EndOfUniverseNote.probable(0.5)
            yield unknown.Crustacean.probable(0.2)
            yield WhiteHole

    @property
    def universe(self):
        return self.white_hole and self.white_hole.universe

    def inside(self):
        return self.children

    def enter(self):
        return self.white_hole


class InterstellarCloud(Model):
    contents = Model.children_property(Model)

    class BaseGenerator(Model.BaseGenerator):
        default = lookups.interstellar_clouds

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield elements.Helium
            yield elements.Hydrogen
            yield elements.Carbon.probable(80)
            yield materials.Water.probable(5)
            yield materials.Ammonia.probable(5)
            yield elements.Nitrogen.probable(5)
            yield elements.Iron.probable(5)
            yield elements.Sulfur.probable(5)
            yield elements.Oxygen.probable(15)


class Nebula(Model, EncounteredMixin):
    stars = Model.children_property(star.StarSystem)
    clouds = Model.children_property(InterstellarCloud)

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield unknown.GalacticLife.probable(15)
            yield star.SingleStar.probable(2)
            yield star.SingleStar.probable(2)
            yield star.SingleStar.probable(2)
            yield from InterstellarCloud.multiple(1, 6)


class GalaxyPart(Model, EncounteredMixin):
    stars = Model.children_property(star.StarSystem)
    nebulas = Model.children_property(Nebula)
    black_holes = Model.children_property(BlackHole)

    class ChildrenGenerator(Model.ChildrenGenerator):
        life_probability = 0
        dyson_sphere_probabilities = 4, 2
        min_star_systems = 20
        max_star_systems = 20
        min_nebula = 20
        max_nebula = 50

        def black_holes(self):
            yield None

        def children_classes(self):
            yield unknown.GalacticLife.probable(self.life_probability)
            yield from [star.DysonSphere.probable(probability) for probability in self.dyson_sphere_probabilities]
            yield from star.StarSystem.multiple(self.min_star_systems, self.max_star_systems)
            yield from Nebula.multiple(self.min_nebula, self.max_nebula)
            yield from self.black_holes()


class GalaxyArm(GalaxyPart):
    class NameGenerator(GalaxyPart.NameGenerator):
        default = 'arm'

    class ChildrenGenerator(GalaxyPart.ChildrenGenerator):
        life_probability = 5
        min_nebula = 20
        max_nebula = 50

        def black_holes(self):
            yield BlackHole.probable(20)
            yield BlackHole.probable(20)


class GalaxyCenter(GalaxyPart):
    central_black_hole = Model.child_property(BlackHole)

    class NameGenerator(GalaxyPart.NameGenerator):
        default = 'galactic center'

    class ChildrenGenerator(GalaxyPart.ChildrenGenerator):
        life_probability = 10
        min_nebula = 0
        max_nebula = 12

        def black_holes(self):
            yield BlackHole


class Galaxy(Model):
    center = Model.child_property(GalaxyCenter)
    arm = Model.children_property(GalaxyArm)

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield GalaxyCenter
            yield from GalaxyArm.multiple(2, 6)


class Supercluster(Model):
    galaxies = Model.children_property(Galaxy)

    class NameGenerator(Model.NameGenerator):
        default = 'galactic supercluster'

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield from Galaxy.multiple(10, 30)


class Universe(Model):
    clusters = Model.children_property(Supercluster)

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield from Supercluster.multiple(10, 30)


class Multiverse(Model):
    universes = Model.children_property(Universe)

    class NameGenerator(Model.NameGenerator):
        default = None

    class BaseGenerator(Model.BaseGenerator):
        default = lookups.multiverses.values

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield from Universe.multiple(10, 30)
