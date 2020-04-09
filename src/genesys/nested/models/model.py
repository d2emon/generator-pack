from genesys.nested.factories.thing_builder import ThingBuilder
from .generating import GeneratingModel
from .tree import TreeModel


class Placeholder:
    def __init__(self, model_class, builder):
        self.model_class = model_class
        self.builder = builder()
        self.__model = None

    def __build(self):
        self.__model = self.model_class(**self.builder.build())
        return self.__model

    @property
    def model(self):
        return self.__model or self.__build()

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def placeholder(self):
        return self


class Model(GeneratingModel, TreeModel):
    default_name = None

    class Factory(ThingBuilder):
        pass

    def __init__(self, name=None, base=None, children=None, parent=None):
        super().__init__(name or self.__default_name, children, parent)
        self.__base = base
        self.__children = children

    def __build_base(self):
        self.__base = next(self.Factory().base_factory)
        return self.__base

    def __build_children(self):
        super().children = next(self.Factory().children_factory)
        return super().name

    @property
    def __default_name(self):
        return self.default_name or self.__class__.__name__

    @property
    def base(self):
        return self.__base or self.__build_base()

    @base.setter
    def base(self, value):
        self.__base = value

    @property
    def children(self):
        if self.__children is None:
            self.__children = self.__build_children()
        if any(isinstance(child, Placeholder) for child in self.__children):
            self.__children = [child.model for child in self.__children]
        return self.__children

    @children.setter
    def children(self, value):
        self.__children = value

    @property
    def model(self):
        return self

    @classmethod
    def placeholder(cls):
        return Placeholder(cls, cls.Factory)

    @classmethod
    def build(cls):
        return cls.placeholder().model
