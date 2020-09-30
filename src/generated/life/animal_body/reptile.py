from genesys.model.model import Model
from .limb import Wing
from .skin import Scales


# class ReptileBodyPart(BodyPart):
#     scales = BodyPart.child_property(Scales)


class ReptileWing(Wing):
    default_name = 'wing'
    scales = Wing.child_property(Scales)


# class ReptileHead(ReptileBodyPart):
#     default_name = 'head'
#
#     class Factory(ReptileBodyPart.Factory):
#         class ChildrenFactory(ReptileBodyPart.Factory.ChildrenFactory):
#             def builders(self):
#                 yield Scales
#                 yield super().builders()


# class ReptileLeg(ReptileBodyPart):
#     default_name = 'leg'
#
#     class Factory(ReptileBodyPart.Factory):
#         class ChildrenFactory(ReptileBodyPart.Factory.ChildrenFactory):
#             def builders(self):
#                 yield Scales
#                 yield super().builders()


# class ReptileBody(ReptileBodyPart):
#     heads = ReptileBodyPart.children_property(ReptileHead)
#     legs = ReptileBodyPart.children_property(ReptileLeg)
#     wings = ReptileBodyPart.children_property(ReptileWing)
#     tails = ReptileBodyPart.children_property(Tail)
#     flesh = ReptileBodyPart.child_property(Flesh)
#
#     default_name = 'body'
#
#     class Factory(ReptileBodyPart.Factory):
#        class ChildrenFactory(ReptileBodyPart.Factory.ChildrenFactory):
#             def builders(self):
#                 yield ReptileHead
#                 yield Scales
#                 yield from ReptileLeg.multiple(4)
#                 yield Tail
#                 yield Flesh


# class SnakeBody(ReptileBody):
#     default_name = 'body'
#
#     class Factory(ReptileBody.Factory):
#         class ChildrenFactory(ReptileBody.Factory.ChildrenFactory):
#             def builders(self):
#                 yield ReptileHead
#                 yield Scales
#                 yield Tail
#                 yield Flesh
