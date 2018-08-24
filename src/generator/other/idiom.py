from generator.generator import ListGenerator
from generator.generator.generated import Generated
from generator.generator.generator_data import FileData


class Idiom(Generated):
    title = "Idiom"


class IdiomGenerator(ListGenerator):
    generated_class = Idiom
    data = { 'name': FileData("data/idiom.txt") }
    template = "{name}."
