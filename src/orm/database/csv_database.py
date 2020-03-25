import csv
from orm.database import DataFile, Database


class CSVDataFile(DataFile):
    def load(self):
        with open(self.filename, 'r') as f:
            yield from list(csv.reader(f))

    def save(self, data):
        with open(self.filename, 'w') as f:
            writer = csv.writer(f)
            for record in data:
                writer.writerow(record)


class CSVDatabase(Database):
    data_file_class = CSVDataFile

    def __init__(self, **config):
        super().__init__(**config)
        self.fields = config.get('fields', [])

    def load(self):
        self._data = [
            {
                name: row[field_id]
                for field_id, name in enumerate(self.fields)
            }
            for row in self.data_file.load()
        ]
