import random

from generator.generator.generated import Generated
from generator.generator.data_provider import FileProvider


class HaikuString(Generated):
    providers = []

    def __init__(self, first="", last=""):
        super().__init__()
        self.first = first
        self.last = last

    @classmethod
    def generate(cls):
        strings = random.choice(cls.providers)
        if strings is None:
            return cls()

        next_data = {key: next(d) for key, d in strings.items()}
        return cls(**next_data)

    def __str__(self):
        return "{} {}".format(self.first, self.last)


class Haiku(Generated):
    class HaikuString1(HaikuString):
        providers = [
            {
                'first': FileProvider("data/haiku/haiku1a.txt"),
                'last': FileProvider("data/haiku/haiku2a.txt"),
            },
            {
                'first': FileProvider("data/haiku/haiku1b.txt"),
                'last': FileProvider("data/haiku/haiku2b.txt"),
            },
            {
                'first': FileProvider("data/haiku/haiku1c.txt"),
                'last': FileProvider("data/haiku/haiku2c.txt"),
            },
            {
                'first': FileProvider("data/haiku/haiku5a.txt"),
                'last': FileProvider("data/haiku/haiku2c.txt"),
            },
            {
                'first': FileProvider("data/haiku/haiku5b.txt"),
                'last': FileProvider("data/haiku/haiku6b.txt"),
            }
        ]

    class HaikuString2(HaikuString):
        providers = [
            {
                'first': FileProvider("data/haiku/haiku3a.txt"),
                'last': FileProvider("data/haiku/haiku4a.txt"),
            },
            {
                'first': FileProvider("data/haiku/haiku3b.txt"),
                'last': FileProvider("data/haiku/haiku4b.txt"),
            },
        ]

    class HaikuString3(HaikuString):
        providers = [
            {
                'first': FileProvider("data/haiku/haiku1a.txt"),
                'last': FileProvider("data/haiku/haiku2a.txt"),
            },
            {
                'first': FileProvider("data/haiku/haiku1b.txt"),
                'last': FileProvider("data/haiku/haiku2b.txt"),
            },
            {
                'first': FileProvider("data/haiku/haiku5a.txt"),
                'last': FileProvider("data/haiku/haiku2c.txt"),
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
