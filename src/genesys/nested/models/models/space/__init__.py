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

# from .galaxy import *
# from .nebula import *
# from .star import *
# from .planet import *
# from .black_hole import *
from genesys.nested.models import Model
from genesys.nested.data import lookups


class Supercluster(Model):
    default_name = 'galactic supercluster'
    # galaxies = Model.children_property(Galaxy)

    class Factory(Model.Factory):
        class ChildrenFactory(Model.Factory.ChildrenFactory):
            def builders(self):
                # yield from Galaxy.multiple(10, 30)
                yield from []


class Universe(Model):
    clusters = Model.children_property(Supercluster)

    class Factory(Model.Factory):
        class ChildrenFactory(Model.Factory.ChildrenFactory):
            def builders(self):
                yield from Supercluster.multiple(10, 30)


class Multiverse(Model):
    universes = Model.children_property(Universe)

    class DataProvider:
        multiverse = lookups.multiverses.values

    class Factory(Model.Factory):
        class BaseFactory(Model.Factory.BaseFactory):
            data = property(lambda self: self.provider.multiverse)

        class ChildrenFactory(Model.Factory.ChildrenFactory):
            def builders(self):
                yield from Universe.multiple(10, 30)
