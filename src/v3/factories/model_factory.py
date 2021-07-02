from .list_factory import ListFactory


class ModelFactory(ListFactory):
    """
    Factory for model
   """
    def __init__(self, data):
        """
        Create factory

        :param data: Array of data dicts
        """
        super().__init__(data)

    @property
    def model(self):
        """
        Build model

        :return: Model, built by factory
        """
        raise NotImplementedError()

    def __call__(self, *args, **kwargs):
        """
        Main factory method

        :param args: Model args
        :param kwargs: Fields to search in data
        :return: Model, built by factory
        """
        values = self.generate(*args, **kwargs)
        values = self.validate(values)
        return self.model(*args, **values)
