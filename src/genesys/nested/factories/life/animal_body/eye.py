from generated import life
from ...materials import WaterFactory
from .body_parts import SoftBodyPartFactory
from .skeleton import FatFactory
from ..body.blood import BloodVesselsFactory


class EyeFleshFactory(SoftBodyPartFactory):
    default_model = life.EyeFlesh

    def children(self):
        yield WaterFactory()
        yield BloodVesselsFactory()
        yield FatFactory()


class SimpleEyeFactory(EyeFleshFactory):
    default_model = life.SimpleEye
