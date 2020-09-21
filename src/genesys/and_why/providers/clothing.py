from providers import RandomItemProvider
from ..sample_data.genders import GENDERS
from ..sample_data import fill


class ClothingDataProvider:
    __filled = False

    def __init__(self):
        self.__factories = {gender: RandomItemProvider(gender) for gender in GENDERS}
        if not self.__filled:
            fill()
            self.__filled = True

    def by_gender(self, gender):
        return self.__factories[gender]
