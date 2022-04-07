from factories.factory import Factory


class TreeModel:
    def __init__(
        self,
        *children,
        parent=None,
    ):
        self.__children = list(children)
        self.__parent = parent

    @property
    def children(self):
        self.__build_children()
        return self.__children

    @children.setter
    def children(self, value):
        self.__children = value

    @property
    def parent(self):
        return self.__parent

    # @parent.setter
    # def parent(self, value):
    #     if self.__parent is not None:
    #         self.__parent.remove_child(self)
    #
    #     value.add_child(self)

    def __build_children(self):
        for id, child in enumerate(self.__children):
            if isinstance(child, Factory):
                self.__children[id] = child()

    def add_child(self, child):
        self.__children.append(child)
        child.__parent = self

    def remove_child(self, child):
        if child in self.__children:
            self.__children.remove(child)
        child.__parent = None

    def children_by_class(self, *child_classes):
        return (child for child in self.children if isinstance(child, child_classes))

    @classmethod
    def children_property(cls, *child_classes, doc=None):
        def get_children(self):
            # return list(self.children_by_class(child_classes))
            children = list(self.children_by_class(child_classes))
            return children

        return property(get_children, None, None, doc)

    @classmethod
    def child_property(cls, *child_classes, doc=None):
        def get_child(self):
            return next(self.children_by_class(child_classes), None)

        return property(get_child, None, None, doc)
