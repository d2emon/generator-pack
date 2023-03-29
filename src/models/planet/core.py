"""
- PlanetCore
"""
from models.tree_model import TreeModel
# from models.v5.materials import Rock
# from models.v5.life import Life


class PlanetCore(TreeModel):
    # life = TreeModel.child_property(Life)
    # minerals = TreeModel.children_property(Rock)

    default_name = 'core'
