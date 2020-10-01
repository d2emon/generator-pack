"""
- InsectLeg
- InsectClaw
- Stinger
- Antenna
- InsectWing
"""
from ...materials import Chitin, Dew
from ..animals.crustacean import CrustaceanLeg, CrustaceanClaw, CrustaceanLimb
from .limb import Wing
from .skin import Scales
from .venom import Venom


class InsectLeg(CrustaceanLeg):
    pass


class InsectClaw(CrustaceanClaw):
    pass


class Stinger(CrustaceanLimb):
    venom = CrustaceanLimb.child_property(Venom)


class Antenna(CrustaceanLimb):
    pass


class InsectWing(Wing):
    default_name = 'wing'
    chitin = Wing.child_property(Chitin)
    scales = Wing.child_property(Scales)
    dew = Wing.child_property(Dew)
