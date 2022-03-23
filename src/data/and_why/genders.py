from data.genders import MALE, FEMALE
from orm import Database


DEFAULT = MALE


GENDERS = Database(
    MALE,
    FEMALE,
)
