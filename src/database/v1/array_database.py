import random
import uuid
from database.base_database import BaseDatabase


class ArrayDatabase(BaseDatabase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._data = None

    def insert(self, fields):
        """
        Save data for data file

        :return:
        """
        self._data.append(fields)

    def find_and_update(self, item_id, fields):
        """
        Save data for data file

        :return:
        """
        for item in filter(lambda i: i.get('uuid') == item_id, self._data):
            item.update(fields)

    def insert_or_update(self, fields):
        """
        Update record by uuid or create new record

        :param fields: Fields to update
        :return:
        """
        item_id = fields.get('uuid')
        return self.find_and_update(item_id, fields) if item_id is not None else self.insert(fields)

    # For models

    def find(self, query=lambda item: True):
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
        return next(self.find(query), None)

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
