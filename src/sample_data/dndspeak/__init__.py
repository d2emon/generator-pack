from .desert_encounters import ITEMS as DESERT_ENCOUNTERS
from .sailing_conditions import ITEMS as SAILING_CONDITIONS

from sample_data.database import add_to_group


__ITEMS = {
    'desert-encounters': DESERT_ENCOUNTERS,
    'sailing-conditions': SAILING_CONDITIONS,
}


def fill():
    for group_id, items in __ITEMS.items():
        for item in items:
            add_to_group(group_id, item)
