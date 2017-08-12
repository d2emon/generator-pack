from . import Generated, FileGenerator


class Swear(Generated):
    def __repr__(self):
        return "Swear: \"%s\"" % (self.generated_text)


class SwearGenerator(FileGenerator):
    generated_class = Swear
    data_file = "data/swear.txt"
