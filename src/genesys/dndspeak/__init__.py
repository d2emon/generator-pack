from models.data_item import DataItem
from models.list_item import SimpleItem
from sample_data.dndspeak import groups


class DesertEncounter(SimpleItem):
    class ItemGenerator:
        default = DataItem.get_values_by_group(groups.DESERT_ENCOUNTERS)


class SailingConditions(SimpleItem):
    class ItemGenerator:
        default = DataItem.get_values_by_group(groups.SAILING_CONDITIONS)
