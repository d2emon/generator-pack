class Model:
    fields = []
    generator = None

    def __init__(self, value=None, **kwargs):
        self.__value = value
        for field in self.fields:
            setattr(self, field, kwargs.get(field))

    @property
    def value(self):
        return self.__value

    @property
    def description(self):
        return str(self.value)

    def __str__(self):
        return self.description

    def __repr__(self):
        return "<{}:\t\"{}\">".format(type(self).__name__, str(self))

    @classmethod
    def provider(cls):
        raise NotImplementedError()

    @classmethod
    def generate(cls):
        return cls(next(cls.provider()))
