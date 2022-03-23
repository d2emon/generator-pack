from database.data_item_database import DataItemDatabase
from . import groups
from .desert_encounters import ITEMS as DESERT_ENCOUNTERS
from .sailing_conditions import ITEMS as SAILING_CONDITIONS


DataItemDatabase.add_to_group(groups.DESERT_ENCOUNTERS, DESERT_ENCOUNTERS)
DataItemDatabase.add_to_group(groups.SAILING_CONDITIONS, SAILING_CONDITIONS)
