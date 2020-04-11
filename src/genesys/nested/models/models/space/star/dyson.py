from genesys.nested.models.models.unknown import DysonSurface
from .star import StarSystem


class DysonSphere(StarSystem):
    class Factory(StarSystem.Factory):
        @classmethod
        def _generate_inhabited(cls):
            yield DysonSurface
            # yield from planet.FuturePlanet.multiple(1, 8)
            yield None


# class DysonSurface(Thing):
#     type_name = "dyson surface"
#     child_generators = [ChildGenerator("dyson segment", (16,))]


# class DysonSegment(Thing):
#     type_name = "dyson segment"
#     child_generators = [
#         ChildGenerator("future city", (4, 20)),
#         ChildGenerator("nanocollector", (12, 20)),
#     ]
