from .list_factory import ListFactory


class FileData:
    def __init__(self, filename):
        self.filename = filename


class FileFactory(ListFactory):
    class DataProvider(ListFactory.DataProvider):
        filename = ''

        @property
        def data(self):
            if self.__data is None:
                self.__data = FileData(self.filename)
            return self.__data

        @data.setter
        def data(self, value):
            self.__data = value
