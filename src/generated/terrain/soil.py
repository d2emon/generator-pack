"""
- Soil
- Mud
- Sand
"""
from genesys.model.model import Model
from ..materials import Silica, Water


class Soil(Model):
    # Habitat
    silica = Model.child_property(Silica)
    water = Model.child_property(Water)

    default_name = 'dirt'


class Mud(Soil):
    default_name = 'mud'


class Sand(Soil):
    default_name = 'sand'
