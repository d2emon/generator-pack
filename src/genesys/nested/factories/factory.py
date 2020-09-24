import random


class Factory:
    default_model = None
    default_name = None

    def __init__(
        self,
        model=None,
        name=None,
        placeholders=(),
    ):
        self.model = model or self.default_model
        self.name = name or self.default_name
        self.placeholders = placeholders

    def children(self):
        yield from self.placeholders

    def __call__(
        self,
        name=None,
        *children,
        parent=None,
        placeholders=None,
        **kwargs,
    ):
        return self.model(
            name=name or self.name,
            *children,
            parent=parent,
            placeholders=placeholders or self.children(),
            **kwargs,
        )

    def probable(self, probability=100):
        return self if random.uniform(0, 100) < probability else None

    def multiple(self, min_items=1, max_items=None):
        count = random.randint(min_items, max_items) if max_items is not None else min_items
        for _ in range(count):
            yield self

    @classmethod
    def select_factory(cls, *factories):
        return random.choice(factories) if len(factories) else None

    @classmethod
    def create_factory(cls, model, default=None):
        class NewFactory(cls):
            model_class = model
            default_name = default

        return NewFactory
