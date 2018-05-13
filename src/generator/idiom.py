from .generator import FileGenerator
from .generator.generated import Generated


class Idiom(Generated):
    title = "Idiom"


class IdiomGenerator(FileGenerator):
    generated_class = Idiom
    data_file = "data/idiom.txt"
    text_format = "%s."
