from data.genders import MALE, FEMALE
from database.data_item_database import DataItemDatabase


DEFAULT = MALE


GENDERS = DataItemDatabase(
    MALE,
    FEMALE,
)
