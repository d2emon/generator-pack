from .generator import FileGenerator
from .generator.generated import Generated


class Motto(Generated):
    title = "Motto"


class MottoGenerator(FileGenerator):
    generated_class = Motto
    data_file = "data/motto.txt"
    text_format = "%s."
