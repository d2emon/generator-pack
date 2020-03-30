from factories.template import FactoryTemplate
from .factory import Factory


class TemplateFactory(Factory):
    default_template = '{c}{n}'

    def factory_template(self, template=None):
        return FactoryTemplate(template or self.template)

    def value(self):
        return next(self.factory_template())
