"""
Plankton

- Plankton
- Plankton Body
- Plankton Thoughts
- Plankton Thought
"""
from ..animal_body import AnimalBody, SimpleEye, SimpleMouth, Exoskeleton, Jelly, SoftFlesh
from generated.mind import SimpleThoughts, Thought
from ..organism import Organism
from genesys.nested.data import lookups


class DataProvider:
    plankton_thought = lookups.plankton_thoughts
    plankton = lookups.plankton


class PlanktonBody(AnimalBody):
    class Factory(AnimalBody.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(AnimalBody.Factory.ChildrenFactory):
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


class PlanktonThoughts(SimpleThoughts):
    class Factory(SimpleThoughts.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(SimpleThoughts.Factory.ChildrenFactory):
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
