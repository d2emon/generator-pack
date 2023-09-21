from models.v5 import life
from factories.thing.nested_factory import NestedFactory as Factory
from utils.nested import select_item
from ...materials import ChitinFactory, DewFactory
from .crustacean import CrustaceanLegFactory, CrustaceanClawFactory
from ..body.skin import ScalesFactory
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
        yield select_item(
            ChitinFactory(),
            ScalesFactory(),
        )
        yield DewFactory().probable(2)
