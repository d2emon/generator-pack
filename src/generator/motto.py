from .generator import ListGenerator
from .generator.generated import Generated
from .generator.generator_data import FileData


class Motto(Generated):
    title = "Motto"


class MottoGenerator(ListGenerator):
    generated_class = Motto
    data = { 'name': FileData("data/motto.txt") }
    template = "{name}."
