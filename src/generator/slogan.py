from . import Generated, FileGenerator


class Slogan(Generated):
    def __repr__(self):
        return "Slogan: \"%s\"" % (self.generated_value)


class SloganGenerator(FileGenerator):
    generated_class = Slogan
    data_file = "data/slogan.txt"
