# from genesys.model.model import Model
from .limb import Limb


class BirdLimb(Limb):
    # feathers = Limb.child_property(Feathers)
    pass


class BirdWing(BirdLimb):
    default_name = 'wing'


class BirdLeg(BirdLimb):
    default_name = 'leg'


class BirdTail(BirdLimb):
    default_name = 'tail'


# class Beak(Bones):
#     pass


# class BirdHead(BirdBodyPart):
#     beaks = BodyPart.children_property(Beak)
#     eyes = BodyPart.children_property(Eye)
#     skull = BodyPart.child_property(Skull)
#
#     default_name = 'head'
#
#         class ChildrenFactory(BirdBodyPart.Factory.ChildrenFactory):
#             def builders(self):
#                 yield Beak
#                 yield from Eye.multiple(2)
#                 yield Skull
#                 yield Feathers


# class BirdBody(BirdBodyPart):
#     heads = BirdBodyPart.children_property(BirdHead)
#     legs = BirdBodyPart.children_property(BirdLeg)
#     wings = BirdBodyPart.children_property(Wing)
#     tails = BirdBodyPart.children_property(BirdTail)
#     flesh = BirdBodyPart.child_property(Flesh)
#
#     default_name = 'body'
#
#         class ChildrenFactory(BirdBodyPart.Factory.ChildrenFactory):
#             def builders(self):
#                 yield BirdHead
#                 yield Feathers
#                 yield from BirdLeg.multiple(2)
#                 yield from BirdWing.multiple(2)
#                 yield BirdTail
#                 yield Flesh
