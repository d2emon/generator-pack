"""
- Star
- StarSystem
"""
from models.nested_model import NestedModel
# from models.v5.materials import Atom
# from models.v5.life import Life
from .orbit import Orbit, PlanetOrbit, AsteroidBelt


class Star(NestedModel):
    # life = NestedModel.child_property(Life)
    # matter = NestedModel.children_property(Atom)
    pass


class StarSystem(NestedModel):
    main_star = NestedModel.child_property(Star)
    stars = NestedModel.children_property(Star)
    orbits = NestedModel.children_property(Orbit)
    planets = NestedModel.children_property(PlanetOrbit)
    asteroid_belts = NestedModel.children_property(AsteroidBelt)
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
