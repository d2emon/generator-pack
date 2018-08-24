from generator.generator import ListGenerator
from generator.generator.generated import Generated
from generator.generator.generator_data import FileData


class Riddle(Generated):
    title = "Riddle"


class RiddleGenerator(ListGenerator):
    generated_class = Riddle
    data = { 'name': FileData("data/riddle.txt") }
