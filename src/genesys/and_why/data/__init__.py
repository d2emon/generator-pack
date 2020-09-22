from orm.models.data_item import DataItem
from . import egypt, genders


def fill():
    DataItem.add_values(genders.MALE, egypt.male)
    DataItem.add_values(genders.FEMALE, egypt.female)
