"""Base tree model class."""
from typing import Collection
from .named_model import NamedModel


class NestedModel(NamedModel):
    """Model with parent and children."""

    def __init__(
        self,
        *children,
        parent=None,
        **fields,
    ):
        """Initialize tree model.

        Args:
            parent (NestedModel, optional): Parent for model. Defaults to None.
        """
        self.logger.debug('Create %s', self)
        self.logger.debug('Parent %s', parent)
        self.logger.debug('Children %s', children)
        self.logger.debug('Fields %s', fields)
        super().__init__(**fields)
        self.__children = list(children)
        self.__parent = parent

        self.__group_factories = {**fields}
        self.groups = {}

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
    def parent(self) -> NamedModel:
        """Get parent model.

        Returns:
            Model: Parent model.
        """
        return self.__parent

    @parent.setter
    def parent(self, value: NamedModel) -> None:
        # TODO: Update parent if changed
        self.__parent = value

    def build_children(self) -> None:
        """Build unbuilt children."""
        for child_id, child in enumerate(self.__children):
            self.__children[child_id] = self.check_child(child)

    def add_child(self, child: NamedModel) -> None:
        """Add child model.

        Args:
            child (TreeModel): Child model.
        """
        self.__children.append(child)
        child.parent = self

    def remove_child(self, child: NamedModel) -> None:
        """Remove child model.

        Args:
            child (TreeModel): Child model.
        """
        if child in self.__children:
            self.__children.remove(child)
        child.parent = None

    def children_by_class(self, *child_classes) -> Collection:
        """Get children with one of classes.

        Returns:
            Collection: Children with one of classes.
        """
        return (child for child in self.children if isinstance(child, child_classes))

    @classmethod
    def contents_property(cls, doc=None) -> property:
        """Property from children.

        Args:
            doc (str, optional): Property docstring. Defaults to None.

        Returns:
            property: Property to deal with children.
        """
        def get_contents(self) -> Collection:
            return [item for item in self.children if item]

        def set_contents(self, value: Collection) -> None:
            self.children = value

        return property(get_contents, set_contents, None, doc)

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
        def get_child(self) -> NamedModel:
            return next(self.children_by_class(child_classes), None)

        return property(get_child, None, None, doc)

    def fill_group(self, field_name):
        values = self.groups.get(field_name)

        if values is not None:
            return values

        factory = self.__group_factories.get(field_name)
        return self.check_child(factory)

    @classmethod
    def group_property(cls, field_name) -> property:
        """Create property to access fields.

        Args:
            field_name (str): Field name.

        Returns:
            property: Field property
        """

        def fget(self):
            values = self.groups.get(field_name)

            if values is not None:
                return values

            data = {
                'parent': self,
            }
            items = [self.check_child(item, **data) for item in self.fill_group(field_name)]
            self.groups[field_name] = items
            self.logger.debug('Get values %s: %s', field_name, items)
            return items

        def fset(self, value):
            self.groups[field_name] = value

        def fdel(self):
            del self.groups[field_name]

        return property(
            fget=fget,
            fset=fset,
            fdel=fdel,
        )

    # Search

    def __by_class(self, child_class) -> Collection:
        """Get children by class.

        Args:
            child_class (class): Class to search.

        Returns:
            Collection[Model]: Selected children.
        """
        return (child for child in self.children if isinstance(child, child_class))

    def all_by_class(self, child_class) -> Collection:
        """List children by class.

        Args:
            child_class (class): Class to search.

        Returns:
            Collection[Model]: Selected children.
        """
        return list(self.__by_class(child_class))

    def first_by_class(self, child_class) -> NamedModel:
        """Get child by class.

        Args:
            child_class (class): Class to search.

        Returns:
            Model: Selected child.
        """
        return next(self.__by_class(child_class), None)
