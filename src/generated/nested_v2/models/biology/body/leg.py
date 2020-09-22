from generated.nested_v2.models import Dust
from .body_parts import BodyPart
from generated.chemistry import Keratin, Sweat


class Knee(BodyPart):
    pass


class Toenail(BodyPart):
    dust = BodyPart.child_property(Dust)
    keratin = BodyPart.child_property(Keratin)

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Dust.probable(40)
                yield Keratin


class Toe(BodyPart):
    nail = BodyPart.child_property(Toenail)

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Toenail
                yield from super().builders()


class Foot(BodyPart):
    toes = BodyPart.children_property(Toe)
    sweat = BodyPart.child_property(Sweat)

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield from Toe.multiple(5)
                yield Sweat.probable(30)
                yield from super().builders()


class Leg(BodyPart):
    foot = BodyPart.child_property(Foot)
    knee = BodyPart.child_property(Knee)

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Foot
                yield Knee
                yield from super().builders()
