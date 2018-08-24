from generator.generator import ListGenerator
from generator.generator.generated import Generated
from generator.generator.generator_data import FileData


class Swear(Generated):
    title = "Swear"


class SwearGenerator(ListGenerator):
    generated_class = Swear
    data = { 'name': FileData("data/swear.txt") }
