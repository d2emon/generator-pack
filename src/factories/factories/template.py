from factories.template import FactoryTemplate
from .factory import Factory


class TemplateFactory(Factory):
    class DataProvider(Factory.DataProvider):
        template = '{c}{n}'

        def __next__(self):
            return next(FactoryTemplate(self.template))
