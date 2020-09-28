"""
Mollusk

- Mollusk
- Mollusk Body
- Mollusk Thoughts
"""
from ..animal_body import AnimalBody, SimpleEye, Tentacle, SoftFlesh, Jelly
from generated.life.body.body import Mouth
from ..mind import SimpleThoughts, Thought
from ..organism import Organism
from genesys.nested.data import lookups


class DataProvider:
    mollusk_thought = lookups.mollusk_thoughts
    mollusk = lookups.mollusks


class MolluskBody(AnimalBody):
    class Factory(AnimalBody.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(AnimalBody.Factory.ChildrenFactory):
            def builders(self):
                yield from SimpleEye.multiple(2)
                yield Mouth
                yield from Tentacle.multiple(6, 8)
                yield Jelly
                yield SoftFlesh


class MolluskThought(Thought):
    class Factory(Thought.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Thought.Factory.BaseFactory):
            thoughts = property(lambda self: self.provider.mollusk_thought)


class MolluskThoughts(SimpleThoughts):
    class Factory(SimpleThoughts.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(SimpleThoughts.Factory.ChildrenFactory):
            def builders(self):
                yield from MolluskThought.multiple(2)


class Mollusk(Organism):
    class Factory(Organism.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Organism.Factory.BaseFactory):
            def __next__(self):
                return next(self.provider.mollusk)

        class ChildrenFactory(Organism.Factory.ChildrenFactory):
            body_class = MolluskBody
            mind_class = MolluskThoughts
