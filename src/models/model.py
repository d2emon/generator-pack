"""Base model class."""
from typing import Any, Collection


class Model:
    """Base model.

    Attributes:
        uuid (str): Model UUID.
        built_with (Factory): Model factory.
        values (Collection): Model values.
        field_names (Collection): Model field names.
    """

    field_names = []
    value_field_name = '_value'

    def __init__(self, *args, built_with=None, **fields):
        """Create data model.

        Args:
            built_with (Factory, optional): Model factory. Defaults to None.
        """
        self.uuid = None
        self.built_with = built_with
        self.values = [str(arg) for arg in args]
        self.__fields = {}
        self.fill(**fields)

    @classmethod
    def field_property(cls, field_name, default=None) -> property:
        """Create property to access fields.

        Args:
            field_name (str): Field name.
            default (Any, optional): Field defult value. Defaults to None.

        Returns:
            property: Field property
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
    def allowed_field_names(self) -> Collection:
        """Get field names.

        Yields:
            Iterator[Collection]: Field name.
        """
        yield from self.field_names

    @property
    def data(self) -> dict:
        """Get model fields.

        Returns:
            dict: Model fields.
        """
        return self.__fields

    @data.setter
    def data(self, value: dict) -> None:
        """Set model fields.

        Args:
            value (dict): Model fields.
        """
        self.__fields = value

    @property
    def _value(self) -> str:
        """Get model value.

        Returns:
            str: Model value.
        """
        return self.data.get('value')

    @_value.setter
    def _value(self, value: str) -> None:
        """Set model value.

        Args:
            value (str): Model value.
        """
        self.data['value'] = value

    @property
    def value(self) -> str:
        """Get model value.

        Returns:
            str: Model value.
        """
        return getattr(self, self.value_field_name, '')

    @value.setter
    def value(self, value: str) -> None:
        """Set model value.

        Args:
            value (str): Model value.
        """
        setattr(self, self.value_field_name, value)

    def fill(self, **fields) -> None:
        """Fill model fields."""
        field_names = list(self.allowed_field_names)
        self.__fields = {
            name: value
            for name, value in fields.items()
            if not field_names or name in field_names
        }

    def __getitem__(self, key: str) -> Any:
        """Get field value.

        Args:
            key (str): Field name.

        Returns:
            Any: Field value.
        """
        return self.data.get(key)

    def __setitem__(self, key: str, value: Any) -> None:
        """Set field value.

        Args:
            key (str): Field name.
            value (Any): Field value.
        """
        self.data[key] = value

    def __str__(self) -> str:
        """Convert model value to string.

        Returns:
            str: Model value.
        """
        return str(self.value)

    def __repr__(self) -> str:
        """Repr model.

        Returns:
            str: Model debug data.
        """
        return f"<{self.__class__.__name__}: \"{self}\">"

    def __len__(self) -> int:
        """Get length of model value.

        Returns:
            int: Length of model value.
        """
        return len(str(self))
