"""
Sharks

- Shark
- Shark Thoughts
- Shark Thought
"""
from .fish import Fish, FishBody, FishThoughts, FishThought
from genesys.nested.data import lookups


class DataProvider:
    shark_thought = lookups.shark_thoughts
    shark = lookups.sharks


class SharkThought(FishThought):
    class Factory(FishThought.Factory):
        data_provider_class = DataProvider

        class BaseFactory(FishThought.Factory.BaseFactory):
            thoughts = property(lambda self: self.provider.shark_thought)


class SharkThoughts(FishThoughts):
    class Factory(FishThoughts.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(FishThoughts.Factory.ChildrenFactory):
            def builders(self):
                yield from SharkThought.multiple(1, 2)


class Shark(Fish):
    class Factory(Fish.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Fish.Factory.BaseFactory):
            def __next__(self):
                return next(self.provider.shark)

        class ChildrenFactory(Fish.Factory.ChildrenFactory):
            body_class = FishBody
            mind_class = SharkThoughts
