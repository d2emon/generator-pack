import csv
from config import DB_CONFIG
from .file_database import DataFile, FileDatabase


class CSVDataFile(DataFile):
    def __init__(self, filename, fields=None):
        super().__init__(filename)
        self.fields = fields

    def __prepare(self, record):
        """
        Inject uuid to record

        :param record: Record
        :return: Injected record
        """
        return {field: record[field_id] for field_id, field in enumerate(self.fields)}

    def load(self):
        with open(self.filename, 'r') as f:
            yield from map(self.__prepare, csv.reader(f))

    def save(self, data):
        with open(self.filename, 'w') as f:
            writer = csv.writer(f)
            for record in data:
                writer.writerow(record)


class CSVDatabase(FileDatabase):
    def __init__(self, filename='', fields=None, **config):
        super().__init__(filename, **config)
        self.fields = fields or []

    @property
    def data_file(self):
        return CSVDataFile(self.filename, self.fields)
