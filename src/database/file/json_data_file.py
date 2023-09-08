import json
from .data_file import DataFile


class JSONDataFile(DataFile):
    def load(self):
        with open(self.filename, 'r') as f:
            yield from json.load(f)

    def save(self, data):
        with open(self.filename, 'w') as f:
            json.dump(list(data), f)
