from ... import unknown
from .star import StarSystem
from .. import planet
# from genesys.nested.factories import Thing, ChildFactory


class DysonSphere(StarSystem):
    class ChildrenFactory(StarSystem.ChildrenFactory):
        @classmethod
        def _generate_inhabited(cls):
            yield unknown.DysonSurface
            yield from planet.FuturePlanet.multiple(1, 8)


# class DysonSurface(Thing):
#     type_name = "dyson surface"
#     child_generators = [ChildGenerator("dyson segment", (16,))]


# class DysonSegment(Thing):
#     type_name = "dyson segment"
#     child_generators = [
#         ChildGenerator("future city", (4, 20)),
#         ChildGenerator("nanocollector", (12, 20)),
#     ]