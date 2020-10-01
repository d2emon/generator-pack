"""
- InsectLeg
- InsectClaw
- Stinger
- Antenna
- InsectWing
"""
from ...materials import Chitin, Dew
from ..animals.crustacean import CrustaceanLeg, CrustaceanClaw
from .limb import Wing
from .skin import Scales
from .venom import Venom


class InsectLeg(CrustaceanLeg):
    pass


class InsectClaw(CrustaceanClaw):
    pass


class Stinger(CrustaceanLeg):
    venom = CrustaceanLeg.child_property(Venom)


class Antenna(CrustaceanLeg):
    pass


class InsectWing(Wing):
    default_name = 'wing'
    chitin = Wing.child_property(Chitin)
    scales = Wing.child_property(Scales)
    dew = Wing.child_property(Dew)
