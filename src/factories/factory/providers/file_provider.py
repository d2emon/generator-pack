class FileDataProvider:
    default_filename = ''

    def __init__(self, filename=None):
        self.__data = None
        self.filename = filename or self.default_filename

    @property
    def _file_data(self):
        raise NotImplementedError()

    @property
    def data(self):
        if self.__data is None:
            self.__data = self._file_data
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
