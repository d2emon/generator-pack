from generator.generator import ListGenerator
from generator.generator.generated import Generated
from generator.generator.generator_data import FileData


class WisdomQuote(Generated):
    title = "Wisdom quote"

    def __repr__(self):
        return "{}:\n\"{}\"".format(self.title, self.value)


class WisdomQuoteGenerator(ListGenerator):
    generated_class = WisdomQuote
    data = { 'name': FileData("data/motivation.txt") }
