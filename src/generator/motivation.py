from . import Generated, ListGenerator
from .data.motivation import names


class Motivation(Generated):
    def __repr__(self):
        return "Motivation: \"%s\"" % (self.generated_text)


class MotivationGenerator(ListGenerator):
    generated_class = Motivation
    data_list = names
    text_format = "%s."
