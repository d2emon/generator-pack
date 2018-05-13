from .generator import DataGenerator, PercentedGenerator
from .generator.template import GeneratorTemplate
from .generator.generated import Generated

from utils import load_lines

import random


vowels = ["a", "e", "i", "o", "u", "y"]
double_vowels = [
    "aa", "ae", "ai", "ao", "au",
    "ea", "ee", "ei", "eo", "eu",
    "ia", "ie", "ii", "io", "iu",
    "oa", "oe", "oi", "oo", "ou",
    "ua", "ue", "ui", "uo", "uu",
]
ending_splice =[
    "an", "ian", "anian", "in", "ine", "ite", "er", "eno", "ino", "ish",
    "ene", "ensian", "ard", "ese", "i", "ic", "iot", "iote", "asque", "onian"
]
ending_no_splice =[
    "nan", "nian", "nin", "no", "ne", "nsian", "lese", "vese", "nese", "gian",
    "vian", "lian"
]
c_ending_no_splice =[
    "n", "an", "an", "anian", "nian", "in", "ine", "ite", "er", "eno", "ino",
    "ish", "ene", "ensian", "ard", "ese", "lese", "vese", "nese", "i", "ic",
    "ot", "ote", "asque", "gian", "onian", "vian"
]


class Demonym():
    title = "Demonym"

    def __init__(self, base):
        def vowelBased(base):
            return base[:-1], random.choice([
                ending_splice,
                ending_no_splice,
            ])

        def doubleVowelBased(base):
            if len(base) < 5:
                word_base = base[:-1]
                word_ends = ending_splice
            else:
                word_base = base[:-2]
                word_ends = random.choice([
                    ending_splice,
                    c_ending_no_splice,
                ])
            return word_base, word_ends

        def consonantBased(base):
            chance = random.randint(0, 100)
            if chance < 40:
                word_base = base
            elif chance < 60:
                word_base = base[:-1]
            elif chance < 80:
                if len(base) < 5:
                    word_base = base[:-1]
                else:
                    word_base = base[:-2]
            else:
                if len(base) < 5:
                    word_base = base[:-1]
                else:
                    word_base = base[:-3]
            return word_base, ending_splice

        self.base = base
        word_base = ""
        word_ends = []
        if self.base[-2:] in double_vowels:
            word_base, word_ends = doubleVowelBased(self.base)
        elif self.base[-1:] in vowels:
            word_base, word_ends = vowelBased(self.base)
        else:
            word_base, word_ends = consonantBased(self.base)
        self.value = "{}{}".format(word_base, random.choice(word_ends))

    def __repr__(self):
        return self.value


class DemonymBase(Generated):
    title = "Demonym Base"

    def __init__(self, value=''):
        Generated.__init__(self)
        self.value = value
        self.__demonym = None

    @property
    def demonym(self):
        if self.__demonym:
            return self.__demonym

        self.__demonym = Demonym(self.value)
        return self.__demonym

    def __repr__(self):
        return "{}:\t\"{} of {}\"".format(self.title, self.demonym, self.value)


class DemonymTemplate(GeneratorTemplate):
    @classmethod
    def generate(cls, filenames):
        parts = [random.choice(load_lines(f)) for f in filenames]
        return "".join(parts)


class DemonymBaseSubGenerator(DataGenerator):
    generated_class = DemonymBase
    data_files = []

    @classmethod
    def generate_value(cls):
        return DemonymTemplate.generate(cls.data_files).capitalize()


class DemonymBaseSubGenerator1(DemonymBaseSubGenerator):
    data_files = [
        "data/demonym/demonym1.txt",
        "data/demonym/demonym2.txt",
        "data/demonym/demonym3.txt",
        "data/demonym/endings.txt",
    ]


class DemonymBaseSubGenerator2(DemonymBaseSubGenerator):
    data_files = [
        "data/demonym/demonym1.txt",
        "data/demonym/demonym2.txt",
        "data/demonym/demonym3.txt",
        "data/demonym/demonym6.txt",
    ]


class DemonymBaseSubGenerator3(DemonymBaseSubGenerator):
    data_files = [
        "data/demonym/demonym3.txt",
        "data/demonym/demonym4.txt",
        "data/demonym/demonym5.txt",
    ]


class DemonymBaseSubGenerator4(DemonymBaseSubGenerator):
    data_files = [
        "data/demonym/demonym2.txt",
        "data/demonym/demonym3.txt",
        "data/demonym/demonym6.txt",
    ]


class DemonymBaseSubGenerator5(DemonymBaseSubGenerator):
    data_files = [
        "data/demonym/demonym3.txt",
        "data/demonym/demonym4.txt",
        "data/demonym/demonym1.txt",
        "data/demonym/endings.txt",
    ]


class DemonymGenerator(PercentedGenerator):
    subgenerators = {
        20: DemonymBaseSubGenerator1,
        40: DemonymBaseSubGenerator2,
        60: DemonymBaseSubGenerator3,
        80: DemonymBaseSubGenerator4,
        100: DemonymBaseSubGenerator5,
    }
