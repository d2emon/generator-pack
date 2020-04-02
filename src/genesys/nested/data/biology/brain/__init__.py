"""
Brain Stuff
"""
from genesys.nested.models import Model
from ...space import BlackHole


class Memory(Model):
    class NameFactory(Model.NameFactory):
        default = '*MEMORY*'


class Memories(Model):
    memories = Model.children_property(Memory)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield from Memory.multiple(2, 4)


class Thought(Model):
    pass


class SadThought(Thought):
    class NameFactory(Thought.NameFactory):
        default = '*SADTHOUGHT*'


class HappyThought(Thought):
    class NameFactory(Thought.NameFactory):
        default = '*HAPPYTHOUGHT*'


class Thoughts(Model):
    thoughts = Model.children_property(Thought)
    black_hole = Model.child_property(BlackHole)

    class ChildrenFactory(Model.ChildrenFactory):
        @classmethod
        def fill_thoughts(cls):
            yield from SadThought.multiple(2, 4)
            yield from HappyThought.multiple(2, 4)

        def children_classes(self):
            yield BlackHole.probable(0.01)
            yield from self.fill_thoughts()


class Psyche(Model):
    thoughts = Model.child_property(Thoughts)
    memories = Model.child_property(Memories)
    contents = Model.children_property(Thoughts, Memories)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Thoughts
            yield Memories
