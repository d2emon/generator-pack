from uuid import uuid4
from .array_database import ArrayDatabase
from .data_item import DataItem


class DataItemDatabase(ArrayDatabase):
    def __init__(self, *data):
        super().__init__()

        self._data = [self.output(value) for value in data]

    @property
    def data(self):
        """
        :return: Data from db
        """
        return self._data

    def find(self, query):
        return (
            item
            for item in self.data
            if query(item.get("value"))
        )

    # Helpers

    @classmethod
    def output(cls, record):
        """
        Prepare loaded record

        :param record: Record
        :return: Prepared record
        """
        return {
            "uuid": uuid4(),
            "value": record,
        }

    # New methods

    def values(self):
        return [ item.get("value") for item in self.data ]

    @classmethod
    def add_to_group(cls, group_id, values):
        DataItem.add_values(group_id, values)

    @classmethod
    def get_from_group(cls, group_id):
        return DataItem.values_by_group_id(group_id)
