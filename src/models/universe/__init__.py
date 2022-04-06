"""
- Supercluster
- Universe
- Multiverse

####

Universe stuff

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
from models.nested_model import NestedModel as Model
from .galaxy import Galaxy


class Supercluster(Model):
    default_name = 'galactic supercluster'
    galaxies = Model.children_property(Galaxy)


class Universe(Model):
    clusters = Model.children_property(Supercluster)


class Multiverse(Model):
    universes = Model.children_property(Universe)
