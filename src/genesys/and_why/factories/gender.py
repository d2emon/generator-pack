from factories.factory import Factory
from ..providers import PROVIDER


class GenderFactory(Factory):
    def __init__(self, data=None):
        super().__init__(data or PROVIDER)

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
        if gender is not None:
            return gender

        return self.data.gender()
