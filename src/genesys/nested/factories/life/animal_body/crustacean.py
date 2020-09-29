from generated import life
from ...factory import Factory
from ...materials import ChitinFactory
from .skeleton import MuscleFactory, FatFactory
from .skin import ExoskeletonFactory


class CrustaceanLegFactory(Factory):
    default_model = life.CrustaceanLeg

    def children(self):
        yield ChitinFactory()
        yield MuscleFactory()
        yield FatFactory()


class CrustaceanClawFactory(CrustaceanLegFactory):
    default_model = life.CrustaceanClaw


class CrustaceanShellFactory(ExoskeletonFactory):
    default_model = life.CrustaceanShell
