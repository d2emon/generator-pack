from .factory import Factory


class DictFactory(Factory):
    """
    Generate values from dictionary with factories
    """
    def __init__(self, **factories):
        self.__factories = factories

    @property
    def factories(self):
        return self.__factories

    def __len__(self):
        """
        :return: Data length
        """
        return len(self.factories)

    def factory(self, key):
        """
        Get item from data

        :param key: Item Key
        :return: Item from data
        """
        return self.factories.get(key)

    def __call__(self, *args, **kwargs):
        """
        Get values from all factories

        :param args:
        :param kwargs:
        :return: Values from all factories
        """
        data = {key: factory(*args, **kwargs) for key, factory in self.factories.items()}
        data.update(**kwargs)
        return data
