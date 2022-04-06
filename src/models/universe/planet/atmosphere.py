"""
- Atmosphere
"""
from models.nested_model import NestedModel
# from models.v5.materials import Gas
# from models.v5.life import Life


class Atmosphere(NestedModel):
    # life = NestedModel.child_property(Life)
    # gases = NestedModel.children_property(Gas)

    default_name = 'atmosphere'
