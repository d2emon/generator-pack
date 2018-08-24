from generator.generator import ListGenerator
from generator.generator.generated import Generated
from generator.generator.generator_data import FileData


class Slogan(Generated):
    title = "Slogan"


class SloganGenerator(ListGenerator):
    generated_class = Slogan
    data = { 'name': FileData("data/slogan.txt") }