from .array_database import ArrayDatabase


class DatabaseLoader(ArrayDatabase):
    def __init__(self, fields=None, **config):
        super().__init__()
        self.config = config
        self._data = None

        self.fields = fields or []

        self.__ready = False
        self.__source = None

    @property
    def is_ready(self):
        return self.__ready and (self._data is not None)

    @property
    def source(self):
        """
        :return: Data source
        """
        if self.__source is None:
            self.__source = self.open()

        return self.__source

    @property
    def data(self):
        """
        :return: Data from db
        """
        if not self.is_ready:
            self.load()

        return self._data

    def open(self):
        """Open data source"""
        raise NotImplementedError()

    def load(self):
        """
        Reload data from data source

        :return:
        """
        data = self.source.load()
        self._data = [self.to_record(item) for item in data]
        self.__ready = True

    def save(self):
        """
        Save data to data source

        :return:
        """
        self.source.save(self.data)
