from generator.generator.generated import ListGenerated, ComplexGenerated
from generator.generator.data_provider import GeneratorProvider, FileProvider


FORGIVE_PRAYER = "forgive"
AID_PRAYER = "aid"


class Deity(ListGenerated):
    template = "{title} {name}, {long_title}"
    providers = {
        'title': FileProvider("data/prayer/deity_title.txt"),
        'name': FileProvider("data/prayer/deity_name.txt"),
        'long': FileProvider("data/prayer/deity_long_title.txt"),
    }

    def __init__(self, name, title="", long=""):
        super().__init__(name)
        self.name = name
        self.title = title
        self.long = long

    def __str__(self):
        return "{deity.title} {deity.name}, {deity.long}".format(deity=self)

    def pray(self, prayer_type=FORGIVE_PRAYER):
        if prayer_type == FORGIVE_PRAYER:
            return ForgivePrayer.generate(self)
        return AidPrayer.generate(self)

    @classmethod
    def generate(cls):
        next_data = {key: next(d) for key, d in cls.providers.items()}
        return cls(**next_data)


class BasePrayer(ListGenerated):
    @classmethod
    def generate(cls, deity=None):
        prayer = super().generate()
        prayer.deity = deity or prayer.deity.generate()
        return prayer


class ForgivePrayer(BasePrayer):
    providers = {
        'deity': GeneratorProvider(Deity),
        'sin': FileProvider("data/prayer/sin.txt"),

        'forgive': FileProvider("data/prayer/forgive.txt"),
        'description': FileProvider("data/prayer/sin_description.txt"),

        'ask1': FileProvider("data/prayer/ask_sin.txt"),
        'promise1': FileProvider("data/prayer/promise.txt"),

        'ask2': FileProvider("data/prayer/ask_sin2.txt"),
        'promise2': FileProvider("data/prayer/promise2.txt"),
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

    @classmethod
    def generate(cls):
        next_data = {key: next(d) for key, d in cls.providers.items()}
        return cls(**next_data)


class AidPrayer(BasePrayer):
    providers = {
        'deity': GeneratorProvider(Deity),
        'ask1': FileProvider("data/prayer/ask.txt"),

        'ask2': FileProvider("data/prayer/ask2.txt"),
        'may': FileProvider("data/prayer/may.txt"),
        'subject': FileProvider("data/prayer/subject.txt"),

        'ask3': FileProvider("data/prayer/ask3.txt"),
        'asker': FileProvider("data/prayer/asker.txt"),
        'title': FileProvider("data/prayer/deity_title2.txt"),

        'bless': FileProvider("data/prayer/bless.txt"),
        'bless_description': FileProvider("data/prayer/bless_description.txt"),
        'bless_subject': FileProvider("data/prayer/bless_subject.txt"),
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

    @classmethod
    def generate(cls):
        next_data = {key: next(d) for key, d in cls.providers.items()}
        return cls(**next_data)


class Prayer(ComplexGenerated):
    generators = {
        50: ForgivePrayer,
        100: AidPrayer,
    }
