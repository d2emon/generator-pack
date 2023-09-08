class DataFile:
    def __init__(self, filename, fields=None):
        self.filename = filename
        self.fields = fields

    def load(self):
        """
        Load data from file

        :return: records
        """
        raise NotImplementedError()

    def save(self, data):
        """
        Save data to file

        :param data: records
        :return:
        """
        raise NotImplementedError()
