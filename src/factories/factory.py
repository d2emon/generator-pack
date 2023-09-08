class Factory:
    """Generate value."""

    __instance = None

    def __init__(self, data=None):
        self.__data_provider = data

    @property
    def data_provider(self):
        return self.__data_provider

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
