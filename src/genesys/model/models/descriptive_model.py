class DescriptiveModel:
    fields = []

    class Factory:
        def __init__(self, provider):
            self.provider = provider

        def __call__(self, *args, **kwargs):
            return next(self.provider())

    def __init__(self, value=None, **kwargs):
        self.__value = value
        self.values = {field: kwargs.get(field) for field in self.fields}

    @property
    def value(self):
        return self.__value

    @property
    def description(self):
        return str(self.value)

    @description.setter
    def description(self, value):
        self.__value = value

    def __str__(self):
        return self.description

    def __repr__(self):
        return "<{}:\t\"{}\">".format(self.__class__.__name__, str(self))

    @classmethod
    def factory(cls):
        return cls.Factory(None)

    @classmethod
    def build(cls, *args, **kwargs):
        factory = cls.factory()

        if factory is None:
            return None

        params = factory(*args, **kwargs)
        return cls(**params)
