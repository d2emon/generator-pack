from . import Generated, FileGenerator


class Riddle(Generated):
    title = "Riddle"


class RiddleGenerator(FileGenerator):
    generated_class = Riddle
    data_file = "data/riddle.txt"
