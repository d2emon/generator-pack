import random
from . import Generated, DataGenerator
from .data.band import names1, names2, names3, names4, names5


class Band(Generated):
    def __repr__(self):
        return "Band: \"%s\"" % (self.generated_value)


class BandGenerator(DataGenerator):
    generated_class = Band
    band_names1 = [names1, names2]
    band_names2 = names5
    band_names3 = [names3, names4]

    @classmethod
    def generate1(cls):
        return "%s %s" % (
            random.choice(cls.band_names1[0]),
            random.choice(cls.band_names1[1]),
        )

    @classmethod
    def generate2(cls):
        return random.choice(cls.band_names2)

    @classmethod
    def generate3(cls):
        return "%s of %s" % (
            random.choice(cls.band_names3[0]),
            random.choice(cls.band_names3[1]),
        )

    @classmethod
    def generate_value(cls):
        chance = random.randint(0, 100)
        if chance < 30:
            return cls.generate1()
        elif chance < 70:
            return cls.generate2()
        else:
            return cls.generate3()
