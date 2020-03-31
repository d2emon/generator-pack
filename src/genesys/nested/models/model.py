import random
from ..factories import Things


class Model:
    MODELS = []

    def __init__(self, factory=None, parent=None):
        self.__name = None
        self.__children = None
        self.__image = None
        self.parent = None

        self.factory = factory

        self.set_parent(parent)

        self.template = None

        self.__position = None

    @property
    def name(self):
        if self.__name is None:
            self.__name = next(self.factory.name_factory)
        return self.__name

    @property
    def image(self):
        return self.factory.name

    @property
    def position(self):
        if self.__position is None:
            self.__position = next(self.factory.position_factory)
        return self.__position

    def set_parent(self, parent=None):
        self.parent = parent

    def add_child(self, child):
        if child is None:
            return

        if self.__children is None:
            self.__children = []

        self.__children.append(child)
        child.set_parent(self)

    @property
    def children(self):
        if self.__children is None:
            self.__children = []
            for child in self.generate_children():
                self.add_child(child)
            random.shuffle(self.__children)
        return self.__children

    def generate_children(self, *args, **kwargs):
        def by_name(thing_name):
            if name is None:
                return None

            thing = Things.get_thing(thing_name)
            if thing is None:
                print("NO CHILD", thing_name)
                return None

            return Model.generate(thing.name)

        # print("GROW", args, kwargs)

        custom = self.factory.custom_factory()
        if custom is not None:
            for name in custom:
                yield by_name(name)
            return

        yield from (by_name(name) for factory in Things.get_factories(self.factory.name) for name in next(factory))

    def __repr__(self):
        desc = '{} "{}"\t-\t'.format(self.parent.factory.name, self.parent.name) if self.parent else ''
        return ' '.join([
            desc,
            self.factory.name,
            '\"{}\"'.format(self.name),
        ])

    @classmethod
    def get_factory(cls, name='error'):
        return Things.get_thing(name) or Things.get_thing('error')

    @classmethod
    def generate(cls, factory_name, parent=None):
        model = cls(
            factory=cls.get_factory(factory_name),
            parent=parent,
        )
        cls.MODELS.append(model)
        return model

    def describe_gen(self, **kwargs):
        return self.factory.description_factory({
            **kwargs,
            'children': kwargs['children'] or self.children
        })
