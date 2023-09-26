"""Base nested model."""
from models.named_model import NamedModel
from models.tree_model import TreeModel


class NestedModel(TreeModel, NamedModel):
    """Model with name, parent, children and placeholders."""

    def __init__(
        self,
        name=None,
        *children,
        parent=None,
        placeholders=None,
    ):
        """Initialize nested model.

        Args:
            name (str, optional): Model name. Defaults to None.
            parent (Model, optional): Parent model. Defaults to None.
            placeholders (Collection[Callable[[], TreeModel]], optional):
              Factories to build children. Defaults to None.
        """
        super().__init__(
            *children,
            parent=parent,
            name=name,
        )
        self.placeholders = list(placeholders) if placeholders else []

    def build_children(self) -> None:
        """Build children from placeholders."""
        super().build_children()

        if not self.placeholders:
            return

        for placeholder in filter(None, self.placeholders):
            self.add_child(placeholder(parent=self))

        self.placeholders = []
