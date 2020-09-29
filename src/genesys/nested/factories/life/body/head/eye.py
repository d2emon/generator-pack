from generated import life
from ....factory import Factory
from ....materials import WaterFactory, SaltFactory
from ...animal_body.body_parts import SoftBodyPartFactory
from ...animal_body.hair import HairFactory
from ...animal_body.eye import EyeFleshFactory


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
