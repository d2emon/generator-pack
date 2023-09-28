"""
- Star
- StarSystem
"""
from models.nested_model import NestedModel
# from models.v5.materials import Atom
from models.v5.life import Life
from models.materials.matter import Matter
from .orbit import Orbit


class Star(Matter):
    life = NestedModel.child_property(Life)


class StarSystem(NestedModel):
    main_star = NestedModel.child_property(Star)
    stars = NestedModel.children_property(Star)
    orbits = NestedModel.children_property(Orbit)
    # asteroid_belts = NestedModel.children_property(AsteroidBelt)
    # # dyson_surfaces = NestedModel.children_property(DysonSurface)

    @property
    def planets(self):
        for orbit in self.orbits:
            yield from orbit.planets


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
