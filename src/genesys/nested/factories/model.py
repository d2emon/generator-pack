from genesys.nested.factories.v2.thing_builder import ThingBuilder


class ModelBuilder:
    class Factory(ThingBuilder):
        def __init__(self, model, **kwargs):
            super().__init__()
            self.model = model
            self.params = kwargs

        def build_params(self, **kwargs):
            params = {**self.params}
            params.update(kwargs)
            return params

        def build(self, **kwargs):
            params = self.build_params(**kwargs)
            return self.model(**params)

    @classmethod
    def build(cls, parent=None, **kwargs):
        model = cls.Factory(cls).build(**kwargs)

        if parent is not None:
            parent.add_child(model)

        return model
