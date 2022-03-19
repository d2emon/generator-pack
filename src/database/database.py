import random
import uuid


class Database:
    def __init__(self, **config):
        self.config = config
        self._data = None

    @property
    def is_ready(self):
        return True

    @property
    def data(self):
        """
        :return: Data from db
        """
        if not self.is_ready:
            self.load()

        return self._data

    def load(self):
        """
        Reload data from data file

        :return:
        """
        raise NotImplementedError()

    def save(self):
        """
        Save data for data file

        :return:
        """
        raise NotImplementedError()

    def update(self, fields):
        """
        Update record by uuid or create new record

        :param fields: Fields to update
        :return:
        """
        item_id = fields.get('uuid')
        if item_id is None:
            self.data.append(fields)
            return

        for item in filter(lambda i: i.get('uuid') == item_id, self.data):
            item.update(fields)

    # For models
    def all(self, query=lambda item: True):
        """
        Get all data from db

        :param query: Db query
        :return: Filtered data
        """
        return filter(query, self.data)

    def first(self, query=lambda item: True):
        """
        Get first data from db

        :param query: Db query
        :return: Data
        """
        return next(self.all(query), None)

    def get(self, item_id):
        """
        Get item by uuid

        :param item_id: uuid
        :return: Data
        """
        return self.first(lambda item: item.get('uuid') == item_id)

    def random(self):
        """
        Get random data from db

        :return: Data
        """
        records = list(self.all())
        return random.choice(records) if len(records) > 0 else None

    # Transform data

    @classmethod
    def output(cls, record):
        """
        Prepare loaded record

        :param record: Record
        :return: Prepared record
        """
        return {
            'uuid': record.get('uuid', str(uuid.uuid4())),
            **record,
        }
