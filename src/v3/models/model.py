class Model:
    """
    Base model
    """

    def __init__(self, *args, generated=True, factory=None, **kwargs):
        self.uuid = None
        self.__args = args
        self.__kwargs = kwargs
        self.generated = generated
        self.factory = factory

    @classmethod
    def prepare(cls, name) -> str:
        """
        Prepare model

        :param name: Unprepared model
        :return: Prepared model
        """
        return str(name)

    @classmethod
    def check_swear(cls, name) -> str:
        """
        Check name for bad words

        :param name: Uncleaned name
        :return: Cleaned name
        """
        return name

    @property
    def data(self):
        if not self.generated:
            self.__generate()
        return self.__kwargs

    @property
    def raw_value(self) -> str:
        """
        :return: Model as string
        """
        return self.data.get('value', '')

    @property
    def value(self) -> str:
        """
        :return: Model as string
        """
        value = self.raw_value
        return self.prepare(value)

    def fill(self, *args, **kwargs):
        self.__args = args
        self.__kwargs = kwargs

    def __generate(self):
        if self.factory is None:
            return
        self.__kwargs = self.factory(self)
        self.generated = True

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
