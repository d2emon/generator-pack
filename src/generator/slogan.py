from . import Generated, FileGenerator


class Slogan(Generated):
    title = "Slogan"


class SloganGenerator(FileGenerator):
    generated_class = Slogan
    data_file = "data/slogan.txt"
