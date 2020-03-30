from models.models import Model


class Factory:
    class DataProvider:
        pass

    default_data = {}
    default_template = '{}'
    model_class = Model

    def __init__(self, provider=None):
        self.__data = None
        self.__template = None
        self.provider = provider or self.DataProvider()

    @property
    def data(self):
        if self.__data is None:
            self.__data = self.default_data
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def template(self):
        if self.__template is None:
            self.__template = self.default_template
        return self.__template

    @template.setter
    def template(self, value):
        self.__template = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.model()

    def value(self):
        return self.template.format(next(self))

    def model(self, *args, **kwargs):
        value = self.value()
        return value and self.model_class(
            value=value,
            # *args,
            **kwargs,
        )
