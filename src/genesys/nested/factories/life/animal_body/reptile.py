from generated import life
from .limb import WingFactory
from .skin import ScalesFactory


class ReptileWingFactory(WingFactory):
    default_model = life.ReptileWing

    @classmethod
    def feathers(cls):
        yield ScalesFactory()
