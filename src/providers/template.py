from .provider import ProviderFactory
from .list_provider import StaticListProvider


class LetterProvider(StaticListProvider):
    static_data = [chr(c) for c in range(ord('A'), ord('Z') + 1)]


class NumberProvider(StaticListProvider):
    static_data = [str(n) for n in range(0, 9)]


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
