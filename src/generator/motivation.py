from . import Generated, FileGenerator


class Motivation(Generated):
    def __repr__(self):
        return "Motivation: \"%s\"" % (self.generated_value)


class MotivationGenerator(FileGenerator):
    generated_class = Motivation
    data_file = "data/motivation.txt"
    text_format = "%s."
