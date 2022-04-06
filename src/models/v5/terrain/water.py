"""
- Abyss
- Beach
- Iceberg
- SeaWater
- Sea
- Ocean
- River
- Lake
"""
from models.nested_model import Model
from ..materials import Ice, Salt, Water
from ..life import Life
from .soil import Soil


class Abyss(Model):
    soil = Model.child_property(Soil)


class Beach(Model):
    soil = Model.child_property(Soil)


class Iceberg(Model):
    soil = Model.child_property(Ice)


class SeaWater(Water):
    salt = Water.child_property(Salt)


class WaterBody(Model):
    life = Model.child_property(Life)
    soil = Model.children_property(Soil)
    water = Model.child_property(Water)


class Sea(WaterBody):
    beaches = Model.children_property(Beach)


class Ocean(Sea):
    default_name = 'ocean'
    abyss = Sea.child_property(Abyss)
    icebergs = Sea.children_property(Iceberg)


class River(WaterBody):
    pass


class Lake(WaterBody):
    pass
