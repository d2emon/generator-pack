from generator.generator.generated import ListGenerated, ComplexGenerated
from generator.generator.generator_data import StaticData, FileData


FORGIVE_PRAYER = "forgive"
AID_PRAYER = "aid"


class Deity(ListGenerated):
    template = "{title} {name}, {long_title}"
    data = {
        'title': FileData("data/prayer/deity_title.txt"),
        'name': FileData("data/prayer/deity_name.txt"),
        'long': FileData("data/prayer/deity_long_title.txt"),
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


class BasePrayer(ListGenerated):
    @classmethod
    def generate(cls, deity=None):
        prayer = super().generate()
        prayer.deity = deity or prayer.deity.generate()
        return prayer


class ForgivePrayer(BasePrayer):
    data = {
        'deity': StaticData(Deity),
        'sin': FileData("data/prayer/sin.txt"),

        'forgive': FileData("data/prayer/forgive.txt"),
        'description': FileData("data/prayer/sin_description.txt"),

        'ask1': FileData("data/prayer/ask_sin.txt"),
        'promise1': FileData("data/prayer/promise.txt"),

        'ask2': FileData("data/prayer/ask_sin2.txt"),
        'promise2': FileData("data/prayer/promise2.txt"),
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
    data = {
        'deity': StaticData(Deity),
        'ask1': FileData("data/prayer/ask.txt"),

        'ask2': FileData("data/prayer/ask2.txt"),
        'may': FileData("data/prayer/may.txt"),
        'subject': FileData("data/prayer/subject.txt"),

        'ask3': FileData("data/prayer/ask3.txt"),
        'asker': FileData("data/prayer/asker.txt"),
        'title': FileData("data/prayer/deity_title2.txt"),

        'bless': FileData("data/prayer/bless.txt"),
        'bless_description': FileData("data/prayer/bless_description.txt"),
        'bless_subject': FileData("data/prayer/bless_subject.txt"),
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
    generators = {
        50: ForgivePrayer,
        100: AidPrayer,
    }
