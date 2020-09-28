from generated import life
from ....factory import Factory
from ....materials import WaterFactory, SaltFactory
from ..body_parts import SoftBodyPartFactory
from ..blood import BloodVesselsFactory
from ..skeleton import FatFactory
from .hair import HairFactory


class TearFactory(Factory):
    default_model = life.Tear

    def children(self):
        yield WaterFactory()
        yield SaltFactory()


class EyelashesFactory(HairFactory):
    default_model = life.Eyelashes


class EyeFleshFactory(SoftBodyPartFactory):
    default_model = life.EyeFlesh

    def children(self):
        yield WaterFactory()
        yield BloodVesselsFactory()
        yield FatFactory()


class EyeFactory(SoftBodyPartFactory):
    default_model = life.Eye

    def children(self):
        yield EyelashesFactory()
        yield EyeFleshFactory()
        yield TearFactory().probable(2)
