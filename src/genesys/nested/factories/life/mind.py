from generated import life
from ..factory import Factory


class MemoryFactory(Factory):
    default_model = life.Memory


class MemoriesFactory(Factory):
    default_model = life.Memories

    def children(self):
        yield MemoryFactory().multiple(2, 4)


class ThoughtFactory(Factory):
    default_model = life.Thought


class SadThoughtFactory(ThoughtFactory):
    default_name = '*SADTHOUGHT*'


class HappyThoughtFactory(ThoughtFactory):
    default_name = '*HAPPYTHOUGHT*'


class ThoughtsFactory(Factory):
    default_model = life.Thoughts

    def children(self):
        from ..universe import BlackHoleFactory

        yield BlackHoleFactory().probable(0.01)
        yield from SadThoughtFactory().multiple(2, 4)
        yield from HappyThoughtFactory().multiple(2, 4)


class PsycheFactory(Factory):
    default_model = life.Psyche

    def children(self):
        yield ThoughtsFactory()
        yield MemoriesFactory()


FACTORIES = {
    'psyche': PsycheFactory(),
    'thoughts': ThoughtsFactory(),
    'sad thought': SadThoughtFactory(),
    'happy thought': HappyThoughtFactory(),
    'memories': MemoriesFactory(),
    'memory': MemoryFactory(),
}
