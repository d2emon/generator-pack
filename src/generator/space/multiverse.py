import random

from generator.generator.generated import ListGenerated
from generator.generator.generator_data import ListData
from generator.generator.mathgen import TwoPoint
from generator import TextGenerator


from fixtures.space.multiverse import multiverse


class UniverseNameGenerator(TextGenerator):
    block_id = 'multiverse'


class GeneratedChildren:
    def __init__(self, child_generator, ids=()):
        self.ids = ids
        self._generated = dict()
        self.child_generator = child_generator()

    def __getitem__(self, item):
        key = self.ids[item]
        if self._generated.get(key) is None:
            self._generated[key] = self.child_generator.generate(item_id=key)
        return self._generated.get(key)

    def __len__(self):
        return len(self.ids)


class NamedGenerated(ListGenerated):
    name_generator_class = TextGenerator
    _name_generator = None

    children_count = ()

    def __init__(self, value=None, generator_data=None, item_id=None):
        if item_id is not None:
            random.seed(item_id)

        super().__init__(value or self.generate_name(generator_data))
        self._children = None

        if len(self.children_count) < 1:
            children_count = 0
        else:
            children_count = random.randrange(*self.children_count)

        self.children_ids = [self.generate_id() for _ in range(children_count)]

    @classmethod
    def name_generator(cls, generator_data=None):
        return cls._name_generator or cls.name_generator_class(generator_data)

    @classmethod
    def generate_name(cls, generator_data=None):
        return str(cls.name_generator(generator_data).generate()),

    @classmethod
    def generate_id(cls):
        return random.randrange(1024)

    @property
    def children(self):
        if self._children is None:
            self._children = GeneratedChildren(UniverseNameGenerator, self.children_ids)
        return self._children


class Multiverse(NamedGenerated):
    class MultiverseNameGenerator(TextGenerator):
        block_id = 'multiverse'

    data = {'value': ListData(multiverse)}
    name_generator = MultiverseNameGenerator

    children_count = 10, 30

    def __init__(self, value=None, generator_data=None, item_id=None):
        super().__init__(value, generator_data, item_id)
        self.positions = TwoPoint()
        self._universes = None

    @property
    def universes_ids(self):
        if self._children is None:
            self._children = [self.positions.generate() for _ in range(self.generate_children_count())]
        return self._children

    @property
    def universes(self):
        return self.universes_ids
