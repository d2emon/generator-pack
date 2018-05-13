from . import Generated, FileGenerator


class Idiom(Generated):
    title = "Idiom"


class IdiomGenerator(FileGenerator):
    generated_class = Idiom
    data_file = "data/idiom.txt"
    text_format = "%s."
