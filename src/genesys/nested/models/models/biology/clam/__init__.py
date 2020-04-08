"""
Clams

- Clam
- Clam Body
- Clam Thoughts
- Clam Thought
"""
from genesys.nested.models.models.unknown import Mind
from ..animal_body import SoftFlesh, ClamShell
from ..mind import SimpleThoughts, Thought
from ..organism import Organism, BasicBody
from genesys.nested.data import lookups


class DataProvider:
    clam_thought = lookups.clam_thoughts
    clam = lookups.clams


class ClamBody(BasicBody):
    class Factory(BasicBody.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(BasicBody.Factory.ChildrenFactory):
            def builders(self):
                yield ClamShell
                yield ClamShell
                yield Mind
                yield SoftFlesh


class ClamThought(Thought):
    class Factory(Thought.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Thought.Factory.BaseFactory):
            thoughts = property(lambda self: self.provider.plankton_thought)


class ClamThoughts(SimpleThoughts):
    class Factory(SimpleThoughts.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(SimpleThoughts.Factory.ChildrenFactory):
            def builders(self):
                yield from ClamThought.multiple(1, 3)


class Clam(Organism):
    class Factory(Organism.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Organism.Factory.BaseFactory):
            def __next__(self):
                return next(self.provider.plankton)

        class ChildrenFactory(Organism.Factory.ChildrenFactory):
            body_class = ClamBody
            mind_class = ClamThoughts
