from models.data_item import DataItem
from . import groups
from .desert_encounters import ITEMS as DESERT_ENCOUNTERS
from .sailing_conditions import ITEMS as SAILING_CONDITIONS


def fill():
    DataItem.add_values(groups, DESERT_ENCOUNTERS)
    DataItem.add_values(groups, SAILING_CONDITIONS)
