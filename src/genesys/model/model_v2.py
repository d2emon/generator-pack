from .generating import GeneratingModel
from .model import Model as BaseModel
from .placeholder import Placeholder


class Model(BaseModel, GeneratingModel):
    def __init__(
        self,
        name=None,
        base=None,
        children=None,
        parent=None,
    ):
        super().__init__(
            name or self.__default_name,
            *children,
            parent,
        )
        self.__base = base

    # def __build_base(self):
    #     self.__base = next(self.Factory().base_factory)
    #     return self.__base

    # def __build_children(self):
    #     self.children = next(self.Factory().children_factory)
    #     return self.children

    # @property
    # def base(self):
    #     return self.__base or self.__build_base()

    # @base.setter
    # def base(self, value):
    #     self.__base = value

    @property
    def children(self):
        def child_builder(child):
            if isinstance(child, Placeholder):
                return child.model
            else:
                return child

        if any(isinstance(child, Placeholder) for child in super().children):
            super().children = map(child_builder, super().children)
        return super().children

    @property
    def model(self):
        return self
