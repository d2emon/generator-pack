from os import path
from utils.loaders import load_lines


class FileDataProvider:
    default_filename = ''

    def __init__(self, filename=None):
        self.__data = None
        self.filename = filename or self.default_filename

    @property
    def __file_path(self):
        return path.abspath(path.join("", self.filename))

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
