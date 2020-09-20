from providers import DataProvider
from factories import ListFactory
from utils import genders


class DollDataProvider(DataProvider):
    def __init__(self):
        self.__genders = ListFactory(None, [
            genders.MALE,
            genders.FEMALE,
        ])

    def __next__(self):
        raise NotImplementedError()

    @property
    def genders(self):
        return self.__genders
