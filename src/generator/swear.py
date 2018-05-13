from .generator import FileGenerator
from .generator.generated import Generated


class Swear(Generated):
    title = "Swear"


class SwearGenerator(FileGenerator):
    generated_class = Swear
    data_file = "data/swear.txt"
