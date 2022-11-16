from data.fixtures.fixtures import vowel_sounds, consonants, double_vowel_sounds, double_consonants
from data.fixtures.fixtures import endings
from genesys.fng.factories.name_factory import ComplexFactory
from models.fng.names.name import Name


single_letter_provider = ComplexFactory.from_lists(consonants, vowel_sounds, double_consonants)
double_letter_provider = ComplexFactory.from_lists(double_consonants, double_vowel_sounds + vowel_sounds)


class BaseToponym(Name):
    providers = None

    def __init__(self, part1="", part2="", part3="", end=""):
        super().__init__("".join([
            part1,
            part2,
            part3,
            end
        ]).capitalize())

    @classmethod
    def generate(cls):
        if not cls.providers:
            return cls()
        next_data = next(cls.providers.items)
        return cls(*next_data)


class Toponym1(BaseToponym):
    providers = ComplexFactory.from_lists(single_letter_provider, endings[2])


class Toponym2(BaseToponym):
    providers = ComplexFactory.from_lists(single_letter_provider, endings[1])


class Toponym3(BaseToponym):
    providers = ComplexFactory.from_lists(double_letter_provider, endings[0])


class Toponym4(BaseToponym):
    providers = ComplexFactory.from_lists(vowel_sounds, double_consonants, endings[1])


class Toponym5(BaseToponym):
    providers = double_letter_provider.set_factory('new', ComplexFactory.from_lists(consonants, endings[2]))


class Toponym(ComplexFactory):
    generators = {
        20: Toponym1,
        40: Toponym2,
        60: Toponym3,
        80: Toponym4,
        100: Toponym5,
    }
