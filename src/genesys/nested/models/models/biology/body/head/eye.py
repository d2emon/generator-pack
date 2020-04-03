from genesys.nested.models import Model
from ....chemistry import Water, Salt
from ..body_parts import SoftBodyPart
from ..blood import BloodVessels
from ..skeleton import Fat
from .hair import Hair


class Tear(Model):
    water = Model.child_property(Water)
    salt = Model.child_property(Salt)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Water
            yield Salt


class Eyelashes(Hair):
    pass


class EyeFlesh(SoftBodyPart):
    water = SoftBodyPart.child_property(Water)

    class NameFactory(SoftBodyPart.NameFactory):
        default = 'eyeball'

    class ChildrenFactory(SoftBodyPart.ChildrenFactory):
        def children_classes(self):
            yield Water
            yield BloodVessels
            yield Fat


class Eye(SoftBodyPart):
    eyelashes = SoftBodyPart.child_property(Eyelashes)
    eye_flesh = SoftBodyPart.child_property(EyeFlesh)
    tear = SoftBodyPart.child_property(Tear)

    class ChildrenFactory(SoftBodyPart.ChildrenFactory):
        def children_classes(self):
            yield Eyelashes
            yield EyeFlesh
            yield Tear.probable(2)
