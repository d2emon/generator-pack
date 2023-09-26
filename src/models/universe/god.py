"""
- GodThoughts (Unused)
- GodPsyche (Unused)
- God (Unused)
"""
from models.nested_model import TreeModel


class GodThoughts(TreeModel):
    # Thoughts
    default_name = 'thoughts'


class GodPsyche(TreeModel):
    default_name = 'psyche'
    thoughts = TreeModel.child_property(GodThoughts)


class God(TreeModel):
    # body = Model.child_property(Body)
    psyche = TreeModel.child_property(GodPsyche)
    # clothes = Model.child_property(ClothingSet)
    # computer = Model.child_property(Computer)
