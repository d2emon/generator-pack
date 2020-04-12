from genesys.nested.models.models.unknown import DysonSurface
from .star import StarSystem
from ..planet import FuturePlanet


class DysonSphere(StarSystem):
    class Factory(StarSystem.Factory):
        @classmethod
        def _generate_inhabited(cls):
            yield DysonSurface
            yield from FuturePlanet.multiple(1, 8)


# class DysonSurface(Thing):
#     type_name = "dyson surface"
#     child_generators = [ChildGenerator("dyson segment", (16,))]


# class DysonSegment(Thing):
#     type_name = "dyson segment"
#     child_generators = [
#         ChildGenerator("future city", (4, 20)),
#         ChildGenerator("nanocollector", (12, 20)),
#     ]
