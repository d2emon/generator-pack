from .generator import DataGenerator
from .generator.template import GeneratorTemplate
from .generator.generated import Generated
from .generator.generator_data import FileData

import random


class Haiku(Generated):
    title = "Haiku"

    def __repr__(self):
        return "{}:\n{}".format(self.title, self.value)


class HaikuSubGenerator(DataGenerator):
    data_files = []

    @classmethod
    def generate(cls):
        snt = random.choice(cls.data_files)
        return GeneratorTemplate.glue(snt, glue=" ")


class HaikuSubGenerator1(HaikuSubGenerator):
    data_files = [
        [
            FileData("data/haiku/haiku1a.txt"),
            FileData("data/haiku/haiku2a.txt"),
        ],
        [
            FileData("data/haiku/haiku1b.txt"),
            FileData("data/haiku/haiku2b.txt"),
        ],
        [
            FileData("data/haiku/haiku1c.txt"),
            FileData("data/haiku/haiku2c.txt"),
        ],
        [
            FileData("data/haiku/haiku5a.txt"),
            FileData("data/haiku/haiku2c.txt"),
        ],
        [
            FileData("data/haiku/haiku5b.txt"),
            FileData("data/haiku/haiku6b.txt"),
        ]
    ]


class HaikuSubGenerator2(HaikuSubGenerator):
    data_files = [
        [
            FileData("data/haiku/haiku3a.txt"),
            FileData("data/haiku/haiku4a.txt"),
        ],
        [
            FileData("data/haiku/haiku3b.txt"),
            FileData("data/haiku/haiku4b.txt"),
        ],
    ]


class HaikuSubGenerator3(HaikuSubGenerator):
    data_files = [
        [
            FileData("data/haiku/haiku1a.txt"),
            FileData("data/haiku/haiku2a.txt"),
        ],
        [
            FileData("data/haiku/haiku1b.txt"),
            FileData("data/haiku/haiku2b.txt"),
        ],
        [
            FileData("data/haiku/haiku5a.txt"),
            FileData("data/haiku/haiku2c.txt"),
        ],
    ]


class HaikuGenerator(DataGenerator):
    generated_class = Haiku

    @classmethod
    def generate_value(cls):
        names = [
            HaikuSubGenerator1.generate(),
            HaikuSubGenerator2.generate(),
            HaikuSubGenerator3.generate(),
        ]
        return "\n".join(names)
