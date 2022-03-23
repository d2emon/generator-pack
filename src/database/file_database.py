import os
from .database_loader import DatabaseLoader


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


class FileDatabase(DatabaseLoader):
    def __init__(self, filename='', **config):
        super().__init__(**config)

        self.__filename = filename
        self.__loaded = False
        self.__file = None

    @property
    def is_ready(self):
        return self.__loaded and (self._data is not None)

    @property
    def filename(self):
        """
        :return: Full filename for data file
        """
        return os.path.join(self.config.get('DATABASE_ROOT', ''), self.__filename)

    @property
    def file(self):
        """
        :return: Data file
        """
        if self.__file is None:
            self.__file = self.open()

        return self.__file

    def open(self):
        """
        :return: Data file
        """
        raise NotImplementedError()

    def load(self):
        """
        Reload data from data file

        :return:
        """
        self._data = list(map(self.output, self.file.load()))
        self.__loaded = True

    def save(self):
        """
        Save data for data file

        :return:
        """
        self.file.save(self.data)
