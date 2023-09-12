from utils.loaders import load_lines
from .data_file import DataFile


class TextDataFile(DataFile):
    def load(self):
        yield from load_lines(self.filename)

    def save(self, data):
        raise NotImplementedError()
