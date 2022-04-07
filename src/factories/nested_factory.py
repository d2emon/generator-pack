import random
from models.model import Model
from .factory import Factory
from .model_factory import ModelFactory


class ChildFactory(Factory):
    def __init__(
        self,
        factory_class,
        min_count=1,
        max_count=None,
        probability=100,
    ):
        self.factory_class = factory_class
        self.min_count = min_count
        self.max_count = max_count
        self.probability = probability

    @classmethod
    def get_probability(cls, probability=100):
        if probability >= 100:
            return True

        return random.uniform(0, 100) < probability

    @classmethod
    def get_count(self, min_count=1, max_count=None):
        if max_count is None:
            return min_count
        
        return random.randint(min_count, max_count)

    def __call__(
        self,
        provider=None,
    ):
        if not self.check_probability(self.probability):
            return

        count = self.get_count(min_count=self.min_count, max_count=self.max_count)
        for _ in range(count):
            yield self.factory_class(
                provider=provider,
            )


class NestedFactory(ModelFactory):
    default_model = Model
    default_name = None
    default_children = []

    def __init__(self, provider=None, *args, **kwargs):
        self.provider = provider

    @property
    def model(self):
        return self.default_model

    @property
    def children(self):
        yield from self.default_children

    # Inherited methods

    def get_data(
        self,
        name=None,
        parent=None,
        **kwargs,
    ):
        return {
            "name": name or self.name_factory(provider=self.provider),
            "parent": parent,
            **kwargs,
        }

    def __call__(
        self,
        *children,
        model=None,
        **kwargs,
    ):
        model_factory = model or self.model_factory

        if len(children) > 0:
            args = list(children)
        else:
            args = self.children_factories()

        data = self.get_data(**kwargs)

        return model_factory(
            *children,
            **data,
        )

    # Factory methods

    def model_factory(self, *children, **kwargs):
        return self.model(*children, **kwargs)

    def name_factory(self, *args, **kwargs):
        return self.default_name

    def children_factories(self, *args, **kwargs):
        return [
            child_factory()
            for child_factory in self.children
            if child_factory is not None
        ]

    # Helper methods

    @classmethod
    def as_child(cls, min_count=1, max_count=None, probability=100):
        return ChildFactory(
            cls,
            min_count=min_count,
            max_count=max_count,
            probability=probability,
        )

    @classmethod
    def probable(cls, probability=100):
        return ChildFactory(cls, probability=probability)

    @classmethod
    def multiple(cls, min_items=1, max_items=None):
        return ChildFactory(cls, min_count=min_items, max_count=max_items)

    @classmethod
    def select_item(cls, *items):
        return random.choice(items) if len(items) else None
