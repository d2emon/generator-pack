from data.and_why.genders import DEFAULT, GENDERS, MALE, FEMALE
from factories.and_why import ListFactory


class GenderProvider:
    default_gender = DEFAULT
    genders = GENDERS
    male = MALE
    female = FEMALE

    __factory = ListFactory(GENDERS)

    @classmethod
    def gender(cls):
        return cls.__factory()
