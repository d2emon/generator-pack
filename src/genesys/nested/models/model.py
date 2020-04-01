import random
from genesys.nested.factories.data import NameFactory, BaseFactory, ChildrenFactory


class GeneratingModel:
    @classmethod
    def probable(cls, probability=100):
        return cls if random.uniform(0, 100) < probability else None

    @classmethod
    def multiple(cls, min_items=1, max_items=None):
        count = random.randint(min_items, max_items) if max_items is not None else min_items
        for _ in range(count):
            yield cls

    @classmethod
    def choice(cls, items):
        return random.choice(items) if len(items) > 0 else None


class Model(GeneratingModel):
    class NameFactory(NameFactory):
        pass

    class BaseFactory(NameFactory):
        pass

    class ChildrenFactory(ChildrenFactory):
        pass

    def __init__(self, name=None, base=None, children=None):
        self.__name = name
        self.__base = base
        self.__children = children

    @property
    def default_name(self):
        return self.__class__.__name__

    @property
    def name(self):
        if self.__name is None:
            self.__name = self.base or self.NameFactory.next(self.default_name)
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def base(self):
        if self.__base is None:
            self.__base = self.BaseFactory.next(None)
        return self.__base

    @base.setter
    def base(self, value):
        self.__base = value

    @property
    def children(self):
        if self.__children is None:
            self.__children = self.ChildrenFactory.next([])
        return self.__children

    @children.setter
    def children(self, value):
        self.__children = value

    def __str__(self):
        return self.name

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
