"""Base nested model."""
from typing import Callable
from .named_model import NamedModel
from .tree_model import TreeModel


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
        self.__placeholders = list(placeholders) if placeholders else []

    def add_placeholder(self, placeholder: Callable[[], TreeModel]) -> None:
        """Add placeholder.

        Args:
            placeholder (function): Factory to build child.
        """
        self.__placeholders.append(placeholder)

    def build_children(self) -> None:
        """Build children from placeholders."""
        super().build_children()

        if not self.__placeholders:
            return

        for placeholder in filter(None, self.__placeholders):
            self.add_child(placeholder(parent=self))

        self.__placeholders = []
