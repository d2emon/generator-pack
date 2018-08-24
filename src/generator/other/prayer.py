from generator.generator import ListGenerator, PercentedGenerator
from generator.generator.generated import Generated
from generator.generator.template import GeneratorTemplate
from generator.generator.generator_data import StaticData, FileData


class Deity(Generated):
    title = "Deity"


class Prayer(Generated):
    title = "Prayer"

    def __repr__(self):
        return "{}:\n\"{}\"".format(self.title, self.value)


class AppealToDeityTemplate(ListGenerator):
    generated_class = Deity
    template = "{title} {name}, {long_title}"
    data = {
        'title': FileData("data/prayer/deity_title.txt"),
        'name': FileData("data/prayer/deity_name.txt"),
        'long_title': FileData("data/prayer/deity_long_title.txt"),
    }


class BasePrayerGenerator(ListGenerator):
    generated_class = Prayer


class ForgivePrayerGenerator(BasePrayerGenerator):
    template = "{deity}, {sin}. {forgive}, {description}. {ask1}, {promise1}. {ask2} so I {promise2}."
    data = {
        'deity': StaticData(AppealToDeityTemplate),
        'sin': FileData("data/prayer/sin.txt"),

        'forgive': FileData("data/prayer/forgive.txt"),
        'description': FileData("data/prayer/sin_description.txt"),

        'ask1': FileData("data/prayer/ask_sin.txt"),
        'promise1': FileData("data/prayer/promise.txt"),

        'ask2': FileData("data/prayer/ask_sin2.txt"),
        'promise2': FileData("data/prayer/promise2.txt"),
    }


class AidPrayerGenerator(BasePrayerGenerator):
    template = "{deity}, {ask1}. {ask2} so I {may} {subject}. I {ask3} this of you {asker}, o {title}. {bless} me with your {bless_description} {bless_subject}."
    data = {
        'deity': StaticData(AppealToDeityTemplate),
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


class PrayerGenerator(PercentedGenerator):
    subgenerators = {
        50: ForgivePrayerGenerator,
        100: AidPrayerGenerator,
    }
