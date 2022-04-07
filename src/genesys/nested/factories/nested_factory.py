from factories.nested_factory import NestedFactory as Factory

# TODO: Remove them
import random
from utils.camel_case import camel_case_to_spaces
from .child_factory import ChildFactory
from .name_factory import NameFactory


class DataProvider:
    multiverse = [
        "multiverse", "lasagnaverse", "doughnutverse", "towelverse", "baconverse", "sharkverse", "nestedverse",
        "tastyverse", "upverse", "downverse", "layerverse", "clusterverse", "metaverse", "quantiverse", "paraverse",
        "epiverse", "alterverse", "hypoverse", "dimensioverse", "planiverse", "pluriverse", "polyverse", "maniverse",
        "stackoverse", "antiverse", "superverse", "upperverse", "maxiverse", "megaverse", "babyverse", "tinyverse",
        "retroverse", "ultraverse", "topoverse", "otherverse", "bubbleverse", "esreverse", "versiverse", "'verse",
        "cookieverse", "grandmaverse",        
    ]


DEFAULT_DATA_PROVIDER = DataProvider()


class NestedFactory(Factory):
    # TODO: Remove inner classes
    class NameFactory(NameFactory):
        default_data = None

        def __init__(self, data=None):
            provider = NameFactory.DataProvider(data or self.default_data)
            super().__init__(provider)

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

    def __init__(
        self,
        provider=DEFAULT_DATA_PROVIDER,
        *args,
        **kwargs,
    ):
        super().__init__(provider=provider, *args, **kwargs)

        # TODO: Remove this fields
        self.thing_name = None
        self.__thing_children = None
        self.thing_factories = []

        self.thing_name_factory = None
        self.thing_children_factory = None
        self.thing_image_factory = None
        self.thing_position_factory = None

    ####

    @classmethod
    def old_init(
        cls,
        name=None,
        name_factory=None,
        names_data=None,
        children_data=None,
        **params,
    ):
        factory = cls()
        factory.thing_name = name or camel_case_to_spaces(type(factory).__name__)
        factory.thing_name_factory = name_factory or factory.NameFactory(names_data or factory.thing_name)
        factory.thing_children_factory = factory.ChildrenFactory(children_data)
        factory.thing_image_factory = factory.ImageFactory(factory.thing_name)
        factory.thing_position_factory = factory.PositionFactory(factory.thing_name)
        return factory

    @classmethod
    def from_str(cls, name, children=None, names=None):
        return cls.old_init(name, names_data=names, children_data=children)

    @property
    def thing_children(self):
        if self.__thing_children is None:
            self.__thing_children = list(next(self.thing_children_factory))

        return self.__thing_children

    def thing_call(self, *args, **kwargs):
        return self.model(
            factory=self,
            name=next(self.thing_name_factory),
            image=next(self.thing_image_factory),
        )
