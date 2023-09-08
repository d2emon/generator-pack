from factories.thing.nested_factory import NestedFactory as Factory

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
    interstellar_cloud = [
        "a bright pink", "a faint", "a fading", "a pale", "a fluo", "a glowing", "a green", "a bright green",
        "a dark brown", "a brooding", "a magenta", "a bright red", "a dark red", "a blueish", "a deep blue",
        "a turquoise", "a teal", "a golden", "a multicolored", "a silver", "a dramatic", "a luminous", "a colossal",
        "a purple", "a gold-trimmed", "an opaline", "a silvery", "a shimmering",
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

        def __call__(self):
            for f in self.factories:
                yield f()

    class ImageFactory:
        def __init__(self, image):
            self.image = image

        def __call__(self):
            return self.image

    class PositionFactory:
        default_positions = None

        def __init__(self, positions=None):
            self.positions = positions or self.default_positions

        def __call__(self):
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

    def life(self):
        yield from []

    def contents(self):
        yield from []

    def children(self):
        yield from self.default_children
        yield from self.life()
        yield from self.contents()

    ####

    @property
    def __class_name(self):
        return camel_case_to_spaces(self.__class__.__name__)

    def get_name_factory(
        self,
        name=None,
        *args,
        **kwargs,
    ):
        return self.NameFactory(name or self.__class_name)

    def get_children_factory(
        self,
        data=None,
        *args,
        **kwargs,
    ):
        return self.ChildrenFactory(data)

    def get_image_factory(
        self,
        name=None,
        *args,
        **kwargs,
    ):
        return self.ImageFactory(name or self.__class_name)

    def get_position_factory(
        self,
        name=None,
        *args,
        **kwargs,
    ):
        return self.PositionFactory(name or self.__class_name)

    def get_factories(self, name, children=None, names=None):
        return {
            "name": self.get_name_factory(name=names or name),
            "children": self.get_children_factory(data=children),
            "image": self.get_image_factory(name=name),
            "position": self.get_position_factory(name=name),
        }

    @classmethod
    def from_str(cls, name, children=None, names=None):
        return cls().get_factories(name, children, names)

    @property
    def thing_children(self, data=None):
        if self.__thing_children is None:
            factory = self.get_children_factory(data)
            children = factory()
            self.__thing_children = list(children)

        return self.__thing_children

    def thing_call(
        self,
        *args,
        name=None,
        **kwargs,
    ):
        name_factory = self.get_name_factory(name)
        image_factory = self.get_image_factory(name)
        return self.model(
            factory=self,
            name=name_factory(),
            image=image_factory(),
        )
