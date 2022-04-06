"""
- GodThoughts (Unused)
- GodPsyche (Unused)
- God (Unused)
"""
from models.nested_model import NestedModel


class GodThoughts(NestedModel):
    # Thoughts
    default_name = 'thoughts'


class GodPsyche(NestedModel):
    default_name = 'psyche'
    thoughts = NestedModel.child_property(GodThoughts)


class God(NestedModel):
    # body = Model.child_property(Body)
    psyche = NestedModel.child_property(GodPsyche)
    # clothes = Model.child_property(ClothingSet)
    # computer = Model.child_property(Computer)
