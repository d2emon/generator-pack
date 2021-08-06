import json
from .file_database import DataFile, FileDatabase


class JSONDataFile(DataFile):
    def load(self):
        with open(self.filename, 'r') as f:
            yield from json.load(f)

    def save(self, data):
        with open(self.filename, 'w') as f:
            json.dump(list(data), f)


class JSONDatabase(FileDatabase):
    def open(self):
        """
        :return: Data file
        """
        return JSONDataFile(self.filename)
