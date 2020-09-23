from genesys.nested.models.tree import TreeModel


class Model(TreeModel):
    default_name = None

    def __init__(
        self,
        name=None,
        *children,
        parent=None,
        placeholders=(),
        **kwargs,
    ):
        super().__init__(
            name or self.__default_name,
            list(children),
            parent,
        )
        self.__placeholders = list(placeholders)

    @property
    def __default_name(self):
        return self.default_name or self.__class__.__name__

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
