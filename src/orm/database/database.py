import random
import uuid


class Database:
    def __init__(self, **config):
        self.config = config

    @property
    def data(self):
        """
        :return: Data from db
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

    def prepare(self, record):
        """
        Prepare loaded record

        :param record: Record
        :return: Prepared record
        """
        return {
            'uuid': record.get('uuid', str(uuid.uuid4())),
            **record,
        }

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
        record = random.choice(records) if len(records) > 0 else None
