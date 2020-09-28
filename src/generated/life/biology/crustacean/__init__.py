"""
Crustaceans

- Crustacean
- Crustacean Body
- Crustacean Thoughts
- Crustacean Thought
"""
from generated.nested_v2.models import Mind
from ..animal_body import AnimalBody, SimpleEye, SoftFlesh, CrustaceanLeg, CrustaceanClaw, CrustaceanShell
from ..mind import SimpleThoughts, Thought
from ..organism import Organism
from genesys.nested.data import lookups


class DataProvider:
    crustacean_thought = lookups.crustacean_thoughts
    crustacean = lookups.crustacean


class CrustaceanBody(AnimalBody):
    liquid = AnimalBody.child_property(Mind)

    class Factory(AnimalBody.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(AnimalBody.Factory.ChildrenFactory):
            def builders(self):
                yield from SimpleEye.multiple(2, 6)
                yield Mind
                yield from CrustaceanLeg.multiple(6, 8)
                yield from CrustaceanClaw.multiple(2)
                yield CrustaceanShell
                yield SoftFlesh


class CrustaceanThought(Thought):
    class Factory(Thought.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Thought.Factory.BaseFactory):
            thoughts = property(lambda self: self.provider.crustacean_thought)


class CrustaceanThoughts(SimpleThoughts):
    class Factory(SimpleThoughts.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(SimpleThoughts.Factory.ChildrenFactory):
            def builders(self):
                yield from CrustaceanThought.multiple(2, 3)


class Crustacean(Organism):
    class Factory(Organism.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Organism.Factory.BaseFactory):
            def __next__(self):
                return next(self.provider.crustacean)

        class ChildrenFactory(Organism.Factory.ChildrenFactory):
            body_class = CrustaceanBody
            mind_class = CrustaceanThoughts
