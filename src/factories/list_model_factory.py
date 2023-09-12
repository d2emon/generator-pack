from .list_factory import ListFactory
from .model_factory import ModelFactory


class ListModelFactory(ModelFactory):
    def __init__(self, data=None):
        super().__init__(data)

        self.data_factory = ListFactory(data)

    @property
    def model(self):
        """
        Build model

        :return: Model, built by factory
        """
        raise NotImplementedError()
