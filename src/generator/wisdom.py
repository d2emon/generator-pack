from . import Generated, FileGenerator


class WisdomQuote(Generated):
    def __repr__(self):
        return "Wisdom quote:\n\"%s\"" % (self.generated_value)


class WisdomQuoteGenerator(FileGenerator):
    generated_class = WisdomQuote
    data_file = "data/wisdom.txt"
