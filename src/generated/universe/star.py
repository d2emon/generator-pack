"""
- Star
- StarSystem
"""
from genesys.model.model import Model
# from generated.nested_v2.models import DysonSurface
# from genesys.nested.data import lookups
# from generated.universe.space.life import Habitat, StarLife
from ..materials import Atom
from .orbit import Orbit, PlanetOrbit, AsteroidBelt


class Star(Model):
    # Habitat
    matter = Model.children_property(Atom)


class StarSystem(Model):
    main_star = Model.child_property(Star)
    stars = Model.children_property(Star)
    orbits = Model.children_property(Orbit)
    planets = Model.children_property(PlanetOrbit)
    asteroid_belts = Model.children_property(AsteroidBelt)
    # dyson_surfaces = Model.children_property(DysonSurface)


# Dyson


# class DysonSurface(Thing):
#     type_name = "dyson surface"
#     child_generators = [ChildGenerator("dyson segment", (16,))]


# class DysonSegment(Thing):
#     type_name = "dyson segment"
#     child_generators = [
#         ChildGenerator("future city", (4, 20)),
#         ChildGenerator("nanocollector", (12, 20)),
#     ]
