import random
from .. import Generated, DataGenerator, GeneratorTemplate


class Galaxy(Generated):
    def __repr__(self):
        return "Galaxy: \"%s\"" % (self.generated_text)


class GalaxyTemplate(GeneratorTemplate):
    @classmethod
    def generate1(cls):
        return cls.generate([
            "data/galaxy/galaxy1.txt",
            "data/galaxy/galaxy2.txt",
        ])

    @classmethod
    def generate2(cls):
        return cls.generate([
            "data/galaxy/galaxy2.txt",
            "data/galaxy/galaxy-type.txt",
        ])

    @classmethod
    def generate3(cls):
        return cls.generate([
            "data/galaxy/galaxy3.txt",
            "data/galaxy/galaxy-type.txt",
        ])

    @classmethod
    def generate4(cls):
        return cls.pregenerate("{c}{c}-{n}{n}")

    @classmethod
    def generate5(cls):
        return cls.pregenerate("{c}{c}{c} {n}{n}{c}")


class GalaxyGenerator(DataGenerator):
    generated_class = Galaxy

    @classmethod
    def generate4(cls):
        return GalaxyTemplate.generate4()

    @classmethod
    def generate5(cls):
        return GalaxyTemplate.generate5()

    @classmethod
    def generate_text(cls):
        methods = {
            30: GalaxyTemplate.generate1,
            50: GalaxyTemplate.generate2,
            80: GalaxyTemplate.generate3,
            90: GalaxyTemplate.generate4,
            100: GalaxyTemplate.generate5,
        }
        chance = random.randint(0, 100)
        for c in sorted(methods):
            if c >= chance:
                return methods[c]()
