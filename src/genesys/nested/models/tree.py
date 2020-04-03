class TreeModel:
    def __init__(self, name=None, children=None, parent=None):
        self.__name = name
        self.__children = children
        self.__parent = parent

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        self.__children = value

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        self.__parent = value

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return "<{} \"{}\">".format(self.__class__.__name__, str(self))

    def children_by_class(self, *child_classes):
        return (child for child in self.children if isinstance(child, child_classes))

    @classmethod
    def children_property(cls, *child_classes, doc=None):
        def get_children(self):
            return list(self.children_by_class(child_classes))

        return property(get_children, None, None, doc)

    @classmethod
    def child_property(cls, *child_classes, doc=None):
        def get_child(self):
            return next(self.children_by_class(child_classes), None)

        return property(get_child, None, None, doc)
