"""
- CrustaceanLimb
- CrustaceanLeg
- CrustaceanClaw
- CrustaceanShell
- Crustacean
- Crustacean Body
"""
from ....materials import Chitin
from ...animal_body.limb import Limb
from ...animal_body.skin import Exoskeleton
from ..animal import Animal, AnimalBody


class CrustaceanLeg(Limb):
    default_name = 'leg'

    chitin = Limb.child_property(Chitin)


class CrustaceanClaw(CrustaceanLeg):
    default_name = 'claw'


class CrustaceanShell(Exoskeleton):
    default_name = 'shell'


class CrustaceanBody(AnimalBody):
    pass


class Crustacean(Animal):
    pass
