import os
from utils.loaders import load_lines
from .list_provider import ListDataProvider


class FileDataProvider(ListDataProvider):
    default_filename = ''

    def __init__(self, filename=None):
        super().__init__()
        self.__data = None
        self.filename = filename or self.default_filename

    def __next__(self):
        raise NotImplementedError()

    @property
    def __file_path(self):
        return os.path.abspath(os.path.join("", self.filename))

    @property
    def __file_data(self):
        return load_lines(self.__file_path)

    @property
    def data(self):
        if self.__data is None:
            self.__data = self.__file_data
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
