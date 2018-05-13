from . import Generated, FileGenerator


class Motto(Generated):
    title = "Motto"


class MottoGenerator(FileGenerator):
    generated_class = Motto
    data_file = "data/motto.txt"
    text_format = "%s."
