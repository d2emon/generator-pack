from models.and_why import genders
from models.data_item import DataItem
from . import egypt


def fill():
    DataItem.add_values(genders.MALE, egypt.male)
    DataItem.add_values(genders.FEMALE, egypt.female)
