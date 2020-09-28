"""
Cetaceans

- Cetacean
- Cetacean Thoughts
- Cetacean Thought
- Cetacean Head
- Cetacean Body
"""
from ..animal_body import AnimalBody, Flesh, CetaceanFin, CetaceanFlipper, Tail
from generated.life.body.body import Head, Mouth, Eye, Skin, Skull
from generated.mind import SimpleThoughts, Thought
from ..organism import Organism
from genesys.nested.data import lookups


class DataProvider:
    cetacean_thought = lookups.cetacean_thoughts
    cetacean = lookups.cetaceans


class CetaceanHead(Head):
    default_name = 'head'

    class Factory(AnimalBody.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(AnimalBody.Factory.ChildrenFactory):
            def builders(self):
                yield Mouth
                yield from Eye.multiple(2)
                yield Skull
                yield Skin


class CetaceanBody(AnimalBody):
    head = AnimalBody.child_property(Head)

    class Factory(AnimalBody.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(AnimalBody.Factory.ChildrenFactory):
            def builders(self):
                yield CetaceanHead
                yield Skin
                yield from CetaceanFlipper.multiple(2)
                yield from CetaceanFin.multiple(1, 2)
                yield Tail
                yield Flesh


class CetaceanThought(Thought):
    class Factory(Thought.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Thought.Factory.BaseFactory):
            thoughts = property(lambda self: self.provider.cetacean_thought)


class CetaceanThoughts(SimpleThoughts):
    class Factory(SimpleThoughts.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(SimpleThoughts.Factory.ChildrenFactory):
            def builders(self):
                yield from CetaceanThought.multiple(1, 2)


class Cetacean(Organism):
    class Factory(Organism.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Organism.Factory.BaseFactory):
            def __next__(self):
                return next(self.provider.cetacean)

        class ChildrenFactory(Organism.Factory.ChildrenFactory):
            body_class = CetaceanBody
            mind_class = CetaceanThoughts
