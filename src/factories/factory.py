class SimpleFactory:
    def __init__(self, data=None):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.__data
