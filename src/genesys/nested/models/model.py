from genesys.nested.factories.data import NameFactory, BaseFactory, ChildrenFactory
from .generating import GeneratingModel
from .tree import TreeModel


class Placeholder:
    def __init__(self, builder):
        self.builder = builder
        self.__model = None

    def __build(self):
        self.__model = self.builder.build()
        return self.__model

    @property
    def model(self):
        return self.__model or self.__build()

    @model.setter
    def model(self, value):
        self.__model = value


class Model(GeneratingModel, TreeModel):
    class NameFactory(NameFactory):
        pass

    class BaseFactory(BaseFactory):
        pass

    class ChildrenFactory(ChildrenFactory):
        pass

    def __init__(self, name=None, base=None, children=None, parent=None):
        super().__init__(name, children, parent)
        self.__base = base

    def __build_name(self):
        # super().name = self.base or self.NameFactory.next(self.default_name)
        # return super().name
        return 'NAME'

    def __build_children(self):
        super().children = self.ChildrenFactory.next([])
        return super().name

    @property
    def default_name(self):
        return self.__class__.__name__

    @property
    def base(self):
        if self.__base is None:
            self.__base = self.BaseFactory.next(None)
        return self.__base

    @base.setter
    def base(self, value):
        self.__base = value

    # @property
    # def name(self):
    #     return super().name or self.__build_name()

    # @property
    # def children(self):
    #     return super().children or self.__build_children()
