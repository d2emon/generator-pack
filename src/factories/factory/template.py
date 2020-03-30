from factories.template import FactoryTemplate
from .factory import Factory


class TemplateFactory(Factory):
    default_template = '{c}{n}'

    def __init__(self):
        super().__init__()
        self.__template = None

    @property
    def template(self):
        if self.__template is None:
            self.__template = self.default_template
        return self.__template

    @template.setter
    def template(self, value):
        self.__template = value

    def factory_template(self, template=None):
        return FactoryTemplate(template or self.template)

    def value(self):
        return next(self.factory_template())
