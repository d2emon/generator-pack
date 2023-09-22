from genesys.nested.factories.nested_factory import NestedFactory
from models.v5 import life
from genesys.nested.materials.organics import OrganicFactory
from ...body.body_parts import BodyPartFactory, SoftBodyPartFactory
from ..hair import HairFactory


class BoogersFactory(NestedFactory):
    model = life.Boogers

    def children(self):
        yield OrganicFactory.one()


class NostrilHairFactory(HairFactory):
    model = life.NostrilHair


class NostrilFactory(SoftBodyPartFactory):
    model = life.Nostril

    def children(self):
        yield NostrilHairFactory.one()
        yield BoogersFactory.multiple(0, 1)
        yield from super().children()


class NoseFactory(BodyPartFactory):
    model = life.Nose

    def children(self):
        yield NostrilFactory.multiple(2)
        yield from super().children()


class SnoutFactory(NoseFactory):
    # TODO: Refactor it
    default_model = life.Snout
