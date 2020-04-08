"""
Brain Stuff
"""
from genesys.nested.factories.thing_builder import ThingBuilder
from genesys.nested.models import Model
from genesys.nested.models.models.space import BlackHole


class Memory(Model):
    default_name = '*MEMORY*'

    class Factory(ThingBuilder):
        pass


class Memories(Model):
    memories = Model.children_property(Memory)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield from Memory.multiple(2, 4)


class Thought(Model):
    class Factory(Model.Factory):
        class BaseFactory(Model.Factory.BaseFactory):
            thoughts = property(lambda self: (thought for thought in []))

            def __next__(self):
                return next(self.thoughts)


class SadThought(Thought):
    default_name = '*SADTHOUGHT*'


class HappyThought(Thought):
    default_name = '*HAPPYTHOUGHT*'


class SimpleThoughts(Model):
    thoughts = Model.children_property(Thought)

    class Factory(Model.Factory):
        class ChildrenFactory(Model.Factory.ChildrenFactory):
            thought_class = Thought

            def builders(self):
                yield from self.thought_class.multiple(1)


class Thoughts(SimpleThoughts):
    black_hole = Model.child_property(BlackHole)

    class Factory(SimpleThoughts.Factory):
        class ChildrenFactory(SimpleThoughts.Factory.ChildrenFactory):
            @classmethod
            def fill_thoughts(cls):
                yield from SadThought.multiple(2, 4)
                yield from HappyThought.multiple(2, 4)

            def builders(self):
                yield BlackHole.probable(0.01)
                yield from self.fill_thoughts()


class Psyche(Model):
    thoughts = Model.child_property(Thoughts)
    memories = Model.child_property(Memories)
    contents = Model.children_property(Thoughts, Memories)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield Thoughts
                yield Memories
