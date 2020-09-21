from .factory import Factory


class TemplateFactory(Factory):
    """
    Generate text from template
    """

    def __init__(self, provider):
        super().__init__()
        self.template = '{c}{n}'
        self.__data = provider
        self.__text = None

    @property
    def data(self):
        return self.__data

    @classmethod
    def glue(cls, parts, glue=""):
        """
        Glue parts into one text

        :param parts: Text parts
        :param glue: Glue
        :return: Glued text
        """
        return glue.join(next(i) for i in parts)

    @property
    def build(self, *args, **kwargs):
        """
        Apply providers for templates

        :param args: Provider args
        :param kwargs: Provider.kwargs
        :return: Text from factory data
        """
        return self.data.text(self.template)
