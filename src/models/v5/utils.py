import random


class Factory:
    factories = {}

    def __init__(self, name, contains, name_factory):
        self.name = name
        self.contains = contains
        self.name_factory = name_factory

        self.factories[name] = self

    @property
    def items(self):
        yield from self.contains

        for item_id, item in enumerate(self.contains):
            if isinstance(item, str):
                continue

            if item[0] != '.':
                continue

            factory = self.factories.get(item[1:])
            if factory is not None:
                yield factory.contains

            self.contains[item_id] = ''

    def clean_thing(self):
        self.contains = [item for item in self.items if item]

    @classmethod
    def clean_things(cls):
        for factory in cls.factories.values():
            factory.clean_thing()

    @classmethod
    def build(cls, what, *args, **kwargs):
        factory = cls.factories.get(what)
        if factory is None:
            return None
        return factory(*args, **kwargs)

    def build_name(self, *args, **kwargs):
        if self.name_factory is not None:
            return self.name_factory(*args, **kwargs)
        
        self.name

    def __call__(self, *args, **kwargs):
        return Model(self, self, *args, **kwargs)

    @classmethod
    def __parse_amount(cls, data):
        options = data.split('-')
        if len(options) < 2:
            return options[0]
        
        return random.randrange(options[0], options[1])

    @classmethod
    def __parse_probability(cls, data):
        amount = cls.__parse_amount(data)

        options = data.split("%")
        if len(options) < 2:
            return amount, 100

        return 1, options[0]

    @classmethod
    def __parse_options(cls, value):
        data = value.split(',')

        factory = cls.factories.get(data[0])

        if len(data) < 2:
            return factory, 0, 100

        amount, probability = cls.__parse_probability(data[1])
        return factory, amount, probability

    def get_children_factories(self):
        for item_id in self.contains:
            item = item_id if isinstance(item, str) else random.choice(item)
            factory, amount, probability = self.__parse_options(item)

            if factory is None:
                continue

            if random.randrange(0, 100) > probability:
                continue

            for _ in range(0, amount):
                yield factory


class Model:
    instances = []

    def __init__(self, factory, *args, parent=None, **kwargs):
        self.name = 'thing'
        self.factory = factory
        self.parent = parent
        self.children = []
        self.n = len(self.instances)
        self.display = 0
        self.grown = False

        self.args = args
        self.kwargs = kwargs

        self.instances.append(self)

    def name(self):
        pass

    def __parse_amount(self, data):
        options = data.split('-')
        if len(options) < 2:
            return options[0]
        
        return random.randrange(options[0], options[1])

    def __parse_probability(self, data):
        amount = self.__parse_amount(data)

        options = data.split("%")
        if len(options) < 2:
            return amount, 100

        return 1, options[0]

    def grow(self):
        if self.grown:
            return

        self.name()

        for factory in self.factory.get_children_factories():
            child = factory(parent=self)
            self.children.append(child)

        self.grown = True
