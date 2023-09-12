from .factory import Factory


class DictFactory(Factory):
    """
    Generate random value from list
    """

    default_data = {}

    def __call__(self, *args, **kwargs):
        """
        Select random item

        :param args: Roll args
        :param kwargs: Roll kwargs
        :return: Random item
        """
        return {
            **self.data,
            **kwargs,
        }
