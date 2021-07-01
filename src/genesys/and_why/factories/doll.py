from factories.and_why import ModelFactory
from ..models import Doll
from ..providers.doll_provider import DollProvider
from .gender import GenderFactory


class DollFactory(ModelFactory):
    def __init__(self, data=DollProvider):
        super().__init__(data)
        self.__gender_factory = GenderFactory(data.genders)

    @property
    def model_class(self):
        return Doll

    def __call__(self, gender=None, *args, **kwargs):
        return self.model_class(gender=gender or self.__gender_factory())

    def male(self):
        return self(self.__gender_factory.male)

    def female(self):
        return self(self.__gender_factory.female)
