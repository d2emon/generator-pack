"""
Cnidarias

- Cnidaria
- Cnidaria Body
- Cnidaria Thoughts
- Cnidaria Thought
"""
from ..animal_body import AnimalBody, SimpleMouth, Jelly, SoftFlesh
from generated.mind import SimpleThoughts, Thought
from ..organism import Organism
from genesys.nested.data import lookups


class DataProvider:
    cnidaria_thought = lookups.cnidaria_thoughts
    cnidaria = lookups.cnidarias


class CnidariaBody(AnimalBody):
    class Factory(AnimalBody.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(AnimalBody.Factory.ChildrenFactory):
            def builders(self):
                yield SimpleMouth
                yield Jelly
                yield SoftFlesh


class CnidariaThought(Thought):
    class Factory(Thought.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Thought.Factory.BaseFactory):
            thoughts = property(lambda self: self.provider.cnidaria_thought)

            def __next__(self):
                return '{}{}'.format(
                    next(self.thoughts[0]),
                    next(self.thoughts[1]),
                )


class CnidariaThoughts(SimpleThoughts):
    class Factory(SimpleThoughts.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(SimpleThoughts.Factory.ChildrenFactory):
            thought_class = CnidariaThought


class Cnidaria(Organism):
    class Factory(Organism.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Organism.Factory.BaseFactory):
            def __next__(self):
                return next(self.provider.cnidaria)

        class ChildrenFactory(Organism.Factory.ChildrenFactory):
            body_class = CnidariaBody
            mind_class = CnidariaThoughts
