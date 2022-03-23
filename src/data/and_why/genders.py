from data.genders import MALE, FEMALE
from database.orm import Database


DEFAULT = MALE


GENDERS = Database(
    MALE,
    FEMALE,
)
