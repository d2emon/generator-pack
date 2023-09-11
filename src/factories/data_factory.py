from .model_factory import ModelFactory


class DataFactory(ModelFactory):
    default_data = []

    def __init__(self, data=None):
        """
        Create factory

        :param data: Array of data dicts
        """
        self.factory_data = self.data_factory(data or self.default_data)

    @classmethod
    def data_factory(cls, data):
        """
        Build model

        :return: Model, built by factory
        """
        raise NotImplementedError()

    def get_data(self, *args, **kwargs):
        return self.factory_data.get_random(*args, **kwargs)
