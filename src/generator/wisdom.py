from .generator import FileGenerator
from .generator.generated import Generated


class WisdomQuote(Generated):
    title = "Wisdom quote"

    def __repr__(self):
        return "{}:\n\"{}\"".format(self.title, self.value)


class WisdomQuoteGenerator(FileGenerator):
    generated_class = WisdomQuote
    data_file = "data/wisdom.txt"
