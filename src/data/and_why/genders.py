from utils.genders import MALE, FEMALE
from .db import Database


DEFAULT = MALE


GENDERS = Database(
    MALE,
    FEMALE,
)
