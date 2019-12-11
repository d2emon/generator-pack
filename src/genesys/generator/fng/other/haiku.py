import random

from genesys.generator import ListGenerated
from genesys.generator import ProvidersList, ListProvider


from fixtures.other import haiku, haiku_middle


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
            ProvidersList(*[ListProvider(part) for part in haiku[0]]),
            ProvidersList(*[ListProvider(part) for part in haiku[1]]),
            ProvidersList(*[ListProvider(part) for part in haiku[2]]),
            ProvidersList(*[ListProvider(part) for part in haiku[3]]),
            ProvidersList(*[ListProvider(part) for part in haiku[4]]),
        ]

    class HaikuString2(HaikuString):
        providers = [
            ProvidersList(*[ListProvider(part) for part in haiku_middle[0]]),
            ProvidersList(*[ListProvider(part) for part in haiku_middle[1]]),
        ]

    class HaikuString3(HaikuString):
        providers = [
            ProvidersList(*[ListProvider(part) for part in haiku[0]]),
            ProvidersList(*[ListProvider(part) for part in haiku[1]]),
            ProvidersList(*[ListProvider(part) for part in haiku[3]]),
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
