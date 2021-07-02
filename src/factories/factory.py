class Factory:
    """
    Generate value
    """
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
        return self()

    def __call__(self, *args, **kwargs):
        """
        Generate result

        :param args: Build args
        :param kwargs: Build kwargs
        :return: Result
        """
        raise NotImplementedError()

    def items(self, count=5, *args, **kwargs):
        """
        Generate multiple results

        :param count: Number of results
        :param args: Build args
        :param kwargs: Build kwargs
        :return: Results
        """
        for _ in range(count):
            yield self(*args, **kwargs)
