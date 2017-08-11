import random
from . import Generated, DataGenerator
from .data.motivation import names


class Motivation(Generated):
    def __repr__(self):
        return "Motivation: \"%s\"" % (self.generated_text)


class MotivationGenerator(DataGenerator):
    generated_class = Motivation
    motivations = names

    @classmethod
    def generate_text(cls):
        return random.choice(cls.motivations) + "."
