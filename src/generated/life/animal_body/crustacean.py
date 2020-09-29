from ...materials import Chitin
from .limb import Limb
from .skin import Exoskeleton


class CrustaceanLimb(Limb):
    chitin = Limb.child_property(Chitin)


class CrustaceanLeg(CrustaceanLimb):
    default_name = 'leg'


class CrustaceanClaw(CrustaceanLeg):
    default_name = 'claw'


class CrustaceanShell(Exoskeleton):
    default_name = 'shell'
