import os
import uuid
from config.storm import CONFIG


class DataFile:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        raise NotImplementedError()

    def save(self, data):
        raise NotImplementedError()


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
        self._data = [self.__inject_uuid(**record) for record in self._data]
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

    @classmethod
    def __inject_uuid(cls, **record):
        return {
            'uuid': record.get('uuid', str(uuid.uuid4())),
            **record,
        }
