import random


class Generated:
    fields = []

    generator = None

    def __init__(self, value=None, **kwargs):
        self.value = value
        for field in self.fields:
            setattr(self, field, kwargs.get(field))

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "{}:\t\"{}\"".format(type(self).__name__, str(self))

    @property
    def generated_value(self):
        return self.value

    @property
    def description(self):
        return str(self)

    @classmethod
    def generate(cls):
        return cls(cls.generator.__next__())


class ListGenerated(Generated):
    data = dict()

    @classmethod
    def generate(cls):
        next_data = {key: next(d) for key, d in cls.data.items()}
        return cls(**next_data)


class ComplexGenerated(Generated):
    generators = dict()

    @classmethod
    def generate(cls):
        chance = random.randint(0, 100)

        generator = cls.generator(chance)
        if generator is None:
            return None
        return generator.generate()

    @classmethod
    def generator(cls, chance=0):
        for c in sorted(cls.generators.keys()):
            if c >= chance:
                return cls.generators[c]
        return None
