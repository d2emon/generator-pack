from . import Generated, FileGenerator


class Swear(Generated):
    title = "Swear"


class SwearGenerator(FileGenerator):
    generated_class = Swear
    data_file = "data/swear.txt"
