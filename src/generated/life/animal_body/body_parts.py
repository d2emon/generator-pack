"""
- BodyPart
- Flesh
- SoftFlesh
- WeirdOrgan
"""
from genesys.model.model import Model
from ...materials import Sweat
from .blood import BloodVessels
from .skin import Skin
from .skeleton import Bones, Muscles, Fat


class BodyPart(Model):
    # bacterias = Model.children_property(Bacteria)
    skin = Model.child_property(Skin)
    blood_vessels = Model.child_property(BloodVessels)
    bones = Model.child_property(Bones)
    fat = Model.child_property(Fat)
    muscles = Model.child_property(Muscles)
    sweat = Model.child_property(Sweat)


class Flesh(BodyPart):
    default_name = 'flesh'


class SoftFlesh(Flesh):
    default_name = 'flesh'


class WeirdOrgan(BodyPart):
    pass
