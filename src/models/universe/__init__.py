"""
Universe stuff

- Supercluster
- Universe
- Multiverse

####

- Barren Planet
- Visitor Planet
- Future Planet
- Terraformed Planet
- Medieval Planet
- Ancient Planet
- Moon
- Terraformed Moon
- Asteroid Belt
- Earth
- Asteroid
- Gas Giant
- Gas Giant Atmosphere
- Planet Core
- Black Hole

- White Hole
- 42
- Everything
- End of Universe Note

- D2emon
- God
- D2emon Psyche
- D2emon Thoughts
"""
from models.tree_model import TreeModel
from .galaxy import Galaxy


class Supercluster(TreeModel):
    default_name = 'galactic supercluster'

    galaxies = TreeModel.children_property(Galaxy)


class Universe(TreeModel):
    clusters = TreeModel.children_property(Supercluster)


class Multiverse(TreeModel):
    universes = TreeModel.children_property(Universe)
