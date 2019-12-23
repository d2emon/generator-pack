from .factories import ThingFactory, MultipleFactory, ProbableFactory, ListFactory


class Thing:
    default_children_data = []
    default_name = ""

    def __init__(self, name=None, *children):
        self.name = name or self.generate_name()
        self.children = children

    @classmethod
    def children_data(cls):
        return cls.default_children_data

    @classmethod
    def __generate_children(cls):
        for child in cls.children_data():
            if child is None:
                continue
            yield from child.factory().generate()

    @classmethod
    def factory(cls):
        return ThingFactory(cls)

    @classmethod
    def multiple_factory(cls, min_count, max_count=None):
        return MultipleFactory(cls, min_count, max_count)

    @classmethod
    def probable_factory(cls, probability):
        return ProbableFactory(cls, probability)

    @classmethod
    def list_factory(cls, items):
        return ListFactory(items)

    @classmethod
    def generate_name(cls):
        return cls.default_name

    @classmethod
    def generate(cls):
        return cls(cls.generate_name(), *cls.__generate_children())

    def find(self, child_class):
        return (child for child in self.children if isinstance(child, child_class))

    def find_one(self, child_class):
        return next(self.find(child_class), None)

    def __str__(self):
        return self.name
