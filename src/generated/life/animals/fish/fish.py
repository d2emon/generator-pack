"""
Fish

- Fish
- Fish Body
- Fish Thoughts
- Fish Thought
"""
from generated.nested_v2.models import Mind
from generated.life.biology.animal_body import AnimalBody, SimpleEye, FishFin, FishSkin, FishTail, Flesh
from generated.life.body.body import Mouth
from generated.mind import SimpleThoughts, Thought
from generated.life.biology.organism import Organism
from generated.life.animals.worm import Worm
from genesys.nested.data import lookups


class DataProvider:
    fish_thought = lookups.fish_thoughts
    fish = lookups.fishes


class FishBody(AnimalBody):
    liquid = AnimalBody.child_property(Mind)
    parasite = AnimalBody.children_property(Worm)

    class Factory(AnimalBody.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(AnimalBody.Factory.ChildrenFactory):
            def builders(self):
                yield from SimpleEye.multiple(2)
                yield Mind
                yield Mouth
                yield from FishFin.multiple(2, 6)
                yield FishSkin
                yield FishTail
                yield Flesh
                yield Worm.probable(5)


class FishThought(Thought):
    class Factory(Thought.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Thought.Factory.BaseFactory):
            thoughts = property(lambda self: self.provider.fish_thought)


class FishThoughts(SimpleThoughts):
    class Factory(SimpleThoughts.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(SimpleThoughts.Factory.ChildrenFactory):
            def builders(self):
                yield from FishThought.multiple(2, 3)


class Fish(Organism):
    class Factory(Organism.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Organism.Factory.BaseFactory):
            def __next__(self):
                return next(self.provider.fish)

        class ChildrenFactory(Organism.Factory.ChildrenFactory):
            body_class = FishBody
            mind_class = FishThoughts
