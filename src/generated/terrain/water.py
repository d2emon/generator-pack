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
from genesys.model.model import Model
from ..materials import Ice, Salt, Water
from .soil import Soil


class Abyss(Model):
    soil = Model.child_property(Soil)


class Beach(Model):
    soil = Model.child_property(Soil)


class Iceberg(Model):
    soil = Model.child_property(Ice)


class SeaWater(Water):
    salt = Water.child_property(Salt)


class Sea(Model):
    # Habitat
    water = Model.child_property(Water)
    beaches = Model.children_property(Beach)


class Ocean(Sea):
    abyss = Sea.child_property(Abyss)
    icebergs = Sea.children_property(Iceberg)


class River(Model):
    soil = Model.children_property(Soil)
    water = Model.child_property(Water)


class Lake(Model):
    soil = Model.children_property(Soil)
    water = Model.child_property(Water)
