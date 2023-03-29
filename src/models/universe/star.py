"""
- Star
- StarSystem
"""
from models.tree_model import TreeModel
# from models.v5.materials import Atom
# from models.v5.life import Life
from .orbit import Orbit, PlanetOrbit, AsteroidBelt
from ..planet import Planet


class Star(TreeModel):
    # life = TreeModel.child_property(Life)
    # matter = TreeModel.children_property(Atom)
    pass


class StarSystem(TreeModel):
    main_star = TreeModel.child_property(Star)
    stars = TreeModel.children_property(Star)
    orbits = TreeModel.children_property(Orbit)
    planets = TreeModel.children_property(Planet)
    asteroid_belts = TreeModel.children_property(AsteroidBelt)
    # dyson_surfaces = Model.children_property(DysonSurface)


# Dyson


class DysonSphere(StarSystem):
    pass


# class DysonSurface(Thing):
#     type_name = "dyson surface"
#     child_generators = [ChildGenerator("dyson segment", (16,))]


# class DysonSegment(Thing):
#     type_name = "dyson segment"
#     child_generators = [
#         ChildGenerator("future city", (4, 20)),
#         ChildGenerator("nanocollector", (12, 20)),
#     ]
