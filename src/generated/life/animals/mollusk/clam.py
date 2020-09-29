"""
Clams

- Clam
- Clam Body
- Clam Thoughts
- Clam Thought
"""
from generated.nested_v2.models import Mind
from .mollusk import Mollusk, MolluskBody, MolluskThoughts, MolluskThought
from generated.life.animal_body import SoftFlesh, ClamShell
from genesys.nested.data import lookups


class DataProvider:
    clam_thought = lookups.clam_thoughts
    clam = lookups.clams


class ClamBody(MolluskBody):
    shell = MolluskBody.children_property(ClamShell)
    liquid = MolluskBody.child_property(Mind)

    class Factory(MolluskBody.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(MolluskBody.Factory.ChildrenFactory):
            def builders(self):
                yield ClamShell
                yield ClamShell
                yield Mind
                yield SoftFlesh


class ClamThought(MolluskThought):
    class Factory(MolluskThought.Factory):
        data_provider_class = DataProvider

        class BaseFactory(MolluskThought.Factory.BaseFactory):
            thoughts = property(lambda self: self.provider.clam_thought)


class ClamThoughts(MolluskThoughts):
    class Factory(MolluskThoughts.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(MolluskThoughts.Factory.ChildrenFactory):
            def builders(self):
                yield from ClamThought.multiple(1, 3)


class Clam(Mollusk):
    class Factory(Mollusk.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Mollusk.Factory.BaseFactory):
            def __next__(self):
                return next(self.provider.plankton)

        class ChildrenFactory(Mollusk.Factory.ChildrenFactory):
            body_class = ClamBody
            mind_class = ClamThoughts
