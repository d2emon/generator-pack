class ListDataProvider:
    default_data = ()

    def __init__(self, data=None):
        self.__data = data

    @property
    def data(self):
        if self.__data is None:
            self.__data = self.default_data
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
