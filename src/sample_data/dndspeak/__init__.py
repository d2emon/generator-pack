from models.data_item import DataItem
from .desert_encounters import ITEMS as DESERT_ENCOUNTERS
from .sailing_conditions import ITEMS as SAILING_CONDITIONS


def fill():
    DataItem.add_values('desert-encounters', DESERT_ENCOUNTERS)
    DataItem.add_values('sailing-conditions', SAILING_CONDITIONS)
