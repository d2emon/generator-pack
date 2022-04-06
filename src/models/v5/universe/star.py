"""
- Star
- StarSystem
"""
from models.nested_model import NestedModel as Model
from ..materials import Atom
from ..life import Life
from .orbit import Orbit, PlanetOrbit, AsteroidBelt


class Star(Model):
    life = Model.child_property(Life)
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
