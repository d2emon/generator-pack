from factories.list_factory import ListFactory
from .provider import ProviderFactory


class LetterProvider(ListFactory):
    def __init__(self):
        super().__init__([chr(c) for c in range(ord('A'), ord('Z') + 1)])


class NumberProvider(ListFactory):
    def __init__(self):
        super().__init__([str(n) for n in range(0, 9)])


class TemplateDataProvider(ProviderFactory):
    def __call__(self):
        return self.text('')

    @property
    def replacers(self):
        return {
            '{c}': LetterProvider(),
            '{n}': NumberProvider(),
        }

    def apply_replacer(self, pattern, value):
        replaced = value
        replacer = self.replacers.get(pattern)

        if replacer is None:
            return replaced

        while pattern in replaced:
            replaced = replaced.replace(pattern, next(replacer), 1)

    def text(self, value):
        """
        Generate text from factory data
        :return: str
        """
        replaced = value
        for pattern in self.replacers.keys():
            replaced = self.apply_replacer(pattern, replaced)
        return replaced
