from factories.model.model import ModelFactory
from ..models import Doll
from .gender import GenderFactory


class DollFactory(ModelFactory):
    def __init__(self, data=None):
        super().__init__()

        self.__gender_factory = GenderFactory(data)

    @property
    def model_class(self):
        return Doll

    def __call__(self, gender=None, *args, **kwargs):
        return self.model_class(gender=gender or self.__gender_factory())

    def male(self):
        return self(self.__gender_factory.male)

    def female(self):
        return self(self.__gender_factory.female)
