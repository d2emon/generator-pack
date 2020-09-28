"""
- Tear
- Eyelashes
- EyeFlesh
- Eye
"""
from ....materials import Water, OrganicMatter
from ..body_parts import BodyPart
from .hair import Hair


class Tear(OrganicMatter):
    pass


class Eyelashes(Hair):
    pass


class EyeFlesh(BodyPart):
    default_name = 'eyeball'

    water = BodyPart.child_property(Water)


class Eye(BodyPart):
    eyelashes = BodyPart.child_property(Eyelashes)
    eye_flesh = BodyPart.child_property(EyeFlesh)
    tear = BodyPart.child_property(Tear)
