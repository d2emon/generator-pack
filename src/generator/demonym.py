import random
from . import Generated, DataGenerator, GeneratorTemplate, load_lines


vowels = ["a", "e", "i", "o", "u", "y"]
double_vowels = [
    "aa", "ae", "ai", "ao", "ae",
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

class DemonymBase(Generated):
    def __init__(self):
        Generated.__init__(self)
        self.__demonym = None

    @property
    def base(self):
        return self.generated_text

    @property
    def demonym(self):
        if self.__demonym:
            return self.__demonym

        c_ran = random.choice(c_ending_no_splice)
        ran = random.choice(ending_no_splice)
        s_ran = random.choice(ending_splice)

        chance = random.randint(0, 100)
        word_base = self.base
        word_end = ""
        if word_base[-1] in vowels:
            word_base = word_base[:-1]
            if chance < 50:
                word_end = s_ran
            else:
                word_end = ran
        elif word_base[-2:] in double_vowels:
            if len(word_base) < 5:
                word_base = word_base[:-1]
                word_end = s_ran
            else:
                word_base = word_base[:-2]
                demonym = toponym[:-2]
                if chance < 50:
                    word_end = s_ran
                else:
                    word_end = c_ran
        else:
            word_end = s_ran
            if chance < 40:
                word_base = word_base
            elif chance < 60:
                word_base = word_base[:-1]
            elif chance < 80:
                if len(word_base) < 5:
                    word_base = word_base[:-1]
                else:
                    word_base = word_base[:-2]
            else:
                if len(word_base) < 5:
                    word_base = word_base[:-1]
                else:
                    word_base = word_base[:-3]
        self.__demonym = "%s%s" % (word_base, word_end)
        return self.__demonym

    def __repr__(self):
        return "Demonym: \"%s(%s)\"" % (self.demonym, self.base)


def makeDemonym(base):
    db = DemonymBase()
    db.generated_text = base
    return db


class DemonymTemplate(GeneratorTemplate):
    @classmethod
    def generate(cls, filenames):
        parts = [random.choice(load_lines(f)) for f in filenames]
        return "".join(parts)


class DemonymGenerator(DataGenerator):
    generated_class = DemonymBase

    @classmethod
    def generate1(cls):
        return DemonymTemplate.generate([
            "data/demonym/demonym1.txt",
            "data/demonym/demonym2.txt",
            "data/demonym/demonym3.txt",
            "data/demonym/endings.txt",
        ]).capitalize()

    @classmethod
    def generate2(cls):
        return DemonymTemplate.generate([
            "data/demonym/demonym1.txt",
            "data/demonym/demonym2.txt",
            "data/demonym/demonym3.txt",
            "data/demonym/demonym6.txt",
        ]).capitalize()

    @classmethod
    def generate3(cls):
        return DemonymTemplate.generate([
            "data/demonym/demonym3.txt",
            "data/demonym/demonym4.txt",
            "data/demonym/demonym5.txt",
        ]).capitalize()

    @classmethod
    def generate4(cls):
        return DemonymTemplate.generate([
            "data/demonym/demonym2.txt",
            "data/demonym/demonym3.txt",
            "data/demonym/demonym6.txt",
        ]).capitalize()

    @classmethod
    def generate5(cls):
        return DemonymTemplate.generate([
            "data/demonym/demonym3.txt",
            "data/demonym/demonym4.txt",
            "data/demonym/demonym1.txt",
            "data/demonym/endings.txt",
        ]).capitalize()

    @classmethod
    def generate_text(cls):
        chance = random.randint(0, 100)
        if chance < 20:
            return cls.generate1()
        elif chance < 40:
            return cls.generate2()
        elif chance < 60:
            return cls.generate3()
        elif chance < 80:
            return cls.generate4()
        else:
            return cls.generate5()
