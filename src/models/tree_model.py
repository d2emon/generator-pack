"""Base tree model class."""
from typing import Collection
from factories.factory import Factory
from .model import Model


class TreeModel(Model):
    """Model with parent and children."""

    def __init__(
        self,
        *children,
        parent=None,
    ):
        """Initialize tree model.

        Args:
            parent (TreeModel, optional): Parent for model. Defaults to None.
        """
        super().__init__()
        self.__children = list(children)
        self.__parent = parent

    @property
    def children(self) -> list:
        """Get children models.

        Returns:
            list: Children models.
        """
        self.build_children()
        return self.__children

    @children.setter
    def children(self, value: list) -> None:
        """Set children models.

        Args:
            value (list): Children models.
        """
        self.__children = value

    @property
    def parent(self) -> Model:
        """Get parent model.

        Returns:
            Model: Parent model.
        """
        return self.__parent

    # TODO: Update parent if changed

    def build_children(self) -> None:
        """Build unbuilt children."""
        for id, child in enumerate(self.__children):
            if isinstance(child, Factory):
                self.__children[id] = child()

    def add_child(self, child: Model) -> None:
        """Add child model.

        Args:
            child (TreeModel): Child model.
        """
        self.__children.append(child)
        child.__parent = self

    def remove_child(self, child: Model) -> None:
        """Remove child model.

        Args:
            child (TreeModel): Child model.
        """
        if child in self.__children:
            self.__children.remove(child)
        child.__parent = None

    def children_by_class(self, *child_classes) -> Collection:
        """Get children with one of classes.

        Returns:
            Collection: Children with one of classes.
        """
        return (child for child in self.children if isinstance(child, child_classes))

    @classmethod
    def children_property(cls, *child_classes, doc=None) -> property:
        """Property from children.

        Args:
            doc (str, optional): Property docstring. Defaults to None.

        Returns:
            property: Property to deal with children.
        """
        def get_children(self) -> Collection:
            return list(self.children_by_class(child_classes))

        return property(get_children, None, None, doc)

    @classmethod
    def child_property(cls, *child_classes, doc=None) -> property:
        """Property from child.

        Args:
            doc (str, optional): Property docstring. Defaults to None.

        Returns:
            property: Property to deal with child.
        """
        def get_child(self) -> Model:
            return next(self.children_by_class(child_classes), None)

        return property(get_child, None, None, doc)
