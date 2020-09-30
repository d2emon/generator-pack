# class SimpleMouth(SkinlessSoftBodyPart):
#     default_name = 'Mouth'
#
#     class Factory(SkinlessSoftBodyPart.Factory):
#         class ChildrenFactory(SkinlessSoftBodyPart.Factory.ChildrenFactory):
#             def builders(self):
#                 yield Teeth
#                 yield from super().builders()
