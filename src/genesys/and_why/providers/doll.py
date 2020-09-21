from factories import ListFactory
from ..sample_data.genders import GENDERS, MALE, FEMALE


class DollDataProvider:
    MALE = MALE
    FEMALE = FEMALE

    def __init__(self):
        self.__genders = ListFactory(None, GENDERS)

    @property
    def genders(self):
        return self.__genders
