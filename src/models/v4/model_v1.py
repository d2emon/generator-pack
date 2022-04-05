import random
from genesys.nested.factories import Things
from .interface.model_v1 import ModelInterface
from .interface.named import NamedModelInterface
from .interface.tree import TreeModelInterface


class Model(ModelInterface, NamedModelInterface, TreeModelInterface):
    MODELS = []

    def __init__(self, factory=None, parent=None):
        super().__init__()
        self.__name = None
        self.__children = None
        # self.__image = None
        self.__parent = parent

        self.__factory = factory
        self.__template = None
        self.__position = None

    @property
    def name(self):
        if self.__name is None:
            self.__name = next(self.factory.name_factory)
        return self.__name

    @property
    def children(self):
        if self.__children is None:
            self.__children = []
            for child in self.generate_children():
                self.add_child(child)
            random.shuffle(self.__children)
        return self.__children

    @property
    def image(self):
        return self.factory.name

    @property
    def position(self):
        if self.__position is None:
            self.__position = next(self.factory.position_factory)
        return self.__position

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        self.__parent = value

    @property
    def factory(self):
        return self.__factory

    @property
    def template(self):
        return self.__template

    def add_child(self, child):
        if child is None:
            return

        if self.__children is None:
            self.__children = []

        self.__children.append(child)
        child.set_parent(self)

    def generate_children(self, *args, **kwargs):
        def by_name(thing_name):
            if name is None:
                return None

            thing = Things.get_thing(thing_name)
            if thing is None:
                print("NO CHILD", thing_name)
                return None

            return self.generate(thing.name)

        custom = self.factory.custom_factory()
        if custom is not None:
            for name in custom:
                yield by_name(name)
            return

        yield from (by_name(name) for factory in Things.get_factories(self.factory.name) for name in next(factory))

    def describe_gen(self, **kwargs):
        """
        :param kwargs:
        :return: Model factory's description factory with kwargs and children
        """
        return self.factory.description_factory({
            **kwargs,
            'children': kwargs['children'] or self.children
        })

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

    def __repr__(self):
        desc = '{} "{}"\t-\t'.format(self.parent.factory.name, self.parent.name) if self.parent else ''
        return ' '.join([
            desc,
            self.factory.name,
            '\"{}\"'.format(self.name),
        ])
