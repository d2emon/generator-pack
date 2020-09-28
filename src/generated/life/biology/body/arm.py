from generated.nested_v2.models import Dust
from .body_parts import BodyPart, SoftBodyPart
from .head.hair import Hair
from generated.materials.chemistry import Keratin, Sweat


class ArmpitHair(Hair):
    default_name = 'hair'


class Armpit(SoftBodyPart):
    hair = SoftBodyPart.child_property(Hair)
    sweat = SoftBodyPart.child_property(Sweat)

    class Factory(SoftBodyPart.Factory):
        class ChildrenFactory(SoftBodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield ArmpitHair
                yield Sweat.probable(80)
                yield from super().builders()


class Elbow(BodyPart):
    pass


class Fingernail(BodyPart):
    dust = BodyPart.child_property(Dust)
    keratin = BodyPart.child_property(Keratin)

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Dust.probable(30)
                yield Keratin


class Finger(BodyPart):
    nail = BodyPart.child_property(Fingernail)

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Fingernail
                yield from super().builders()


class Hand(BodyPart):
    fingers = BodyPart.children_property(Finger)

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield from Finger.multiple(5)
                yield from super().builders()


class Arm(BodyPart):
    hand = BodyPart.child_property(Hand)
    elbow = BodyPart.child_property(Elbow)
    armpit = BodyPart.child_property(Armpit)

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Hand
                yield Elbow
                yield Armpit
                yield from super().builders()
