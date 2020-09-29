# terrain stuff
from .water import Ocean, Sea, SeaWater, Iceberg, Beach, Abyss, River, Lake
from .soil import Sand, Soil, Mud
from .land import Landscape, Plain, Forest, Jungle, Mountain, Cave
from .sky import Sky, Meteorite, Ozone, Cloud, Precipitation


# class Biome(Thing):
#     child_generators = [
#         ChildGenerator("plain", (1, 5)),
#         [
#             ChildGenerator("forest", (0, 4)),
#             ChildGenerator("jungle", (0, 4)),
#         ],
#         ChildGenerator("mountain", (0, 3))
#     ]
