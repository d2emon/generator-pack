class Model:
    """
    Base model
    """

    def __init__(self, *args, **kwargs):
        self.uuid = None
        self.__args = args
        self.__kwargs = kwargs

    @property
    def data(self):
        """
        :return: Model data
        """
        return self.__kwargs

    @property
    def items(self):
        """
        :return: Model data
        """
        return self.data

    @property
    def raw_value(self) -> str:
        """
        :return: Model as raw string
        """
        return self['value']

    @property
    def value(self) -> str:
        """
        :return: Model as string
        """
        return self.raw_value

    def fill(self, *args, **kwargs):
        self.__args = args
        self.__kwargs = kwargs

    def __getitem__(self, item):
        return self.data.get(item)

    def __setitem__(self, key, value):
        self.data[key] = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"<{self.__class__.__name__}: \"{self}\">"

    def __len__(self):
        return len(str(self))
