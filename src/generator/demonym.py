from .generator import ListGenerator, PercentedGenerator
from .generator.generated import Generated
from .generator.generator_data import FileData

from utils.loaders import load_lines

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
        return "{} of {}".format(self.value, self.base)


class DemonymBase(Generated):
    title = "Demonym Base"

    def __init__(self, value=''):
        Generated.__init__(self)
        self.value = value

    @property
    def demonym(self):
        return self.__demonym

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value.capitalize()
        self.__demonym = Demonym(self.__value)

    def __repr__(self):
        return "{}:\t\"{}, {}\"".format(self.title, self.value, self.demonym)


class DemonymBaseSubGenerator(ListGenerator):
    generated_class = DemonymBase


class DemonymGenerator(PercentedGenerator):
    class DemonymBaseSubGenerator1(DemonymBaseSubGenerator):
        template = "{demonym1}{demonym2}{demonym3}{end}"
        data = {
            'demonym1': FileData("data/demonym/demonym1.txt"),
            'demonym2': FileData("data/demonym/demonym2.txt"),
            'demonym3': FileData("data/demonym/demonym3.txt"),
            'end': FileData("data/demonym/endings.txt"),
        }


    class DemonymBaseSubGenerator2(DemonymBaseSubGenerator):
        template = "{demonym1}{demonym2}{demonym3}{end}"
        data = {
            'demonym1': FileData("data/demonym/demonym1.txt"),
            'demonym2': FileData("data/demonym/demonym2.txt"),
            'demonym3': FileData("data/demonym/demonym3.txt"),
            'end': FileData("data/demonym/demonym6.txt"),
        }


    class DemonymBaseSubGenerator3(DemonymBaseSubGenerator):
        template = "{demonym1}{demonym2}{demonym3}"
        data = {
            'demonym1': FileData("data/demonym/demonym3.txt"),
            'demonym2': FileData("data/demonym/demonym4.txt"),
            'demonym3': FileData("data/demonym/demonym5.txt"),
        }


    class DemonymBaseSubGenerator4(DemonymBaseSubGenerator):
        template = "{demonym1}{demonym2}{demonym3}"
        data = {
            'demonym1': FileData("data/demonym/demonym2.txt"),
            'demonym2': FileData("data/demonym/demonym3.txt"),
            'demonym3': FileData("data/demonym/demonym6.txt"),
        }


    class DemonymBaseSubGenerator5(DemonymBaseSubGenerator):
        template = "{demonym1}{demonym2}{demonym3}{end}"
        data = {
            'demonym1': FileData("data/demonym/demonym3.txt"),
            'demonym2': FileData("data/demonym/demonym4.txt"),
            'demonym3': FileData("data/demonym/demonym1.txt"),
            'end': FileData("data/demonym/endings.txt"),
        }
    subgenerators = {
        20: DemonymBaseSubGenerator1,
        40: DemonymBaseSubGenerator2,
        60: DemonymBaseSubGenerator3,
        80: DemonymBaseSubGenerator4,
        100: DemonymBaseSubGenerator5,
    }
