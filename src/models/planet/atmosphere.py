"""
- Atmosphere
"""
from models.nested_model import TreeModel
# from models.v5.materials import Gas
# from models.v5.life import Life


class Atmosphere(TreeModel):
    # life = TreeModel.child_property(Life)
    # gases = TreeModel.children_property(Gas)

    default_name = 'atmosphere'
