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
    class Factory(ThingBuilder):
        pass


class SadThought(Thought):
    default_name = '*SADTHOUGHT*'


class HappyThought(Thought):
    default_name = '*HAPPYTHOUGHT*'


class Thoughts(Model):
    thoughts = Model.children_property(Thought)
    black_hole = Model.child_property(BlackHole)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
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
