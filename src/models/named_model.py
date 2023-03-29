"""Named model class."""
from .model import Model


class NamedModel(Model):
    """Model with name.

    Attribute:
        default_name (str): Default name for model.
    """

    default_name = None
    field_names = [
        'name',
    ]
    value_field_name = 'name'

    def __init__(self, name=None, *args, **kwargs):
        """Initialize model.

        Args:
            name (str, optional): Initial name for model. Defaults to None.
        """
        super().__init__(*args, name=name, **kwargs)

    @property
    def name(self) -> str:
        """Get model value.

        Returns:
            str: Model value.
        """
        if self['name'] is None:
            self['name'] = self.get_name()

        return self['name']

    @name.setter
    def name(self, value: str):
        """Set model value.

        Args:
            value (str): Model value.
        """
        self['name'] = value

    def get_name(self):
        return self.default_name or self.__class__.__name__ or ''
