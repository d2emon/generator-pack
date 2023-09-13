from factories.model_factory import ModelFactory


class DataFactory(ModelFactory):
    default_data = []

    def __init__(self, data=None):
        """
        Create factory

        :param data: Array of data dicts
        """
        self.factory_data = self.factory(data or self.default_data)

    @classmethod
    def factory(cls, data):
        """
        Build model

        :return: Model, built by factory
        """
        raise NotImplementedError()

    def data_factory(self, *args, **kwargs):
        return self.factory_data.get_random(*args, **kwargs)
