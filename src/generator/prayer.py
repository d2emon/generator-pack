from . import Generated, ParamGenerator, GeneratorTemplate, load_lines
import random


class Prayer(Generated):
    def __repr__(self):
        return "Prayer:\n\"%s\"" % (self.generated_text)


class AppealToDeityTemplate(GeneratorTemplate):
    template = "%s %s, %s"

    @classmethod
    def generate(cls, filenames):
        return cls.template % (
            random.choice(load_lines(filenames[0])),
            random.choice(load_lines(filenames[1])),
            random.choice(load_lines(filenames[2])),
        )


class ForgivePrayerTemplate(GeneratorTemplate):
    template = ", %s. %s, %s. %s, %s. %s so I %s."

    @classmethod
    def generate(cls, filenames):
        return cls.template % (
            random.choice(load_lines(filenames[0])),
            random.choice(load_lines(filenames[1])),
            random.choice(load_lines(filenames[2])),
            random.choice(load_lines(filenames[3])),
            random.choice(load_lines(filenames[4])),
            random.choice(load_lines(filenames[5])),
            random.choice(load_lines(filenames[6])),
        )


class AidPrayerTemplate(GeneratorTemplate):
    template = ", %s. %s so I %s %s. I %s this of you %s, o %s. %s me with your %s %s."

    @classmethod
    def generate(cls, filenames):
        return cls.template % (
            random.choice(load_lines(filenames[0])),
            random.choice(load_lines(filenames[1])),
            random.choice(load_lines(filenames[2])),
            random.choice(load_lines(filenames[3])),
            random.choice(load_lines(filenames[4])),
            random.choice(load_lines(filenames[5])),
            random.choice(load_lines(filenames[6])),
            random.choice(load_lines(filenames[7])),
            random.choice(load_lines(filenames[8])),
            random.choice(load_lines(filenames[9])),
        )


class PrayerGenerator(ParamGenerator):
    generated_class = Prayer

    @classmethod
    def forgiveness(cls):
        return ForgivePrayerTemplate.generate([
            "data/prayer/sin.txt",
            "data/prayer/forgive.txt",

            "data/prayer/sin_description.txt",
            "data/prayer/ask_sin.txt",
            "data/prayer/promise.txt",
            "data/prayer/ask_sin2.txt",
            "data/prayer/promise2.txt",
        ])

    @classmethod
    def aid(cls):
        return AidPrayerTemplate.generate([
            "data/prayer/ask.txt",
            "data/prayer/ask2.txt",

            "data/prayer/may.txt",
            "data/prayer/subject.txt",
            "data/prayer/ask3.txt",
            "data/prayer/asker.txt",
            "data/prayer/deity_title2.txt",

            "data/prayer/bless.txt",
            "data/prayer/bless_description.txt",
            "data/prayer/bless_subject.txt",
        ])

    @classmethod
    def generate_text(cls, forgive=False):
        appeal =AppealToDeityTemplate.generate([
            "data/prayer/deity_title.txt",
            "data/prayer/deity_name.txt",
            "data/prayer/deity_long_title.txt",
        ])
        if forgive:
            return appeal + cls.forgiveness()
        else:
            return appeal + cls.aid()

