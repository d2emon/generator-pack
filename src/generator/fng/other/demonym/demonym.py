import random


from fixtures.other.alphabet import vowels, double_vowels
from fixtures.other.demonym import endings


BASE_SHORT = 0
BASE_VOWEL = 1
BASE_DOUBLE_VOWEL = 2
BASE_CONSONANT = 3


def base_type(word):
    if len(word) < 2:
        return BASE_SHORT
    elif word[:-2] in double_vowels:
        return BASE_DOUBLE_VOWEL
    elif word[:-1] in vowels:
        return BASE_VOWEL
    return BASE_CONSONANT


class Demonym:
    def __init__(self, toponym):
        def build_demonym(base="", endings=()):
            return base + random.choice(endings)

        def vowel_based():
            return random.choice(endings[:2])

        def double_vowel_based(toponym):
            if len(toponym) < 5:
                return toponym[:-1], random.choice(endings[0])

            endings_type = random.choice([
                endings[0],
                endings[2],
            ])
            return toponym[:-2], random.choice(endings_type)

        def consonant_based(toponym):
            chance = random.randint(0, 100)
            if chance < 40:
                base = toponym
            elif chance < 60:
                base = toponym[:-1]
            elif chance < 80:
                if len(toponym) < 5:
                    base = toponym[:-1]
                else:
                    base = toponym[:-2]
            else:
                if len(toponym) < 5:
                    base = toponym[:-1]
                else:
                    base = toponym[:-3]
            return base, endings[0]

        self.toponym = str(toponym)
        toponym_base_type = base_type(toponym)
        if toponym_base_type == BASE_DOUBLE_VOWEL:
            base, ending = double_vowel_based(self.toponym)
        elif toponym_base_type == BASE_VOWEL:
            base, ending = self.toponym[:-1], vowel_based()
        else:
            base, ending = consonant_based(self.toponym)
        self.value = base + random.choice(ending)

    def __str__(self):
        return self.value

    def __repr__(self):
        return "{} of {}".format(str(self), self.toponym)
