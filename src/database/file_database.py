import os
from .database_loader import DatabaseLoader
from .file.csv_data_file import CSVDataFile
from .file.json_data_file import JSONDataFile


class FileDatabase(DatabaseLoader):
    def __init__(self, filename='', **config):
        super().__init__(**config)

        self.__filename = filename

    @property
    def filename(self):
        """
        :return: Full filename for data file
        """
        return os.path.join(self.config.get('DATABASE_ROOT', ''), self.__filename)

    @property
    def source_factory(self):
        """
        :return: Data file
        """
        raise NotImplementedError()

    def open(self):
        """
        :return: Data file
        """
        raise self.source_factory(self.filename, self.fields)


class CSVDatabase(FileDatabase):
    source_factory = CSVDataFile


class JSONDatabase(FileDatabase):
    source_factory = JSONDataFile
