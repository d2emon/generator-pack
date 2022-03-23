from orm.db import Database


IN_HAND = 1
SHIELD = 2
HEAD = 3
NECK = 4
TORSO = 5
HIPS = 6


SLOTS = Database(
    IN_HAND,
    SHIELD,
    HEAD,
    NECK,
    TORSO,
    HIPS,
)
