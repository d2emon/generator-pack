"""
Plankton

- Plankton
- Plankton Body
- Plankton Thoughts
- Plankton Thought
"""
from ..animal_body import SimpleEye, SimpleMouth, Exoskeleton, Jelly, SoftFlesh
from ..mind import Thoughts, Thought
from ..organism import Organism, BasicBody
from genesys.nested.data import lookups


class DataProvider:
    plankton_thought = lookups.plankton_thoughts
    plankton = lookups.plankton


class PlanktonBody(BasicBody):
    class Factory(BasicBody.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(BasicBody.Factory.ChildrenFactory):
            def builders(self):
                yield from SimpleEye.multiple(0, 3)
                yield SimpleMouth
                yield Exoskeleton
                yield Jelly
                yield SoftFlesh


class PlanktonThought(Thought):
    class Factory(Thought.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Thought.Factory.BaseFactory):
            thoughts = property(lambda self: self.provider.plankton_thought)


class PlanktonThoughts(Thoughts):
    class Factory(Thoughts.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(Thoughts.Factory.ChildrenFactory):
            thought_class = PlanktonThought


class Plankton(Organism):
    class Factory(Organism.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Organism.Factory.BaseFactory):
            def __next__(self):
                return next(self.provider.plankton)

        class ChildrenFactory(Organism.Factory.ChildrenFactory):
            body_class = PlanktonBody
            mind_class = PlanktonThoughts
