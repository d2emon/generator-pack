from ...unknown import Dust, Sweat, Keratin
from .body_parts import BodyPart


class Knee(BodyPart):
    pass


class Toenail(BodyPart):
    dust = BodyPart.child_property(Dust)
    keratin = BodyPart.child_property(Keratin)

    class ChildrenFactory(BodyPart.ChildrenFactory):
        def children_classes(self):
            yield Dust.probable(40)
            yield Keratin


class Toe(BodyPart):
    nail = BodyPart.child_property(Toenail)

    class ChildrenFactory(BodyPart.ChildrenFactory):
        def children_classes(self):
            yield Toenail
            yield from super().children_classes()


class Foot(BodyPart):
    toes = BodyPart.children_property(Toe)
    sweat = BodyPart.child_property(Sweat)

    class ChildrenFactory(BodyPart.ChildrenFactory):
        def children_classes(self):
            yield from Toe.multiple(5)
            yield Sweat.probable(30)
            yield from super().children_classes()


class Leg(BodyPart):
    foot = BodyPart.child_property(Foot)
    knee = BodyPart.child_property(Knee)

    class ChildrenFactory(BodyPart.ChildrenFactory):
        def children_classes(self):
            yield Foot
            yield Knee
            yield from super().children_classes()
