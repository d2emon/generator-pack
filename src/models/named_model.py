"""Named model class."""
from .model import Model
from .field_mixins import WithName


class NamedModel(WithName, Model):
    """Model with name.

    Attribute:
        default_name (str): Default name for model.
    """

    default_name = None

    def __init__(self, name=None, *args, **kwargs):
        """Initialize model.

        Args:
            name (str, optional): Initial name for model. Defaults to None.
        """
        super().__init__(*args, name=name, **kwargs)

    def get_name(self):
        return self.default_name or self.__class__.__name__ or ''
