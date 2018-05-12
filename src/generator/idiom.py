from . import Generated, FileGenerator


class Idiom(Generated):
    def __repr__(self):
        return "Idiom: \"%s\"" % (self.generated_value)


class IdiomGenerator(FileGenerator):
    generated_class = Idiom
    data_file = "data/idiom.txt"
    text_format = "%s."
