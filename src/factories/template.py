from .factory import Factory


class TemplateFactory(Factory):
    def __init__(self, provider=None):
        super().__init__(provider)
        self.template = '{c}{n}'
        self.__text = None

    @property
    def model(self, *args, **kwargs):
        """
        Apply providers for templates

        :param args: Provider args
        :param kwargs: Provider.kwargs
        :return: Text from factory data
        """
        return self.provider.text(self.template)

    @classmethod
    def glue(cls, parts, glue=""):
        """
        Glue parts into one text

        :param parts: Text parts
        :param glue: Glue
        :return: Glued text
        """
        return glue.join(next(i) for i in parts)
