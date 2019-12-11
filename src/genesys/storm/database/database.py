import csv
import json
import os
import uuid
from ..config import CONFIG


def add_uuid(**record):
    return {
        'uuid': record.get('uuid', str(uuid.uuid4())),
        **record,
    }


class DataFile:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        raise NotImplementedError()

    def save(self, data):
        raise NotImplementedError()


class JSONDataFile(DataFile):
    def load(self):
        with open(self.filename, 'r') as f:
            yield from json.load(f)

    def save(self, data):
        with open(self.filename, 'w') as f:
            json.dump(list(data), f)


class CSVDataFile(DataFile):
    def load(self):
        with open(self.filename, 'r') as f:
            yield from list(csv.reader(f))

    def save(self, data):
        with open(self.filename, 'w') as f:
            writer = csv.writer(f)
            for record in data:
                writer.writerow(record)


class Database:
    data_file_class = None

    def __init__(self, **config):
        self.config = {
            **CONFIG,
            **config,
        }
        self._data = None

    @property
    def filename(self):
        filename = self.config.get('filename')
        return os.path.join(self.config['DATABASE_ROOT'], filename) if filename else None

    @property
    def data_file(self):
        return self.data_file_class(self.filename)

    @property
    def data(self):
        if self._data is None:
            self.load()
        self._data = [add_uuid(**record) for record in self._data]
        return self._data

    def load(self):
        self._data = list(self.data_file.load())
        return self._data

    def save(self):
        self.data_file.save(self.data)

    def update(self, fields):
        item_id = fields.get('uuid')
        if item_id is None:
            self._data.append(fields)
            return

        for item in filter(lambda i: i.get('uuid') == item_id, self.data):
            item.update(fields)


class JSONDatabase(Database):
    data_file_class = JSONDataFile


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
