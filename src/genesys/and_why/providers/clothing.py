from utils import genders
from providers import DataProvider, RandomItemProvider
from ..sample_data import groups


class ClothingDataProvider(DataProvider):
    def __init__(self):
        self.__factories = {
            genders.MALE: RandomItemProvider(groups.MALE),
            genders.FEMALE: RandomItemProvider(groups.FEMALE),

        }

    def __next__(self):
        raise NotImplementedError()

    def gender_factory(self, gender):
        return self.__factories[gender]
