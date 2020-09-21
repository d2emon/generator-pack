from providers.data_manager import DataManager
from ..models import Doll
from ..providers import DollDataProvider


class DollManager(DataManager):
    def __init__(self, provider=None):
        super().__init__(provider or DollDataProvider())

    @classmethod
    def doll(cls, gender=None):
        return Doll(gender or next(cls.get_provider().genders))

    @classmethod
    def male(cls):
        return Doll(cls.get_provider().MALE)

    @classmethod
    def female(cls):
        return Doll(cls.get_provider().FEMALE)
