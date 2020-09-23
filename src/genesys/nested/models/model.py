from genesys.nested.factories.v2.thing_builder import ThingBuilder
from genesys.nested.models.mixins.generating import GeneratingModel
from .tree import TreeModel
from .placeholder import Placeholder


class ModelBuilder:
    class Factory(ThingBuilder):
        pass

    @classmethod
    def placeholder(cls, **kwargs):
        return Placeholder(cls, cls.Factory, **kwargs)

    @classmethod
    def build(cls, parent=None, **kwargs):
        model = cls.placeholder(**kwargs).model
        if parent is not None:
            parent.add_child(model)
        return model


class Model(GeneratingModel, TreeModel):
    default_name = None

    def __init__(
        self,
        name=None,
        base=None,
        children=None,
        parent=None,
    ):
        super().__init__(
            name or self.__default_name,
            children,
            parent,
        )
        self.__base = base
        self.__children = children

    # def __build_base(self):
    #     self.__base = next(self.Factory().base_factory)
    #     return self.__base

    # def __build_children(self):
    #     self.__children = next(self.Factory().children_factory)
    #     return self.__children

    @property
    def __default_name(self):
        return self.default_name or self.__class__.__name__

    # @property
    # def base(self):
    #     return self.__base or self.__build_base()

    # @base.setter
    # def base(self, value):
    #     self.__base = value

    @property
    def children(self):
        # if self.__children is None:
        #     self.__children = self.__build_children()
        if any(isinstance(child, Placeholder) for child in self.__children):
            self.__children = [child.model for child in self.__children]
        return self.__children

    @children.setter
    def children(self, value):
        self.__children = value

    @property
    def model(self):
        return self
