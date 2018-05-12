from . import Generated, FileGenerator


class Motto(Generated):
    def __repr__(self):
        return "Motto: \"%s\"" % (self.generated_value)


class MottoGenerator(FileGenerator):
    generated_class = Motto
    data_file = "data/motto.txt"
    text_format = "%s."
