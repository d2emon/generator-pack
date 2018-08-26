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


class Demonym:
    def __init__(self, toponym):
        def build_demonym(base="", endings=()):
            return base + random.choice(endings)

        def vowel_based(toponym):
            return build_demonym(toponym[:-1], random.choice([
                ending_splice,
                ending_no_splice,
            ]))

        def double_vowel_based(toponym):
            if len(toponym) < 5:
                return build_demonym(toponym[:-1], ending_splice)
            return build_demonym(toponym[:-2], random.choice([
                ending_splice,
                c_ending_no_splice,
            ]))

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
            return build_demonym(base, ending_splice)

        self.toponym = str(toponym)
        if self.toponym[-2:] in double_vowels:
            self.value = double_vowel_based(self.toponym)
        elif self.toponym[-1:] in vowels:
            self.value = vowel_based(self.toponym)
        else:
            self.value = consonant_based(self.toponym)

    def __str__(self):
        return self.value

    def __repr__(self):
        return "{} of {}".format(str(self), self.toponym)
