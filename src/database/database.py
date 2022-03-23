import uuid


class BaseDatabase:
    @property
    def data(self):
        """
        :return: Data from db
        """
        raise NotImplementedError()

    def insert(self, fields):
        """
        Save data for data file

        :return:
        """
        raise NotImplementedError()

    def replace(self, item_id, fields):
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
        item_id = self.get_item_id(fields)
        return self.replace(item_id, fields) if item_id is not None else self.insert(fields)

    def find(self, query):
        """
        Get all data from db

        :param query: Db query
        :return: Filtered data
        """
        raise NotImplementedError()

    def all(self):
        return self.find(lambda item: True)

    def first(self, query):
        """
        Get first data from db

        :param query: Db query
        :return: Data
        """
        raise NotImplementedError()

    def get(self, item_id):
        """
        Get item by uuid

        :param item_id: uuid
        :return: Data
        """
        raise NotImplementedError()

    def random(self):
        """
        Get random data from db

        :return: Data
        """
        raise NotImplementedError()

    # Helpers

    @classmethod
    def get_item_id(cls, item):
        return item.get('uuid')

    @classmethod
    def to_record(cls, data):
        """
        Prepare loaded record

        :param record: Record
        :return: Prepared record
        """
        return {
            'uuid': data.get('uuid', str(uuid.uuid4())),
            **data,
        }
