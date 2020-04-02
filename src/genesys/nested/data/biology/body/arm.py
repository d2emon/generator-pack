from ...unknown import Dust
from .body_parts import BodyPart, SoftBodyPart
from .head.hair import Hair
from ...chemistry import Keratin, Sweat


class ArmpitHair(Hair):
    class NameFactory(SoftBodyPart.NameFactory):
        default = 'hair'


class Armpit(SoftBodyPart):
    hair = SoftBodyPart.child_property(Hair)
    sweat = SoftBodyPart.child_property(Sweat)

    class ChildrenFactory(SoftBodyPart.ChildrenFactory):
        def children_classes(self):
            yield ArmpitHair
            yield Sweat.probable(80)
            yield from super().children_classes()


class Elbow(BodyPart):
    pass


class Fingernail(BodyPart):
    dust = BodyPart.child_property(Dust)
    keratin = BodyPart.child_property(Keratin)

    class ChildrenFactory(BodyPart.ChildrenFactory):
        def children_classes(self):
            yield Dust.probable(30)
            yield Keratin


class Finger(BodyPart):
    nail = BodyPart.child_property(Fingernail)

    class ChildrenFactory(BodyPart.ChildrenFactory):
        def children_classes(self):
            yield Fingernail
            yield from super().children_classes()


class Hand(BodyPart):
    fingers = BodyPart.children_property(Finger)

    class ChildrenFactory(BodyPart.ChildrenFactory):
        def children_classes(self):
            yield from Finger.multiple(5)
            yield from super().children_classes()


class Arm(BodyPart):
    hand = BodyPart.child_property(Hand)
    elbow = BodyPart.child_property(Elbow)
    armpit = BodyPart.child_property(Armpit)

    class ChildrenFactory(BodyPart.ChildrenFactory):
        def children_classes(self):
            yield Hand
            yield Elbow
            yield Armpit
            yield from super().children_classes()
