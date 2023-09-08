from factories.list_factory import ListFactory
from utils.loaders import load_lines


class TextFileLoader(ListFactory):
    @classmethod
    def from_text_file(cls, filename):
        data = list(load_lines(filename))
        return cls(data)
