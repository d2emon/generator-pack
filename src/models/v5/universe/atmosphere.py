"""
- Atmosphere
"""
from models.nested_model import Model
from ..materials import Gas
from ..life import Life


class Atmosphere(Model):
    life = Model.child_property(Life)
    gases = Model.children_property(Gas)

    default_name = 'atmosphere'
