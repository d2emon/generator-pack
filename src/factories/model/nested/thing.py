from factories.model.model import ModelFactory


class ThingFactory(ModelFactory):
    """
    Base factory for nested
    """

    @property
    def data(self):
        raise NotImplementedError()
