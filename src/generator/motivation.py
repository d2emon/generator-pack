from .generator import ListGenerator
from .generator.generated import Generated
from .generator.generator_data import FileData


class Motivation(Generated):
    title = "Motivation"


class MotivationGenerator(ListGenerator):
    generated_class = Motivation
    data = { 'name': FileData("data/motivation.txt") }
    template = "{name}."
