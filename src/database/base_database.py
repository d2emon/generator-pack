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

    def find_and_update(self, item_id, fields):
        """
        Save data for data file

        :return:
        """
        raise NotImplementedError()

    def save_or_update(self, fields):
        """
        Update record by uuid or create new record

        :param fields: Fields to update
        :return:
        """
        raise NotImplementedError()

    # For models

    def find(self, query=lambda item: True):
        """
        Get all data from db

        :param query: Db query
        :return: Filtered data
        """
        raise NotImplementedError()

    def first(self, query=lambda item: True):
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
