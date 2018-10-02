import random

from generator.generator.generated import Generated
from generator.generator.generator_data import FileData


class HaikuString(Generated):
    data = []

    def __init__(self, first="", last=""):
        super().__init__()
        self.first = first
        self.last = last

    @classmethod
    def generate(cls):
        strings = random.choice(cls.data)
        if strings is None:
            return cls()

        next_data = {key: next(d) for key, d in strings.items()}
        return cls(**next_data)

    def __str__(self):
        return "{} {}".format(self.first, self.last)


class Haiku(Generated):
    class HaikuString1(HaikuString):
        data = [
            {
                'first': FileData("data/haiku/haiku1a.txt"),
                'last': FileData("data/haiku/haiku2a.txt"),
            },
            {
                'first': FileData("data/haiku/haiku1b.txt"),
                'last': FileData("data/haiku/haiku2b.txt"),
            },
            {
                'first': FileData("data/haiku/haiku1c.txt"),
                'last': FileData("data/haiku/haiku2c.txt"),
            },
            {
                'first': FileData("data/haiku/haiku5a.txt"),
                'last': FileData("data/haiku/haiku2c.txt"),
            },
            {
                'first': FileData("data/haiku/haiku5b.txt"),
                'last': FileData("data/haiku/haiku6b.txt"),
            }
        ]

    class HaikuString2(HaikuString):
        data = [
            {
                'first': FileData("data/haiku/haiku3a.txt"),
                'last': FileData("data/haiku/haiku4a.txt"),
            },
            {
                'first': FileData("data/haiku/haiku3b.txt"),
                'last': FileData("data/haiku/haiku4b.txt"),
            },
        ]

    class HaikuString3(HaikuString):
        data = [
            {
                'first': FileData("data/haiku/haiku1a.txt"),
                'last': FileData("data/haiku/haiku2a.txt"),
            },
            {
                'first': FileData("data/haiku/haiku1b.txt"),
                'last': FileData("data/haiku/haiku2b.txt"),
            },
            {
                'first': FileData("data/haiku/haiku5a.txt"),
                'last': FileData("data/haiku/haiku2c.txt"),
            },
        ]

    strings = [
        HaikuString1,
        HaikuString2,
        HaikuString3,
    ]

    def __init__(self, *args):
        super().__init__()
        self.text = args[:3]

    @classmethod
    def string_generator(cls):
        for s in cls.strings:
            yield s.generate()
        raise StopIteration

    @classmethod
    def generate(cls):
        strings = cls.string_generator()
        return cls(*strings)

    def __str__(self):
        return "\n".join([str(s) for s in self.text])

    def __repr__(self):
        return "{}:\n{}".format(type(self).__name__, str(self))
