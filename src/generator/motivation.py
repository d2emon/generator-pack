from . import Generated, FileGenerator


class Motivation(Generated):
    title = "Motivation"


class MotivationGenerator(FileGenerator):
    generated_class = Motivation
    data_file = "data/motivation.txt"
    text_format = "%s."
