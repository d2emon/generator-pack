from genesys.model.model import Model
from .limb import Limb
from .skin import Skin, Scales


class FishFin(Limb):
    default_name = 'fin'
    scales = Model.child_property(Scales)


class FishTail(Limb):
    default_name = 'tail'
    scales = Model.child_property(Scales)


class FishSkin(Skin):
    default_name = 'skin'
    scales = Skin.child_property(Scales)
