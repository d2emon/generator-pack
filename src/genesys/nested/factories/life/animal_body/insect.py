from generated import life
from factories.nested_factory import NestedFactory as Factory
from ...materials import ChitinFactory, DewFactory
from ..animals.crustacean import CrustaceanLegFactory, CrustaceanClawFactory
from .skin import ScalesFactory
from .venom import VenomFactory


class InsectLegFactory(CrustaceanLegFactory):
    default_model = life.InsectLeg


class InsectClawFactory(CrustaceanClawFactory):
    default_model = life.InsectClaw


class StingerFactory(Factory):
    default_model = life.Stinger

    def children(self):
        yield ChitinFactory()
        yield VenomFactory()


class AntennaFactory(Factory):
    default_model = life.Antenna

    def children(self):
        yield ChitinFactory()


class InsectWingFactory(Factory):
    default_model = life.InsectWing

    def children(self):
        yield self.select_item(
            ChitinFactory(),
            ScalesFactory(),
        )
        yield DewFactory().probable(2)
