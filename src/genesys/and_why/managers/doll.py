from utils import genders
from providers.data_manager import DataManager
from ..doll import Doll


class DollManager(DataManager):
    @classmethod
    def doll(cls, gender=None):
        return Doll(gender or next(cls.get_provider().genders))

    @classmethod
    def male(cls):
        return cls.doll(genders.MALE)

    @classmethod
    def female(cls):
        return cls.doll(genders.FEMALE)
