"""
Brain Stuff
"""
from models.nested_model import NestedModel as Model


class PsycheElement(Model):
    pass


class Memory(Model):
    default_name = '*MEMORY*'


class Thought(Model):
    pass


class Memories(PsycheElement):
    memories = Model.children_property(Memory)


class Thoughts(PsycheElement):
    thoughts = Model.children_property(Thought)

    @property
    def black_hole(self):
        from ..universe import BlackHole

        return self.children_by_class(BlackHole)


class Psyche(Model):
    contents = Model.children_property(PsycheElement)
    thoughts = Model.child_property(Thoughts)
    memories = Model.child_property(Memories)
