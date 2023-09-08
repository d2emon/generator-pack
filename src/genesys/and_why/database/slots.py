from ..data import slots
from database.data_item_database import DataItemDatabase


SLOTS = DataItemDatabase(
    slots.IN_HAND,
    slots.SHIELD,
    slots.HEAD,
    slots.NECK,
    slots.TORSO,
    slots.HIPS,
)
