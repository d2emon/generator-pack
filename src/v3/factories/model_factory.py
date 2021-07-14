from .factory import Factory


class ModelFactory(Factory):
    """
    Factory for model
   """

    @property
    def model(self):
        """
        Build model

        :return: Model, built by factory
        """
        raise NotImplementedError()

    def generate(self, *args, **kwargs):
        """
        Generate value from data

        :param args: Args for generation
        :param kwargs: Kwargs for generation
        :return: Generated value
        """
        raise NotImplementedError()

    def validate(self, items) -> dict:
        """
        Validate items

        :param items: Name items
        :return: Validated name items
        """
        return items

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
