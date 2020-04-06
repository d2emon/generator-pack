from genesys.nested.factories.thing_builder import ThingBuilder
from genesys.nested.models import Model
from ....chemistry import Water, Salt
from ..body_parts import SoftBodyPart
from ..blood import BloodVessels
from ..skeleton import Fat
from .hair import Hair


class Tear(Model):
    water = Model.child_property(Water)
    salt = Model.child_property(Salt)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield Water
                yield Salt


class Eyelashes(Hair):
    pass


class EyeFlesh(SoftBodyPart):
    water = SoftBodyPart.child_property(Water)

    default_name = 'eyeball'

    class Factory(SoftBodyPart.Factory):
        class ChildrenFactory(SoftBodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Water
                yield BloodVessels
                yield Fat


class Eye(SoftBodyPart):
    eyelashes = SoftBodyPart.child_property(Eyelashes)
    eye_flesh = SoftBodyPart.child_property(EyeFlesh)
    tear = SoftBodyPart.child_property(Tear)

    class Factory(SoftBodyPart.Factory):
        class ChildrenFactory(SoftBodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Eyelashes
                yield EyeFlesh
                yield Tear.probable(2)
