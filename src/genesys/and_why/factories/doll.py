from factories.model_factory import ModelFactory
from ..models import Doll
from ..providers import PROVIDER
from .gender import GenderFactory


class Subfactories:
    def __init__(self, data):
        self.gender = GenderFactory(data)


class DollFactory(ModelFactory):
    model = Doll

    def __init__(self, data=None):
        super().__init__(data or PROVIDER)
        self.__subfactories = Subfactories(self.data_provider)

    def __call__(self, gender=None, *args, **kwargs):
        if gender is None:
            gender = self.__subfactories.gender()

        return self.model(
            gender=gender,
            *args,
            **kwargs,
        )

    def male(self):
        return self(self.__subfactories.gender.male)

    def female(self):
        return self(self.__subfactories.gender.female)
