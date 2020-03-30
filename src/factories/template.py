from providers.template import LetterProvider, NumberProvider
from factories.factory import Factory


class TemplateFactory(Factory):
    class DataProvider:
        @property
        def replacers(self):
            return {
                '{c}': LetterProvider(),
                '{n}': NumberProvider(),
            }

    default_template = '{c}{n}'

    def __init__(self, provider=None):
        super().__init__(provider)
        self.__text = None

    def value(self):
        template = self.template
        replacers = self.provider.replacers
        for k, v in replacers.items():
            while k in template:
                template = template.replace(k, next(v), 1)
        return template

    def strip(self):
        return self.value().strip()

    @classmethod
    def glue(cls, parts, glue=""):
        return glue.join(next(i) for i in parts).capitalize()
