import random
from . import Generated, DataGenerator, GeneratorTemplate
from .data.band import names1, names2, names3, names4, names5


class Haiku(Generated):
    def __repr__(self):
        return "Haiku:\n%s" % (self.generated_value)


class HaikuGenerator(DataGenerator):
    generated_class = Haiku
    band_names1 = [names1, names2]
    band_names2 = names5
    band_names3 = [names3, names4]

    @classmethod
    def generate1(cls):
        snt = random.randint(0, 4)
        if snt == 0:
            return GeneratorTemplate.generate([
                "data/haiku/haiku1a.txt",
                "data/haiku/haiku2a.txt",
            ])
        elif snt == 1:
            return GeneratorTemplate.generate([
                "data/haiku/haiku1b.txt",
                "data/haiku/haiku2b.txt",
            ])
        elif snt == 2:
            return GeneratorTemplate.generate([
                "data/haiku/haiku1c.txt",
                "data/haiku/haiku2c.txt",
            ])
        elif snt == 3:
            return GeneratorTemplate.generate([
                "data/haiku/haiku5a.txt",
                "data/haiku/haiku2c.txt",
            ])
        else:
            return GeneratorTemplate.generate([
                "data/haiku/haiku5b.txt",
                "data/haiku/haiku6b.txt",
            ])

    @classmethod
    def generate2(cls):
        snt = random.randint(0, 1)
        if snt == 0:
            return GeneratorTemplate.generate([
                "data/haiku/haiku3a.txt",
                "data/haiku/haiku4a.txt",
            ])
        else:
            return GeneratorTemplate.generate([
                "data/haiku/haiku3b.txt",
                "data/haiku/haiku4b.txt",
            ])

    @classmethod
    def generate3(cls):
        snt = random.randint(0, 2)
        if snt == 0:
            return GeneratorTemplate.generate([
                "data/haiku/haiku1a.txt",
                "data/haiku/haiku2a.txt",
            ])
        elif snt == 1:
            return GeneratorTemplate.generate([
                "data/haiku/haiku1b.txt",
                "data/haiku/haiku2b.txt",
            ])
        else:
            return GeneratorTemplate.generate([
                "data/haiku/haiku5a.txt",
                "data/haiku/haiku2c.txt",
            ])

    @classmethod
    def generate_value(cls):
        names = [
            cls.generate1(),
            cls.generate2(),
            cls.generate3(),
        ]
        return "\n".join(names)
