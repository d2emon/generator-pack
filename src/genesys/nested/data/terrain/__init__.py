"""
Terrain Stuff

- Ocean
- Sea
- Sea Water
- Iceberg
- Beach
- Abyss
- River
- Lake

- Sand
- Soil
- Mud

- Plain
- Forest
- Jungle
- Mountain
- Cave

- Ancient Plain
- Ancient Forest
- Ancient Jungle
- Ancient Mountain
- Ancient Cave

- Future Sky
- Terraformed Sky
- Sky
- Meteorite
- Ozone
- Cloud
- Precipitation
"""
from .water import *
from .soil import *
from .land import *
from .ancient import *
from .sky import *


# class Biome(Thing):
#     child_generators = [
#         ChildGenerator("plain", (1, 5)),
#         [
#             ChildGenerator("forest", (0, 4)),
#             ChildGenerator("jungle", (0, 4)),
#         ],
#         ChildGenerator("mountain", (0, 3))
#     ]


# ChildGenerator("sea life"),
# ChildGenerator("salt"),
# ChildGenerator("bear", probability=10),
# ChildGenerator("beach life"),
# ChildGenerator("abyss life"),
# ChildGenerator("visitor ship", probability=10),
# ChildGenerator("sky life"),
# ChildGenerator("plane", (1, 8)),
# ChildGenerator("rocketship", probability=20),
# ChildGenerator("sprowseship", (4, 12)),
