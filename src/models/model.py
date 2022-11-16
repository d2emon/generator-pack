from typing import Any, Collection


class Model:
    """
    Base model
    """

    def __init__(self, *args, built_with=None, **fields):
        self.uuid = None
        self.built_with = built_with
        self.values = [str(arg) for arg in args]
        self.__fields = {}
        self.fill(**fields)

        # print("Model", repr(self), self.uuid)
        # print("With", self.built_with)
        # print("Args", args, fields)


    @classmethod
    def field_property(cls, field_name, default=None):
        """
        :return: Property to access field
        """
        def fget(self):
            return self.data.get(field_name, default)

        def fset(self, value):
            self.data[field_name] = value

        def fdel(self):
            del self.data[field_name]

        return property(
            fget=fget,
            fset=fset,
            fdel=fdel,
        )

    @property
    def field_names(self) -> Collection:
        """
        :return: Field names
        """
        yield from []

    @property
    def data(self) -> dict:
        """
        :return: Model data
        """
        return self.__fields

    @property
    def value(self) -> str:
        """
        :return: Model as string
        """
        return self['value']

    def fill(self, **fields) -> None:
        """
        Fill model fields
        """
        field_names = list(self.field_names)
        self.__fields = {
            name: value
            for name, value in fields.items()
            if not len(field_names) or name in field_names
        }

    def __getitem__(self, item) -> Any:
        """
        :return: Get field
        """
        return self.data.get(item)

    def __setitem__(self, key, value) -> None:
        """
        :return: Set field
        """
        self.data[key] = value

    def __str__(self) -> str:
        return str(self.value).title()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: \"{self}\">"

    def __len__(self) -> int:
        return len(str(self))
