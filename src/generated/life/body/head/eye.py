"""
- Tear
- Eyelashes
- EyeFlesh
- Eye
"""
from ....materials import OrganicMatter
from ...animal_body.body_parts import BodyPart
from ...animal_body.hair import Hair
from ...animal_body.eye import EyeFlesh


class Tear(OrganicMatter):
    pass


class Eyelashes(Hair):
    pass


class Eye(BodyPart):
    eyelashes = BodyPart.child_property(Eyelashes)
    eye_flesh = BodyPart.child_property(EyeFlesh)
    tear = BodyPart.child_property(Tear)
