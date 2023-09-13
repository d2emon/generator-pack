from models.v5 import mind
from factories.thing.nested_factory import NestedFactory as Factory
from utils.nested import select_item


class MemoryFactory(Factory):
    default_model = mind.Memory


class MemoriesFactory(Factory):
    default_model = mind.Memories

    def children(self):
        yield MemoryFactory().multiple(2, 4)


class ThoughtFactory(Factory):
    default_model = mind.Thought
    thoughts = []

    def generate_name(self):
        return select_item(*self.thoughts)


class SadThoughtFactory(ThoughtFactory):
    thoughts = ['*SADTHOUGHT*']


class HappyThoughtFactory(ThoughtFactory):
    thoughts = ['*HAPPYTHOUGHT*']


class ThoughtsFactory(Factory):
    default_model = mind.Thoughts
    black_hole_probability = 0.01

    @classmethod
    def thoughts(cls):
        yield from SadThoughtFactory().multiple(2, 4)
        yield from HappyThoughtFactory().multiple(2, 4)

    def children(self):
        from ..universe import BlackHoleFactory

        yield BlackHoleFactory().probable(self.black_hole_probability)
        yield from self.thoughts()


class PsycheFactory(Factory):
    default_model = mind.Psyche

    @property
    def thoughts_factory(self):
        return ThoughtsFactory()

    @property
    def memories_factory(self):
        return MemoriesFactory()

    def children(self):
        yield self.thoughts_factory
        yield self.memories_factory


FACTORIES = {
    'psyche': PsycheFactory(),
    'thoughts': ThoughtsFactory(),
    'sad thought': SadThoughtFactory(),
    'happy thought': HappyThoughtFactory(),
    'memories': MemoriesFactory(),
    'memory': MemoryFactory(),
}
