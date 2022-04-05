"""
- EyeFlesh
- SimpleEye ???
- Tear
- Eyelashes
- Eye
"""
from models.v5.materials import Water
from ....materials import OrganicMatter
from ..body_parts import BodyPart
from ..hair import Hair


class EyeFlesh(BodyPart):
    default_name = 'eyeball'

    water = BodyPart.child_property(Water)


class SimpleEye(EyeFlesh):
    default_name = 'eye'


class Tear(OrganicMatter):
    pass


class Eyelashes(Hair):
    pass


class Eye(BodyPart):
    eyelashes = BodyPart.child_property(Eyelashes)
    eye_flesh = BodyPart.child_property(EyeFlesh)
    tear = BodyPart.child_property(Tear)
