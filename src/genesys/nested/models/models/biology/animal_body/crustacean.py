from .body_part import Exoskeleton
from ..body import BodyPart, Muscles, Fat
from ...chemistry import Chitin


class CrustaceanBodyPart(BodyPart):
    chitin = BodyPart.child_property(Chitin)


class CrustaceanLeg(CrustaceanBodyPart):
    default_name = 'leg'

    class Factory(CrustaceanBodyPart.Factory):
        class ChildrenFactory(CrustaceanBodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Chitin
                yield Muscles
                yield Fat


class CrustaceanClaw(CrustaceanLeg):
    default_name = 'claw'


class CrustaceanShell(Exoskeleton):
    default_name = 'shell'
