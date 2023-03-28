"""Complex model class."""
from typing import Collection
from .model import Model


class ComplexModel(Model):
    """Model with children.

    Attributes:
        uuid (str): Model UUID.
        built_with (Factory): Model factory.
        values (Collection): Model values.
        static_field_names (Collection): Model field names.
        children (dict): Model children.
    """

    static_field_names = []
    children = {}

    @property
    def field_names(self) -> Collection:
        """Get field names.

        Yields:
            Iterator[Collection]: Field name.
        """
        yield from self.static_field_names
        yield from self.children.keys()

    def with_children(self) -> Model:
        """Fill model with children fields.

        Generate empty children fields

        Returns:
            Model: Model with children fields.
        """
        for field, factory in self.children.items():
            if self.data.get(field) is None:
                child = factory()
                self.data[field] = child.with_children() \
                    if isinstance(child, ComplexModel) else child

        return self
