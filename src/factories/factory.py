class Factory:
    """
    Generate value
    """

    # def __init__(self, provider=None):
    #     self.provider = provider
    #     self.data = None

    @property
    def data(self):
        raise NotImplementedError()

    def __iter__(self):
        """
        Factory iterator

        :return: Factory
        """
        return self

    def __next__(self):
        """
        Generate result with default params

        :return: Result
        """
        return self.build()

    def build(self, *args, **kwargs):
        """
        Generate result

        :param args: Build args
        :param kwargs: Build kwargs
        :return: Result
        """
        return str(self.data) or None

    def items(self, count=5, *args, **kwargs):
        """
        Generate multiple results

        :param count: Number of results
        :param args: Build args
        :param kwargs: Build kwargs
        :return: Results
        """
        for _ in range(count):
            yield self.build(*args, **kwargs)
