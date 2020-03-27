import random


def get_filtered_children(*child_classes):
    def child_getter(self):
        for child in self.children:
            for child_class in child_classes:
                if isinstance(child, child_class):
                    yield child
    return child_getter


class ChildFilterMixin:
    @property
    def children(self):
        raise NotImplementedError()

    def filter_children(self, *child_classes):
        return get_filtered_children(*child_classes)(self)


class Generating:
    @classmethod
    def generate(cls):
        yield cls()

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


class Model(ChildFilterMixin, Generating):
    class DataGenerator:
        default = None
        __instance = None

        def __init__(self, data=default):
            self.data = data

        def __iter__(self):
            return self

        def __next__(self):
            return self.data

        @classmethod
        def instance(cls):
            if cls.__instance is None:
                cls.__instance = cls(cls.default)
            return cls.__instance

        @classmethod
        def next(cls):
            return next(cls.instance())

    class NameGenerator(DataGenerator):
        def __next__(self):
            return self.data

    class BaseGenerator(DataGenerator):
        default = []

        def __next__(self):
            return random.choice(self.data) if self.data and len(self.data) > 0 else None

    class ChildrenGenerator(DataGenerator):
        default = [[]]

        def children_classes(self):
            for group in self.data:
                yield from group

        def __next__(self):
            return [c() for c in self.children_classes() if c is not None]

    def __init__(self, name=None, base=None, children=None):
        self.__name = name
        self.__base = base
        self.__children = children

    @property
    def name(self):
        if self.__name is None:
            base = self.base
            self.__name = base or self.NameGenerator.next() or self.__class__.__name__
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def base(self):
        if self.__base is None:
            self.__base = self.BaseGenerator.next()
        return self.__base

    @base.setter
    def base(self, value):
        self.__base = value

    @property
    def children(self):
        if self.__children is None:
            self.__children = self.ChildrenGenerator.next()
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


def thing(class_name, children, name):
    class Thing(Model):
        class NameGenerator(Model.DataGenerator):
            default = name

        class ChildrenGenerator(Model.DataGenerator):
            default = children

    Thing.__name__ = class_name
    return Thing
