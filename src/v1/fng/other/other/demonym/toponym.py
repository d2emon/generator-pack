from providers import ListProvider
from factories.generator import Generated, ComplexGenerated

from genesys.fixtures.fixtures import vowel_sounds, consonants, double_vowel_sounds, double_consonants
from genesys.fixtures.fixtures import endings


single_letter_provider = ListProvider(consonants) + ListProvider(vowel_sounds) + ListProvider(double_consonants)
double_letter_provider = ListProvider(double_consonants) + ListProvider(double_vowel_sounds + vowel_sounds)


class BaseToponym(Generated):
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
    providers = single_letter_provider + ListProvider(endings[2])


class Toponym2(BaseToponym):
    providers = single_letter_provider + ListProvider(endings[1])


class Toponym3(BaseToponym):
    providers = double_letter_provider + ListProvider(endings[0])


class Toponym4(BaseToponym):
    providers = ListProvider(vowel_sounds) + ListProvider(double_consonants) + ListProvider(endings[1])


class Toponym5(BaseToponym):
    providers = double_letter_provider + ListProvider(consonants) + ListProvider(endings[2])


class Toponym(ComplexGenerated):
    generators = {
        20: Toponym1,
        40: Toponym2,
        60: Toponym3,
        80: Toponym4,
        100: Toponym5,
    }
