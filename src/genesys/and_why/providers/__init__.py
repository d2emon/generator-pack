from factories import ListFactory
from providers import RandomItemProvider
from ..data import fill
from ..data.genders import GENDERS, MALE, FEMALE


class DollDataProvider:
    MALE = MALE
    FEMALE = FEMALE

    __filled = False

    def __init__(self):
        self.__genders = ListFactory(GENDERS)
        self.__factories = {gender: RandomItemProvider(gender) for gender in GENDERS}
        if not self.__filled:
            fill()
            self.__filled = True

    @property
    def genders(self):
        return self.__genders

    def by_gender(self, gender):
        return self.__factories[gender]
