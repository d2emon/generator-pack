import random


from fixtures.other.alphabet import vowels, double_vowels
from fixtures.other.demonym import endings


BASE_SHORT = 0
BASE_VOWEL = 1
BASE_DOUBLE_VOWEL = 2
BASE_DOUBLE_VOWEL_SHORT = 3
BASE_CONSONANT = 4


def consonant_base(word):
    chance = random.randint(0, 100)
    if chance < 40:
        return word
    if chance < 60:
        return word[:-1]
    if len(word) < 5:
        return word[:-1]
    if chance < 80:
        return word[:-2]
    return word[:-3]


BASE_SPLIT = {
    BASE_VOWEL: lambda word: word[:-1],
    BASE_DOUBLE_VOWEL_SHORT: lambda word: word[:-1],
    BASE_DOUBLE_VOWEL: lambda word: word[:-2],
    BASE_CONSONANT: consonant_base,
}
BASE_ENDINGS = {
    BASE_VOWEL: endings[0] + endings[1],
    BASE_DOUBLE_VOWEL_SHORT: endings[0],
    BASE_DOUBLE_VOWEL: endings[0] + endings[2],
    BASE_CONSONANT: endings[0]
}


def base_type(word):
    if len(word) < 2:
        return BASE_SHORT
    elif word[:-2] in double_vowels:
        if len(word) < 5:
            return BASE_DOUBLE_VOWEL_SHORT
        return BASE_DOUBLE_VOWEL
    elif word[:-1] in vowels:
        return BASE_VOWEL
    return BASE_CONSONANT


def word_base(word):
    word_base_type = base_type(word)

    base_split = BASE_SPLIT.get(word_base_type)
    endings = BASE_ENDINGS.get(word_base_type, [])

    if base_split is None:
        return BASE_SPLIT(word), endings
    return word, endings


class Demonym:
    def __init__(self, toponym):
        self.toponym = str(toponym)
        base, ending = word_base(self.toponym)
        self.value = base + random.choice(ending)

    def __str__(self):
        return self.value

    def __repr__(self):
        return "{} of {}".format(str(self), self.toponym)
