from providers.data_manager import DataManager
from ..models import Doll
from ..providers import DollDataProvider
from ..data.genders import DEFAULT


class DollManager(DataManager):
    def __init__(self, provider=None):
        super().__init__(provider or DollDataProvider())

    @classmethod
    def gender(cls):
        return next(cls.get_provider().genders)

    @classmethod
    def doll(cls, gender=None):
        return Doll(gender or cls.gender())

    @classmethod
    def male(cls):
        return cls.doll(cls.get_provider().MALE)

    @classmethod
    def female(cls):
        return cls.doll(cls.get_provider().FEMALE)

    @classmethod
    def by_gender(cls, gender=None):
        return cls.get_provider().by_gender(gender or DEFAULT).data
