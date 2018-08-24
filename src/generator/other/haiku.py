from generator.generator import Generator, ListGenerator
from generator.generator.template import GeneratorTemplate
from generator.generator.generated import Generated
from generator.generator.generator_data import FileData

import random


class Haiku(Generated):
    title = "Haiku"

    def __repr__(self):
        return "{}:\n{}".format(self.title, "\n".join(self.value))


class HaikuSubGenerator(Generator):
    template = "{part1} {part2}"

    @classmethod
    def generate(cls):
        snt = random.choice(cls.data)
        next_data = {key: next(d) for key, d in snt.items()}
        return cls.template.format(**next_data)


class HaikuGenerator(Generator):
    generated_class = Haiku
    class HaikuSubGenerator1(HaikuSubGenerator):
        data = [
            {
                'part1': FileData("data/haiku/haiku1a.txt"),
                'part2': FileData("data/haiku/haiku2a.txt"),
            },
            {
                'part1': FileData("data/haiku/haiku1b.txt"),
                'part2': FileData("data/haiku/haiku2b.txt"),
            },
            {
                'part1': FileData("data/haiku/haiku1c.txt"),
                'part2': FileData("data/haiku/haiku2c.txt"),
            },
            {
                'part1': FileData("data/haiku/haiku5a.txt"),
                'part2': FileData("data/haiku/haiku2c.txt"),
            },
            {
                'part1': FileData("data/haiku/haiku5b.txt"),
                'part2': FileData("data/haiku/haiku6b.txt"),
            }
        ]


    class HaikuSubGenerator2(HaikuSubGenerator):
        data = [
            {
                'part1': FileData("data/haiku/haiku3a.txt"),
                'part2': FileData("data/haiku/haiku4a.txt"),
            },
            {
                'part1': FileData("data/haiku/haiku3b.txt"),
                'part2': FileData("data/haiku/haiku4b.txt"),
            },
        ]


    class HaikuSubGenerator3(HaikuSubGenerator):
        data = [
            {
                'part1': FileData("data/haiku/haiku1a.txt"),
                'part2': FileData("data/haiku/haiku2a.txt"),
            },
            {
                'part1': FileData("data/haiku/haiku1b.txt"),
                'part2': FileData("data/haiku/haiku2b.txt"),
            },
            {
                'part1': FileData("data/haiku/haiku5a.txt"),
                'part2': FileData("data/haiku/haiku2c.txt"),
            },
        ]

    strings = [
        HaikuSubGenerator1,
        HaikuSubGenerator2,
        HaikuSubGenerator3,
    ]

    @classmethod
    def __next__(cls):
        return [s.generate() for s in cls.strings]

    @classmethod
    def fill_generated(cls, generated, *args, **kwargs):
        # generated.value = cls.generate_value()
        generated.value = cls.__next__()
        return generated
