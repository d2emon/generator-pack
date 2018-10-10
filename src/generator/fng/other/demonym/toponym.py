from generator.generator.generated import Generated, ComplexGenerated
from generator.generator.data_provider import FileProvider


class BaseToponym(Generated):
    def __init__(self, part1="", part2="", part3="", end=""):
        super().__init__("".join([
            part1,
            part2,
            part3,
            end
        ]).capitalize())

    @classmethod
    def generate(cls):
        next_data = next(cls.providers.items)
        return cls(*next_data)


class Toponym1(BaseToponym):
    providers = FileProvider("data/demonym/demonym1.txt") \
        + FileProvider("data/demonym/demonym2.txt") \
        + FileProvider("data/demonym/demonym3.txt") \
        + FileProvider("data/demonym/endings.txt")


class Toponym2(BaseToponym):
    providers = FileProvider("data/demonym/demonym1.txt") \
        + FileProvider("data/demonym/demonym2.txt") \
        + FileProvider("data/demonym/demonym3.txt") \
        + FileProvider("data/demonym/demonym6.txt")


class Toponym3(BaseToponym):
    providers = FileProvider("data/demonym/demonym3.txt") \
        + FileProvider("data/demonym/demonym4.txt") \
        + FileProvider("data/demonym/demonym5.txt")


class Toponym4(BaseToponym):
    providers = FileProvider("data/demonym/demonym2.txt") \
        + FileProvider("data/demonym/demonym3.txt") \
        + FileProvider("data/demonym/demonym6.txt")


class Toponym5(BaseToponym):
    providers = FileProvider("data/demonym/demonym3.txt") \
        + FileProvider("data/demonym/demonym4.txt") \
        + FileProvider("data/demonym/demonym1.txt") \
        + FileProvider("data/demonym/endings.txt")


class Toponym(ComplexGenerated):
    generators = {
        20: Toponym1,
        40: Toponym2,
        60: Toponym3,
        80: Toponym4,
        100: Toponym5,
    }
