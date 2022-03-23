from .array_database import ArrayDatabase


class DatabaseLoader(ArrayDatabase):
    def __init__(self, **config):
        super().__init__()
        self.config = config

    @property
    def is_ready(self):
        return True

    def load(self):
        """
        Reload data from data file

        :return:
        """
        raise NotImplementedError()

    def save(self):
        """
        Save data for data file

        :return:
        """
        raise NotImplementedError()

    @property
    def data(self):
        """
        :return: Data from db
        """
        if not self.is_ready:
            self.load()

        return self._data
