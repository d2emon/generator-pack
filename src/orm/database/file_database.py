import os
from .memory_database import MemoryDatabase


class DataFile:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        """
        Load data from file

        :return: records
        """
        raise NotImplementedError()

    def save(self, data):
        """
        Save data to file

        :param data: records
        :return:
        """
        raise NotImplementedError()


class FileDatabase(MemoryDatabase):
    def __init__(self, filename='', **config):
        super().__init__(**config)
        self.__filename = filename
        self.__data = None
        self.__loaded = False

    @property
    def is_loaded(self):
        return self.__loaded and (self.__data is not None)

    @property
    def filename(self):
        """
        :return: Full filename for data file
        """
        return os.path.join(self.config.get('DATABASE_ROOT'), self.__filename)

    @property
    def data_file(self):
        """
        :return: Data file
        """
        raise NotImplementedError()

    @property
    def data(self):
        """
        :return: Data from db
        """
        if not self.is_loaded:
            self.load()

        return self.__data

    def load(self):
        """
        Reload data from data file

        :return:
        """
        self.__data = list(map(self.prepare, self.data_file.load()))
        self.__loaded = True

    def save(self):
        """
        Save data for data file

        :return:
        """
        self.data_file.save(self.data)
