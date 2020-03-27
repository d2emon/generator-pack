from .factory import Factory


class ListFactory(Factory):
    class DataProvider(Factory.DataProvider):
        template = '{name}'
        default = {}

        def __init__(self):
            self.__data = None

        @property
        def data(self):
            if self.__data is None:
                self.__data = self.default
            return self.__data

        @data.setter
        def data(self, value):
            self.__data = value

        def __next__(self):
            next_data = {key: next(factory) for key, factory in self.data.items()}
            return self.template.format(**next_data)
