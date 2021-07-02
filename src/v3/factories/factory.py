class Factory:
    """
    Base factory class
   """
    __instance = None

    def __init__(self, *args, **kwargs):
        """
        Create factory
        """
        pass

    @classmethod
    def instance(cls, *args, **kwargs):
        """
        Get static instance of factory

        :param args: Factory args
        :param kwargs: Factory kwargs
        :return: Static instance
        """
        if cls.__instance is None:
            cls.__instance = cls(*args, **kwargs)
        return cls.__instance

    def __call__(self, *args, **kwargs):
        """
        Main factory method

        :param args: Generation args
        :param kwargs: Generation kwargs
        :return: Built by factory
        """
        raise NotImplementedError()

    def multiple(self, count=10, *args, **kwargs):
        """
        Build multiple models

        :param count: Count of models
        :param args: Model args
        :param kwargs: Fields to search in data
        :return: Models, built by factory
        """
        for generated_id in range(count):
            yield self(*args, generated_id=generated_id * 10, **kwargs)
