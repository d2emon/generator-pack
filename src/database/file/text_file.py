from utils.loaders import load_lines
from .data_file import DataFile


class TextDataFile(DataFile):
    def load(self):
        for value in load_lines(self.filename):
            yield {
                "value": value,
            }

    def save(self, data):
        raise NotImplementedError()
