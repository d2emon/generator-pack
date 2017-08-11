import random
from . import Generated, DataGenerator
from .data.battlecry import names


class BattleCry(Generated):
    def __repr__(self):
        return "BattleCry: \"%s\"" % (self.generated_text)


class BattleCryGenerator(DataGenerator):
    generated_class = BattleCry
    cries = names

    @classmethod
    def generate_text(cls):
        return random.choice(cls.cries) + "!"
