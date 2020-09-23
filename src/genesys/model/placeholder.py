class Placeholder:
    def __init__(self, builder):
        self.builder = builder
        self.__model = None

    def build(self, **kwargs):
        self.__model = self.builder.build(**kwargs)
        return self.__model

    @property
    def model(self):
        if self.__model is None:
            self.build()
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def placeholder(self):
        return self
