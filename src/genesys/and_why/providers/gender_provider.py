from data.and_why.genders import DEFAULT, GENDERS
from factories.and_why import ListFactory
from providers import RandomItemProvider
from utils.genders import MALE, FEMALE


class GenderProvider:
    def __init__(self):
        self.default_gender = DEFAULT
        self.genders = GENDERS.values()
        self.male = MALE
        self.female = FEMALE
        self.__gender_factory = ListFactory(self.genders)
        self.gender_factories = { gender: RandomItemProvider(gender) for gender in self.genders }

    def build_gender(self):
        return self.__gender_factory()

    def by_gender(self, gender):
        factory = self.gender_factories.get(gender)
        return factory.data if factory else None


GENDER_PROVIDER = GenderProvider()
