"""
- FishFin
- FishTail
- FishSkin
"""
from models.nested_model import NestedModel as Model
from .limb import Limb, Tail
from .skin import Skin, Scales


class FishFin(Limb):
    default_name = 'fin'
    scales = Model.child_property(Scales)


class FishTail(Tail):
    default_name = 'tail'
    scales = Model.child_property(Scales)


class FishSkin(Skin):
    default_name = 'skin'
    scales = Skin.child_property(Scales)
