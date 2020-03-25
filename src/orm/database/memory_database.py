from orm.database import DataFile, Database


class MemoryDataFile(DataFile):
    __data = []

    def load(self):
        yield from self.__data

    def save(self, data):
        self.__data = list(data)


class MemoryDatabase(Database):
    data_file_class = MemoryDataFile
