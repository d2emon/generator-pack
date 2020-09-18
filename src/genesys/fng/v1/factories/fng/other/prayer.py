from providers import ListProvider, FactoryProvider
from factories.generator import ListGenerated, ComplexGenerated

from sample_data.fixtures.other.prayer import forgive, aid, deity

RANDOM_PRAYER = 0
FORGIVE_PRAYER = 1
AID_PRAYER = 2


class Deity(ListGenerated):
    template = "{title} {name}, {long_title}"
    providers = {
        'title': ListProvider(deity.titles),
        'name': ListProvider(deity.names),
        'long': ListProvider(deity.long),
    }

    def __init__(self, name, title="", long=""):
        super().__init__(name)
        self.name = name
        self.title = title
        self.long = long

    def __str__(self):
        return "{deity.title} {deity.name}, {deity.long}".format(deity=self)

    def pray(self, prayer_type=RANDOM_PRAYER):
        if prayer_type == RANDOM_PRAYER:
            return Prayer.generate(self)
        if prayer_type == FORGIVE_PRAYER:
            return ForgivePrayer.generate(self)
        return AidPrayer.generate(self)

    @classmethod
    def generate(cls):
        next_data = {key: next(d) for key, d in cls.providers.items()}
        return cls(**next_data)


class BasePrayer(ListGenerated):
    deity_provider = FactoryProvider(Deity)

    @classmethod
    def generate(cls, deity=None):
        deity = deity or next(cls.deity_provider)
        # prayer = super().generate()
        # prayer.deity = deity or cls.deity_provider.generate()
        next_data = {key: next(d) for key, d in cls.providers.items()}
        return cls(deity, **next_data)
        # return prayer


class ForgivePrayer(BasePrayer):
    providers = {
        'sin': ListProvider(forgive.sins),

        'forgive': ListProvider(forgive.forgives),
        'description': ListProvider(forgive.descriptions),

        'ask1': ListProvider(forgive.asks[0]),
        'promise1': ListProvider(forgive.promises[0]),

        'ask2': ListProvider(forgive.asks[1]),
        'promise2': ListProvider(forgive.promises[1]),
    }

    def __init__(self, deity, sin="", forgive="", description="", ask1="", promise1="", ask2="", promise2=""):
        super().__init__(sin)
        self.deity = deity
        self.sin = sin
        self.forgive = forgive
        self.sin_description = description
        self.ask1 = ask1
        self.promise1 = promise1
        self.ask2 = ask2
        self.promise2 = promise2

    def __str__(self):
        return ("{deity}, {prayer.sin}. {prayer.forgive}, {prayer.sin_description}. "
                "{prayer.ask1}, {prayer.promise1}. {prayer.ask2} so I {prayer.promise2}.").format(
            deity=str(self.deity),
            prayer=self
        )


class AidPrayer(BasePrayer):
    providers = {
        'ask1': ListProvider(aid.asks[0]),

        'ask2': ListProvider(aid.asks[1]),
        'may': ListProvider(aid.mays),
        'subject': ListProvider(aid.subjects),

        'ask3': ListProvider(aid.asks[2]),
        'asker': ListProvider(aid.askers),
        'title': ListProvider(aid.titles),

        'bless': ListProvider(aid.blesses),
        'bless_description': ListProvider(aid.descriptions),
        'bless_subject': ListProvider(aid.bless_subjects),
    }

    def __init__(self, deity, ask1="", ask2="", ask3="", may="", subject="", asker="", title="", bless="", bless_description="", bless_subject=""):
        super().__init__(subject)
        self.deity = deity
        self.ask1 = ask1
        self.ask2 = ask2
        self.ask3 = ask3
        self.may = may
        self.subject = subject
        self.asker = asker
        self.title = title
        self.bless = bless
        self.bless_description = bless_description
        self.bless_subject = bless_subject

    def __str__(self):
        return ("{prayer.deity}, {prayer.ask1}. {prayer.ask2} so I {prayer.may} {prayer.subject}. "
                "I {prayer.ask3} this of you {prayer.asker}, o {prayer.title}. "
                "{prayer.bless} me with your {prayer.bless_description} {prayer.bless_subject}.").format(
            deity=str(self.deity),
            prayer=self,
        )


class Prayer(ComplexGenerated):
    deity_provider = Deity

    generators = {
        50: ForgivePrayer,
        100: AidPrayer,
    }

    @classmethod
    def generate(cls, deity=None):
        prayer = super().generate()
        prayer.deity = deity or cls.deity_provider.generate()
        # next_data = {key: next(d) for key, d in cls.providers.items()}
        # return cls(deity, **next_data)
        return prayer
