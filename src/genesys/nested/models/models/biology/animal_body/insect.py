from .body_part import Scales, Wing
from .crustacean import CrustaceanShell, CrustaceanLeg, CrustaceanClaw, CrustaceanBodyPart
from .venom import Venom
from ...chemistry import Chitin, Dew


class InsectLeg(CrustaceanLeg):
    pass


class InsectClaw(CrustaceanClaw):
    pass


class Stinger(CrustaceanBodyPart):
    venom = CrustaceanBodyPart.child_property(Venom)

    class Factory(CrustaceanBodyPart.Factory):
        class ChildrenFactory(CrustaceanBodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Chitin
                yield Venom


class Antenna(CrustaceanBodyPart):
    class Factory(CrustaceanBodyPart.Factory):
        class ChildrenFactory(CrustaceanBodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Chitin


class InsectWing(Wing):
    chitin = Wing.child_property(Chitin)
    scales = Wing.child_property(Scales)
    dew = Wing.child_property(Dew)

    default_name = 'wing'

    class Factory(Wing.Factory):
        class ChildrenFactory(Wing.Factory.ChildrenFactory):
            has_feathers = False

            def builders(self):
                yield next(Wing.Factory.BaseFactory([
                    Chitin,
                    Scales,
                ]))
                yield Dew.probable(3)
