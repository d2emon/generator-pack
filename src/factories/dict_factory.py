from .model import ModelFactory


class DictFactory(ModelFactory):
    """
    Generate values from dictionary with factories
    """

    @property
    def data(self):
        raise NotImplementedError()

    @property
    def model_class(self):
        return None

    def __len__(self):
        """
        :return: Data length
        """
        return len(self.data)

    def factory(self, key):
        """
        Get item from data

        :param key: Item Key
        :return: Item from data
        """
        return self.data.get(key)

    def build(self, *args, **kwargs):
        """
        Get values from all factories

        :param args:
        :param kwargs:
        :return: Values from all factories
        """
        data = {key: next(factory) for key, factory in self.data.items()}
        return self.model_class(*args, **data, **kwargs) if self.model_class is not None else data
