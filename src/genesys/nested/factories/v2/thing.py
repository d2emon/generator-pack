import random
from utils.camel_case import camel_case_to_spaces
from .children import ChildFactory
from .name import NameFactory


class Factory:
    class NameFactory(NameFactory):
        default_data = None

        def __init__(self, data=None):
            super().__init__(data or self.default_data)

    class ChildrenFactory:
        default_data = []
        default_factories = []
        default_factory = None

        def __init__(self, data=None):
            self.data = data or self.default_data

        @property
        def factories(self):
            yield from self.default_factories
            yield from (ChildFactory.from_str(child) for child in self.data)
            if self.default_factory is not None:
                yield ChildFactory(*self.default_factory)

        def __iter__(self):
            return self

        def __next__(self):
            return (next(f) for f in self.factories)

    class ImageFactory:
        def __init__(self, image):
            self.image = image

        def __iter__(self):
            return self

        def __next__(self):
            return self.image

    class PositionFactory:
        default_positions = None

        def __init__(self, positions=None):
            self.positions = positions or self.default_positions

        def __iter__(self):
            return self

        def __next__(self):
            return [random.randrange(*pos) if len(pos) > 1 else None for pos in self.positions]

    # things_n = 0
    model_type = None

    def __init__(
        self,
        name=None,
        name_factory=None,
        names_data=None,
        children_data=None,
        **params,
    ):
        self.name = name or camel_case_to_spaces(type(self).__name__)
        self.__children = None

        self.name_factory = name_factory or self.NameFactory(names_data or self.name)
        self.children_factory = self.ChildrenFactory(children_data)
        self.image_factory = self.ImageFactory(self.name)
        self.position_factory = self.PositionFactory(self.name)

    @property
    def children(self):
        if self.__children is None:
            self.__children = list(next(self.children_factory))
        return self.__children

    def __call__(self, *args, **kwargs):
        return self

    def __iter__(self):
        return self

    def __next__(self):
        model = self.model_type()
        model.factory = self
        model.name = next(self.name_factory)
        model.image = next(self.image_factory)
        return model

    def clear(self):
        # def process_factory(factory):
        #     if not isinstance(factory.data, str):
        #         yield factory
        #         return
        #     if factory.data[0] != '.':
        #         yield factory
        #         return
        #     sub_name = factory.data[1:]
        #     sub_item = self.get_thing(sub_name)
        #     if sub_item is not None:
        #         yield from sub_item.factories

        # factories = [process_factory(factory) for factory in self.factories]
        # # print(self.name, self.factories, "+", to_concat)
        # # print(list(f))
        # self.factories = [factory for factory in factories if factory is not None]
        pass


class Thing(Factory):
    @classmethod
    def from_str(cls, name, children=None, names=None):
        thing = cls(name, names_data=names, children_data=children)
        # thing.name_factory = NameFactory(name_factory, defaulr=name)
        # thing.factories += [ChildFactory.from_str(child) for child in children]
        # thing.add_factories(children)
        print('FACTORIES', thing.name, thing.children)
        return thing
