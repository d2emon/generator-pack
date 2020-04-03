"""
Universe stuff

- Multiverse
- Universe
- Supercluster
- Galaxy Arm
- Galaxy Center
- Nebula
- Interstellar Cloud
- StarSystem
- DysonSphere
- Star
- Planet
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

from .galaxy import *
from .nebula import *
from .star import *
from .planet import *
from .black_hole import *

from genesys.nested.models import Model


class Supercluster(Model):
    default_name = 'galactic supercluster'
    galaxies = Model.children_property(Galaxy)


class Universe(Model):
    clusters = Model.children_property(Supercluster)


class Multiverse(Model):
    universes = Model.children_property(Universe)
