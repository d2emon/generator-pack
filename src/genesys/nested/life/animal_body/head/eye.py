from models.v5 import life
from factories.nested_factory import NestedFactory as Factory
from ....materials import WaterFactory, SaltFactory
from ..body_parts import SoftBodyPartFactory
from ..skeleton import FatFactory
from ..blood import BloodVesselsFactory
from ..hair import HairFactory


class EyeFleshFactory(SoftBodyPartFactory):
    default_model = life.EyeFlesh

    def children(self):
        yield WaterFactory()
        yield BloodVesselsFactory()
        yield FatFactory()


class SimpleEyeFactory(EyeFleshFactory):
    default_model = life.SimpleEye


class TearFactory(Factory):
    default_model = life.Tear

    def children(self):
        yield WaterFactory()
        yield SaltFactory()


class EyelashesFactory(HairFactory):
    default_model = life.Eyelashes


class EyeFactory(SoftBodyPartFactory):
    default_model = life.Eye

    def children(self):
        yield EyelashesFactory()
        yield EyeFleshFactory()
        yield TearFactory().probable(2)
