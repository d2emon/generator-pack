from factories.list_factory import ListFactory
from ..providers.gender_provider import GENDER_PROVIDER


class GenderFactory(ListFactory):
    def __init__(self, data=None):
        super().__init__(data or GENDER_PROVIDER)

    @property
    def male(self):
        return self(self.data.male)

    @property
    def female(self):
        return self(self.data.female)
