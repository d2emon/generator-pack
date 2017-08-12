from . import Generated, FileGenerator


class Riddle(Generated):
    def __repr__(self):
        return "Riddle: \"%s\"" % (self.generated_text)


class RiddleGenerator(FileGenerator):
    generated_class = Riddle
    data_file = "data/riddle.txt"
