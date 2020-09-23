from .named import NamedModel
from .tree import TreeModel


class Model(TreeModel, NamedModel):
    def __init__(
        self,
        name=None,
        *children,
        parent=None,
        placeholders=(),
        **kwargs,
    ):
        super().__init__(
            *children,
            parent=parent,
        )
        NamedModel.__init__(self, name)
        self.__placeholders = list(placeholders)

    @property
    def children(self):
        self.build_children()
        return super().children

    def add_placeholder(self, placeholder):
        self.__placeholders.append(placeholder)

    def build_children(self):
        if not len(self.__placeholders):
            return
        for placeholder in filter(None, self.__placeholders):
            self.add_child(placeholder(parent=self))
        self.__placeholders = []
