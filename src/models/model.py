class Model:
    """
    Base model
    """

    def __init__(self, *args, **fields):
        self.uuid = None
        self.__fields = {}
        self.fill(**fields)

    @classmethod
    def field_property(cls, field_name, default=None):
        return property(
            fget=lambda self: self.data.get(field_name, default),
            fset=lambda self, value: self.data.set(value, value),
        )

    @property
    def field_names(self):
        """
        :return: Field names
        """
        yield from []

    @property
    def data(self):
        """
        :return: Model data
        """
        return self.__fields

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

    def fill(self, **fields):
        field_names = list(self.field_names)
        self.__fields = {
            name: value
            for name, value in fields.items()
            if not len(field_names) or name in self.field_names
        }

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
