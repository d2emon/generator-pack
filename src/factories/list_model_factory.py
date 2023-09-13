from .list_factory import ListFactory
from .model_factory import ModelFactory


class ListModelFactory(ModelFactory):
    def __init__(self, data=None):
        super().__init__(data)

        self.__data_factory = ListFactory(data)

    @property
    def model(self):
        """
        Build model

        :return: Model, built by factory
        """
        raise NotImplementedError()

    def data_factory(self, *args, **kwargs):
        """Generate data

        Args:
            *args: Data args.
            **kwargs: Data kwargs.

        Returns:
            str: Resulting name
        """
        return self.__data_factory(*args, **kwargs)
