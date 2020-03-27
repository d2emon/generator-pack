import json
from orm.database import DataFile, Database


class JSONDataFile(DataFile):
    def load(self):
        with open(self.filename, 'r') as f:
            yield from json.load(f)

    def save(self, data):
        with open(self.filename, 'w') as f:
            json.dump(list(data), f)


class JSONDatabase(Database):
    data_file_class = JSONDataFile
