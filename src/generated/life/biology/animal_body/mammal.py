from .body_part import Snout, Tail, Flesh
from generated.life.body.body import Hair, BodyPart, Mouth, Nose, Eye, Ear, Skull
from generated.materials.chemistry import Keratin


class Fur(Hair):
    class Factory(Hair.Factory):
        class ChildrenFactory(Hair.Factory.ChildrenFactory):
            def builders(self):
                yield Keratin


class Whiskers(Hair):
    class Factory(Hair.Factory):
        class ChildrenFactory(Hair.Factory.ChildrenFactory):
            def builders(self):
                yield Keratin


class MammalBodyPart(BodyPart):
    fur = BodyPart.child_property(Fur)


class MammalLeg(MammalBodyPart):
    default_name = 'leg'

    class Factory(MammalBodyPart.Factory):
        class ChildrenFactory(MammalBodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Fur
                yield super().builders()


class MammalHead(MammalBodyPart):
    mouths = BodyPart.children_property(Mouth)
    noses = BodyPart.children_property(Nose)
    whiskers = BodyPart.child_property(Whiskers)
    eyes = BodyPart.children_property(Eye)
    ears = BodyPart.children_property(Ear)
    skull = BodyPart.child_property(Skull)

    default_name = 'head'

    class Factory(MammalBodyPart.Factory):
        class ChildrenFactory(MammalBodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Mouth
                yield Snout
                yield Whiskers
                yield from Eye.multiple(2)
                yield from Ear.multiple(2)
                yield Skull
                yield Fur


class MammalBody(MammalBodyPart):
    heads = MammalBodyPart.children_property(MammalHead)
    leg = MammalBodyPart.children_property(MammalLeg)
    tails = MammalBodyPart.children_property(Tail)
    flesh = MammalBodyPart.child_property(Flesh)

    default_name = 'body'

    class Factory(MammalBodyPart.Factory):
        class ChildrenFactory(MammalBodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield MammalHead
                yield Fur
                yield from MammalLeg.multiple(4)
                yield Tail
                yield Flesh
