from .generator import DataGenerator, PercentedGenerator
from .generator.generated import Generated
from .generator.template import GeneratorTemplate
from .generator.generator_data import FileData


class Deity(Generated):
    title = "Deity"


class Prayer(Generated):
    title = "Prayer"

    def __repr__(self):
        return "{}:\n\"{}\"".format(self.title, self.value)


class AppealToDeityTemplate(DataGenerator):
    generated_class = Deity
    template = "%s %s, %s"
    data_files = [
        FileData("data/prayer/deity_title.txt"),
        FileData("data/prayer/deity_name.txt"),
        FileData("data/prayer/deity_long_title.txt"),
    ]

    @classmethod
    def __next__(cls):
        return cls.template % (
            cls.data_files[0].__next__(),
            cls.data_files[1].__next__(),
            cls.data_files[2].__next__(),
        )


class BasePrayerGenerator(DataGenerator):
    generated_class = Prayer


class ForgivePrayerGenerator(BasePrayerGenerator):
    template = "%s, %s. %s, %s. %s, %s. %s so I %s."
    data_files = [
        FileData("data/prayer/sin.txt"),

        FileData("data/prayer/forgive.txt"),
        FileData("data/prayer/sin_description.txt"),

        FileData("data/prayer/ask_sin.txt"),
        FileData("data/prayer/promise.txt"),

        FileData("data/prayer/ask_sin2.txt"),
        FileData("data/prayer/promise2.txt"),
    ]

    @classmethod
    def __next__(cls, *args, **kwargs):
        deity = AppealToDeityTemplate.generate()
        return cls.template % (
            deity.value,
            cls.data_files[0].__next__(),
            cls.data_files[1].__next__(),
            cls.data_files[2].__next__(),
            cls.data_files[3].__next__(),
            cls.data_files[4].__next__(),
            cls.data_files[5].__next__(),
            cls.data_files[6].__next__(),
        )


class AidPrayerGenerator(BasePrayerGenerator):
    template = "%s, %s. %s so I %s %s. I %s this of you %s, o %s. %s me with your %s %s."
    data_files = [
        FileData("data/prayer/ask.txt"),

        FileData("data/prayer/ask2.txt"),
        FileData("data/prayer/may.txt"),
        FileData("data/prayer/subject.txt"),

        FileData("data/prayer/ask3.txt"),
        FileData("data/prayer/asker.txt"),
        FileData("data/prayer/deity_title2.txt"),

        FileData("data/prayer/bless.txt"),
        FileData("data/prayer/bless_description.txt"),
        FileData("data/prayer/bless_subject.txt"),
    ]

    @classmethod
    def __next__(cls, *args, **kwargs):
        deity = AppealToDeityTemplate.generate()
        return cls.template % (
            deity.value,
            cls.data_files[0].__next__(),
            cls.data_files[1].__next__(),
            cls.data_files[2].__next__(),
            cls.data_files[3].__next__(),
            cls.data_files[4].__next__(),
            cls.data_files[5].__next__(),
            cls.data_files[6].__next__(),
            cls.data_files[7].__next__(),
            cls.data_files[8].__next__(),
            cls.data_files[9].__next__(),
        )


class PrayerGenerator(PercentedGenerator):
    subgenerators = {
        50: ForgivePrayerGenerator,
        100: AidPrayerGenerator,
    }
