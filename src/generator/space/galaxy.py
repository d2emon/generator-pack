import random
from .. import Generated, DataGenerator, GeneratorTemplate


class Galaxy(Generated):
    def __repr__(self):
        return "Galaxy: \"%s\"" % (self.generated_text)


class GalaxyTemplate(GeneratorTemplate):
    letters = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
    numbers = range(0, 9)

    @classmethod
    def generate4(cls):
        return "%s%s-%d%d" % (
            random.choice(cls.letters),
            random.choice(cls.letters),
            random.choice(cls.numbers),
            random.choice(cls.numbers),
        )

    @classmethod
    def generate5(cls):
        return "%s%s%s %d%d%s" % (
            random.choice(cls.letters),
            random.choice(cls.letters),
            random.choice(cls.letters),
            random.choice(cls.numbers),
            random.choice(cls.numbers),
            random.choice(cls.letters),
        )


class GalaxyGenerator(DataGenerator):
    generated_class = Galaxy

    @classmethod
    def generate1(cls):
        return GalaxyTemplate.generate([
            "data/galaxy/galaxy1.txt",
            "data/galaxy/galaxy2.txt",
        ])

    @classmethod
    def generate2(cls):
        return GalaxyTemplate.generate([
            "data/galaxy/galaxy2.txt",
            "data/galaxy/galaxy-type.txt",
        ])

    @classmethod
    def generate3(cls):
        return GalaxyTemplate.generate([
            "data/galaxy/galaxy3.txt",
            "data/galaxy/galaxy-type.txt",
        ])

    @classmethod
    def generate4(cls):
        return GalaxyTemplate.generate4()

    @classmethod
    def generate5(cls):
        return GalaxyTemplate.generate5()

    @classmethod
    def generate_text(cls):
        methods = {
            30: cls.generate1,
            50: cls.generate2,
            80: cls.generate3,
            90: cls.generate4,
            100: cls.generate5,
        }
        chance = random.randint(0, 100)
        for c in sorted(methods):
            if c >= chance:
                return methods[c]()
