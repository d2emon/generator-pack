from models.v5 import life
from factories.nested_factory import NestedFactory as Factory
from ....materials import OrganicFactory
from ..body_parts import BodyPartFactory, SoftBodyPartFactory
from ..hair import HairFactory


class BoogersFactory(Factory):
    default_model = life.Boogers

    def children(self):
        yield OrganicFactory()


class NostrilHairFactory(HairFactory):
    default_model = life.NostrilHair


class NostrilFactory(SoftBodyPartFactory):
    default_model = life.Nostril

    def children(self):
        yield NostrilHairFactory()
        yield from BoogersFactory().multiple(0, 1)
        yield from super().children()


class NoseFactory(BodyPartFactory):
    default_model = life.Nose

    def children(self):
        yield from NostrilFactory().multiple(2)
        yield from super().children()


class SnoutFactory(NoseFactory):
    default_model = life.Snout
