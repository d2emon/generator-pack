from providers.template import LetterProvider, NumberProvider
from .provider import DataProvider


class TemplateDataProvider(DataProvider):
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
