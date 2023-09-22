from genesys.nested.factories.nested_factory import NestedFactory
from models.v5 import life
from genesys.nested.materials.molecules import SaltFactory
from genesys.nested.materials.water import WaterFactory
from ...body.blood import BloodVesselsFactory
from ...body.body_parts import SoftBodyPartFactory
from ...body.skeleton import FatFactory
from ..hair import HairFactory


class EyelashesFactory(HairFactory):
    model = life.Eyelashes


class EyeFleshFactory(SoftBodyPartFactory):
    model = life.EyeFlesh

    def children(self):
        yield WaterFactory.one()
        yield BloodVesselsFactory.one()
        yield FatFactory.one()


class TearFactory(NestedFactory):
    model = life.Tear

    def children(self):
        yield WaterFactory.one()
        yield SaltFactory.one()


class EyeFactory(SoftBodyPartFactory):
    model = life.Eye

    def children(self):
        yield EyelashesFactory.one()
        yield EyeFleshFactory.one()
        yield TearFactory.probable(2)


class SimpleEyeFactory(EyeFleshFactory):
    # TODO: Refactor it
    default_model = life.SimpleEye
