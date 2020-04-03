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
from genesys.nested.factories.thing_builder import ThingBuilder
from genesys.nested.data import lookups


class Supercluster(Model):
    galaxies = Model.children_property(Galaxy)

    class NameFactory(Model.NameFactory):
        default = 'galactic supercluster'

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield from Galaxy.multiple(10, 30)


class UniverseBuilder(ThingBuilder):
    class Universe(Model):
        clusters = Model.children_property(Supercluster)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield from Supercluster.multiple(10, 30)

    model = Universe


class Multiverse(Model):
    universes = Model.children_property(UniverseBuilder.Universe)

    class NameFactory(Model.NameFactory):
        default = None

    class BaseFactory(Model.BaseFactory):
        default = lookups.multiverses.values

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield from UniverseBuilder.Universe.multiple(10, 30)
