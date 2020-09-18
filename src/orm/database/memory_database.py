from .database import Database


class MemoryDatabase(Database):
    def __init__(self, **config):
        super().__init__(**config)
        self.__data = []

    @property
    def data(self):
        return self.__data
