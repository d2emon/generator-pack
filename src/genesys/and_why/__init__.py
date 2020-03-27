from factories.random_factory import DataItemFactory, RandomFactory
from models.and_why import DollModel, genders
from models.data_manager import DataManager
from sample_data.and_why import groups


class ClothingManager(DataManager):
    class DataProvider(DataManager.DataProvider):
        def __init__(self):
            self.__factories = {
                genders.MALE: DataItemFactory(groups.MALE),
                genders.FEMALE: DataItemFactory(groups.FEMALE),

            }

        def gender_factory(self, gender):
            return self.__factories[gender]

    @classmethod
    def by_gender(cls, gender):
        return cls.get_provider().gender_factory(gender).data


class Doll(DollModel):
    def fill(self, items=None):
        super().fill(items or ClothingManager.by_gender(self.gender))


class DollManager(DataManager):
    class DataProvider(DataManager.DataProvider):
        def __init__(self):
            self.__genders = RandomFactory([
                genders.MALE,
                genders.FEMALE,
            ])

        @property
        def genders(self):
            return self.__genders

    @classmethod
    def doll(cls, gender=None):
        return Doll(gender or next(cls.get_provider().genders))

    @classmethod
    def male(cls):
        return cls.doll(genders.MALE)

    @classmethod
    def female(cls):
        return cls.doll(genders.FEMALE)
