from data.and_why.genders import DEFAULT, GENDERS
from factories.and_why import ListFactory
from providers import RandomItemProvider
from utils.genders import MALE, FEMALE


class BaseGenderProvider:
    @property
    def default_gender(self):
        return DEFAULT

    @property
    def male(self):
        return MALE

    @property
    def female(self):
        return FEMALE

    def gender(self):
        raise NotImplementedError()


class GenderProvider(BaseGenderProvider):
    def __init__(self):
        genders = GENDERS.values()

        # Factories
        self.__gender_factory = ListFactory(genders)

        # Providers
        self.__providers = { gender: RandomItemProvider(gender) for gender in genders }

    def gender(self):
        return self.__gender_factory()

    def by_gender(self, gender):
        provider = self.__providers.get(gender)
        return provider.data if provider else None


GENDER_PROVIDER = GenderProvider()
