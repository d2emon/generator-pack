from generated import life
from ...factory import Factory
from .blood import BloodVesselsFactory
from .skeleton import BonesFactory, MuscleFactory, FatFactory
from .skin import SkinFactory


class BodyPartFactory(Factory):
    default_model = life.BodyPart

    has_bones = True
    has_skin = True

    def children(self):
        # yield Bacteria.probable(30)
        # yield Bacteria.probable(10)
        if self.has_skin:
            yield SkinFactory()
        yield BloodVesselsFactory()
        if self.has_bones:
            yield BonesFactory()
        yield FatFactory()
        yield MuscleFactory()


class SoftBodyPartFactory(BodyPartFactory):
    has_bones = False
    has_skin = True


class SkinlessBodyPartFactory(BodyPartFactory):
    has_bones = True
    has_skin = False


class SkinlessSoftBodyPartFactory(BodyPartFactory):
    has_bones = False
    has_skin = False
