"""
Worm

- Worm
- Worm Body
- Worm Thoughts
- Worm Thought
"""
from generated.life.biology.animal_body import AnimalBody, SimpleMouth, SoftFlesh
from generated.mind import SimpleThoughts, Thought
from generated.life.biology.organism import Organism
from genesys.nested.data import lookups


class DataProvider:
    worm_thought = lookups.worm_thoughts
    worm = lookups.worms


class WormBody(AnimalBody):
    class Factory(AnimalBody.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(AnimalBody.Factory.ChildrenFactory):
            def builders(self):
                yield SimpleMouth
                yield SoftFlesh


class WormThought(Thought):
    class Factory(Thought.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Thought.Factory.BaseFactory):
            thoughts = property(lambda self: self.provider.worm_thought)

            def __next__(self):
                return '{}{}'.format(
                    next(self.thoughts[0]),
                    next(self.thoughts[1]),
                )


class WormThoughts(SimpleThoughts):
    class Factory(SimpleThoughts.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(SimpleThoughts.Factory.ChildrenFactory):
            def builders(self):
                yield from WormThought.multiple(1, 2)


class Worm(Organism):
    class Factory(Organism.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Organism.Factory.BaseFactory):
            def __next__(self):
                return next(self.provider.worm)

        class ChildrenFactory(Organism.Factory.ChildrenFactory):
            body_class = WormBody
            mind_class = WormThoughts
