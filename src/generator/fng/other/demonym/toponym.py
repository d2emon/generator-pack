from generator.generator.generated import ListGenerated, ComplexGenerated
from generator.generator.generator_data import FileData


class BaseToponym(ListGenerated):
    def __init__(self, part1="", part2="", part3="", end=""):
        super().__init__("".join([
            part1,
            part2,
            part3,
            end
        ]).capitalize())


class Toponym1(BaseToponym):
    data = {
        'part1': FileData("data/demonym/demonym1.txt"),
        'part2': FileData("data/demonym/demonym2.txt"),
        'part3': FileData("data/demonym/demonym3.txt"),
        'end': FileData("data/demonym/endings.txt"),
    }


class Toponym2(BaseToponym):
    data = {
        'part1': FileData("data/demonym/demonym1.txt"),
        'part2': FileData("data/demonym/demonym2.txt"),
        'part3': FileData("data/demonym/demonym3.txt"),
        'end': FileData("data/demonym/demonym6.txt"),
    }


class Toponym3(BaseToponym):
    data = {
        'part1': FileData("data/demonym/demonym3.txt"),
        'part2': FileData("data/demonym/demonym4.txt"),
        'part3': FileData("data/demonym/demonym5.txt"),
    }


class Toponym4(BaseToponym):
    data = {
        'part1': FileData("data/demonym/demonym2.txt"),
        'part2': FileData("data/demonym/demonym3.txt"),
        'part3': FileData("data/demonym/demonym6.txt"),
    }


class Toponym5(BaseToponym):
    data = {
        'part1': FileData("data/demonym/demonym3.txt"),
        'part2': FileData("data/demonym/demonym4.txt"),
        'part3': FileData("data/demonym/demonym1.txt"),
        'end': FileData("data/demonym/endings.txt"),
    }


class Toponym(ComplexGenerated):
    generators = {
        20: Toponym1,
        40: Toponym2,
        60: Toponym3,
        80: Toponym4,
        100: Toponym5,
    }
