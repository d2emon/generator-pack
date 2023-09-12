class Factory:
    """
    Base factory to build something with data.

    Attributes:
        data (Database): Database for factory.
        default_data (Database): Default database for factory.
    """

    default_data = None
    __instance = None

    def __init__(self, data=None):
        """
        Construct factory with data from database.

        Args:
            data (Database, optional): Database for factory. Defaults to None.
        """
        self.__data = data or self.default_data

    @property
    def data(self):
        return self.__data

    @classmethod
    def instance(cls, *args, **kwargs):
        """
        Get static instance of factory.

        Args:
            *args (list): Args for building factory.
            **kwargs (dict): Kwargs for building factory.

        Returns:
            Factory: Static instance of Factory.
        """
        if cls.__instance is None:
            cls.__instance = cls(*args, **kwargs)
        return cls.__instance

    def __iter__(self):
        """
        Factory iterator.

        Returns:
            Factory: Factory as iterator.
        """
        return self

    def __next__(self):
        """
        Generate result with default params.

        Returns:
            Something built by this factory.
        """
        return self()

    def __call__(self, *args, **kwargs):
        """
        Generate result

        Args:
            *args (list): Args for building result.
            **kwargs (dict): Kwargs for building result.

        Returns:
            Something built by this factory.
        """
        raise NotImplementedError()

    def items(self, count=5, *args, **kwargs):
        """
        Generate multiple results.

        Args:
            count (int): Number of results to build.
            *args (list): Args for building result.
            **kwargs (dict): Kwargs for building result.

        Returns:
            generator: Something built by this factory.

        :return: Results
        """
        for _ in range(count):
            yield self(*args, **kwargs)
