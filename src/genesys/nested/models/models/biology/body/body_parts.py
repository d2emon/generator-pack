from genesys.nested.models.models.unknown import Bacteria
from genesys.nested.factories.thing_builder import ThingBuilder
from genesys.nested.models import Model
from .blood import BloodVessels
from .skin import Skin
from .skeleton import Bones, Fat, Muscles


class BodyPart(Model):
    bacterias = Model.children_property(Bacteria)
    skin = Model.child_property(Skin)
    blood_vessels = Model.child_property(BloodVessels)
    bones = Model.child_property(Bones)
    fat = Model.child_property(Fat)
    muscles = Model.child_property(Muscles)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            has_bones = True
            has_skin = True

            def builders(self):
                yield Bacteria.probable(30)
                yield Bacteria.probable(10)
                if self.has_skin:
                    yield Skin
                yield BloodVessels
                if self.has_bones:
                    yield Bones
                yield Fat
                yield Muscles


class SoftBodyPart(BodyPart):
    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            has_bones = False
            has_skin = True


class SkinlessBodyPart(BodyPart):
    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            has_bones = True
            has_skin = False


class SkinlessSoftBodyPart(BodyPart):
    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            has_bones = False
            has_skin = False
