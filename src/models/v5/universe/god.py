"""
- GodThoughts (Unused)
- GodPsyche (Unused)
- God (Unused)
"""
from models.v5.model import Model


class GodThoughts(Model):
    # Thoughts
    default_name = 'thoughts'


class GodPsyche(Model):
    default_name = 'psyche'
    thoughts = Model.child_property(GodThoughts)


class God(Model):
    # body = Model.child_property(Body)
    psyche = Model.child_property(GodPsyche)
    # clothes = Model.child_property(ClothingSet)
    # computer = Model.child_property(Computer)
