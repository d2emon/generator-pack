class Placeholder:
    def __init__(self, model_class, builder, **params):
        self.model_class = model_class
        self.builder = builder()
        self.__model = None
        self.params = params

    def __build(self):
        self.__model = self.model_class(
            **self.builder.build(),
            **self.params,
        )
        return self.__model

    @property
    def model(self):
        return self.__model or self.__build()

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def placeholder(self):
        return self
