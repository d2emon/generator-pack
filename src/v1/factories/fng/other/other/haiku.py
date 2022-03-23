import random
from providers.list_provider import ListProvider
from factories.generator import ListGenerated
from genesys.fixtures.fixtures import haiku_middle
from genesys.fixtures.fixtures.other.haiku import haiku


class HaikuString(ListGenerated):
    providers = []

    @classmethod
    def generate(cls):
        provider = random.choice(cls.providers)
        if provider is None:
            return cls()

        next_data = next(provider.items)
        return cls(next_data)


class Haiku(ListGenerated):
    class HaikuString1(HaikuString):
        providers = [
            ListProvider.multiple(haiku[0]),
            ListProvider.multiple(haiku[1]),
            ListProvider.multiple(haiku[2]),
            ListProvider.multiple(haiku[3]),
            ListProvider.multiple(haiku[4]),
        ]

    class HaikuString2(HaikuString):
        providers = [
            ListProvider.multiple(haiku_middle[0]),
            ListProvider.multiple(haiku_middle[1]),
        ]

    class HaikuString3(HaikuString):
        providers = [
            ListProvider.multiple(haiku[0]),
            ListProvider.multiple(haiku[1]),
            ListProvider.multiple(haiku[3]),
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
