from factories.factory import Factory
from factories.list_factory import ListFactory
from ..providers.gender_provider import GENDER_PROVIDER


class GenderFactory(Factory):
    def __init__(self, data=None):
        self.__data = data or GENDER_PROVIDER

    @property
    def data(self):
        return self.__data

    @property
    def male(self):
        return self(self.data.male)

    @property
    def female(self):
        return self(self.data.female)

    def __call__(self, gender=None, *args, **kwargs):
        """
        Select random item

        :param gender: Set gender
        :param args: Roll args
        :param kwargs: Roll kwargs
        :return: Random item
        """
        if (gender is not None):
            return gender

        return self.data.gender()
