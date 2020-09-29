"""
- EyeFlesh
- SimpleEye
"""
from ...materials import Water
from .body_parts import BodyPart


class EyeFlesh(BodyPart):
    default_name = 'eyeball'

    water = BodyPart.child_property(Water)


class SimpleEye(EyeFlesh):
    default_name = 'eye'
