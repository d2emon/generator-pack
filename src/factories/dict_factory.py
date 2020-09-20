from .template import TemplateFactory


class DictFactory(TemplateFactory):
    """
    Generate values from dictionary with factories
    """

    def model(self, *args, **kwargs):
        """
        Get values from all factories

        :param args:
        :param kwargs:
        :return: Values from all factories
        """
        return {key: next(factory) for key, factory in self.data.items()}

    def factory(self, key):
        """
        Get item from data

        :param key: Item Key
        :return: Item from data
        """
        return self.data.get(key)
