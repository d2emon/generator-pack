from factories.and_why import ListFactory
from ..providers.gender_provider import GenderProvider


class GenderFactory(ListFactory):
    def __init__(self, data=None):
        super().__init__(data or GenderProvider())

    @property
    def male(self):
        return self(self.data.male)

    @property
    def female(self):
        return self(self.data.female)
