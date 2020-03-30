from .template import TemplateFactory


class DictFactory(TemplateFactory):
    default_template = '{name}'

    def __init__(self):
        super().__init__()
        self.__template = None

    def factory(self, key):
        return self.data.get(key)

    def value(self):
        data = {key: next(factory) for key, factory in self.data.items()}
        return self.template.format(**data)
