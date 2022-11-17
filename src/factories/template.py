from .factory import Factory
from .list_factory import ListFactory


class LetterFactory(ListFactory):
    def __init__(self):
        super().__init__([chr(c) for c in range(ord('A'), ord('Z') + 1)])


class NumberFactory(ListFactory):
    def __init__(self):
        super().__init__([str(n) for n in range(0, 9)])


class TemplateFactory(Factory):
    """
    Generate text from template
    """

    template = '{c}{n}'

    # From provider

    @property
    def __replacers(self):
        return {
            '{c}': LetterFactory(),
            '{n}': NumberFactory(),
        }

    def __apply_replacer(self, value, pattern, replacer):
        replaced = value

        # if replacer is None:
        #     return replaced

        while pattern in replaced:
            replaced = replaced.replace(pattern, next(replacer), 1)

        return replaced

    def __text_provider(self, value):
        """
        Generate text from factory data
        :return: str
        """
        replaced = value

        for pattern, replacer in self.__replacers.items():
            replaced = self.__apply_replacer(replaced, pattern, replacer)

        return replaced

    def build_args(self, *args, **kwargs):
        """
        Apply providers for templates

        :param args: Provider args
        :param kwargs: Provider.kwargs
        :return: Text from factory data
        """
        return [
            self.__text_provider(self.template),
        ]
