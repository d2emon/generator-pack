from models.data_item import DataItem
from . import egypt, groups


def fill():
    DataItem.add_values(groups.MALE, egypt.male)
    DataItem.add_values(groups.FEMALE, egypt.female)
