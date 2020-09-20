from genesys.nested.models.models.unknown import Feathers
from .body_part import Wing, Flesh
from ..body import BodyPart, Bones, Eye, Skull


class BirdWing(Wing):
    pass


class BirdBodyPart(BodyPart):
    feathers = BodyPart.child_property(Feathers)


class BirdLeg(BirdBodyPart):
    default_name = 'leg'

    class Factory(BirdBodyPart.Factory):
        class ChildrenFactory(BirdBodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Feathers
                yield super().builders()


class BirdTail(BirdBodyPart):
    default_name = 'tail'

    class Factory(BirdBodyPart.Factory):
        class ChildrenFactory(BirdBodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Feathers
                yield super().builders()


class Beak(Bones):
    pass


class BirdHead(BirdBodyPart):
    beaks = BodyPart.children_property(Beak)
    eyes = BodyPart.children_property(Eye)
    skull = BodyPart.child_property(Skull)

    default_name = 'head'

    class Factory(BirdBodyPart.Factory):
        class ChildrenFactory(BirdBodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Beak
                yield from Eye.multiple(2)
                yield Skull
                yield Feathers


class BirdBody(BirdBodyPart):
    heads = BirdBodyPart.children_property(BirdHead)
    legs = BirdBodyPart.children_property(BirdLeg)
    wings = BirdBodyPart.children_property(Wing)
    tails = BirdBodyPart.children_property(BirdTail)
    flesh = BirdBodyPart.child_property(Flesh)

    default_name = 'body'

    class Factory(BirdBodyPart.Factory):
        class ChildrenFactory(BirdBodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield BirdHead
                yield Feathers
                yield from BirdLeg.multiple(2)
                yield from BirdWing.multiple(2)
                yield BirdTail
                yield Flesh
