from .model_factory import ModelFactory
from .list_factory import ListFactory


class ListModelFactory(ModelFactory):
    def __init__(self, data):
        super().__init__()

        self.__factory = ListFactory(data)

    @property
    def model(self):
        """
        Build model

        :return: Model, built by factory
        """
        raise NotImplementedError()

    def generate(self, *args, **kwargs):
        return self.__factory(*args, **kwargs)
