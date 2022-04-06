"""
Insects (arachnids etc too)

- Insect
- Insect Body
- Insect Thoughts
- Insect Thought
- Social Insect
- Insect Queen
- Anthill
- Beehive
- Insect Egg
- Social Insect Thoughts
- Social Insect Thought
"""
from factories.list_factory import ListFactory
from models.v5.nested_v2.models import Mind, Paper, Dirt, EggShell, EggThoughts
from models.v4.model import Model
from models.v5.life.animal_body import AnimalBody, SimpleEye, InsectLeg, InsectClaw, InsectWing, Exoskeleton, Stinger, Antenna, \
    Flesh, SoftFlesh
from models.v5.mind import SimpleThoughts, Thought
from models.v5.life.biology.organism import Organism
from models.v5.materials import OrganicMatter
from genesys.nested.data import lookups


class DataProvider:
    insect_thought = lookups.insect_thoughts
    insect = lookups.insects
    social_insect_thought = lookups.social_insect_thoughts
    social_insect = lookups.social_insects


class InsectBody(AnimalBody):
    liquid = AnimalBody.child_property(Mind)
    antennas = AnimalBody.children_property(Antenna)
    wings = AnimalBody.children_property(InsectWing)
    stinger = AnimalBody.child_property(Stinger)

    class Factory(AnimalBody.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(AnimalBody.Factory.ChildrenFactory):
            legs = property(lambda self: ListFactory([
                InsectLeg.multiple(6),
                InsectLeg.multiple(8),
            ]))
            claws = property(lambda self: ListFactory([
                InsectClaw.multiple(2),
                [],
            ]))
            wings = property(lambda self: ListFactory([
                InsectWing.multiple(2),
                InsectWing.multiple(4),
                [],
                [],
            ]))
            antennas = property(lambda self: ListFactory([
                Antenna.multiple(2),
                [],
            ]))

            def builders(self):
                yield from SimpleEye.multiple(2, 8)
                yield Mind
                yield from self.legs
                yield from self.claws
                yield Exoskeleton
                yield Stinger.probable(30)
                yield from self.wings
                yield from self.antennas
                yield Flesh


class InsectThought(Thought):
    class Factory(Thought.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Thought.Factory.BaseFactory):
            thoughts = property(lambda self: self.provider.insect_thought)


class InsectThoughts(SimpleThoughts):
    class Factory(SimpleThoughts.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(SimpleThoughts.Factory.ChildrenFactory):
            def builders(self):
                yield from InsectThought.multiple(2, 3)


class Insect(Organism):
    class Factory(Organism.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Organism.Factory.BaseFactory):
            def __next__(self):
                return next(self.provider.insect)

        class ChildrenFactory(Organism.Factory.ChildrenFactory):
            body_class = InsectBody
            mind_class = InsectThoughts


class SocialInsectThought(Thought):
    class Factory(Thought.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Thought.Factory.BaseFactory):
            thoughts = property(lambda self: self.provider.social_insect_thought)


class SocialInsectThoughts(SimpleThoughts):
    class Factory(SimpleThoughts.Factory):
        data_provider_class = DataProvider

        class ChildrenFactory(SimpleThoughts.Factory.ChildrenFactory):
            def builders(self):
                yield from SocialInsectThought.multiple(1, 2)


class SocialInsect(Insect):
    class Factory(Insect.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Insect.Factory.BaseFactory):
            def __next__(self):
                return next(self.provider.social_insect)

        class ChildrenFactory(Insect.Factory.ChildrenFactory):
            body_class = InsectBody
            mind_class = SocialInsectThoughts


class InsectQueen(SocialInsect):
    default_name = 'queen'


class InsectEgg(Model):
    class Factory(Model.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Model.Factory.BaseFactory):
            def __next__(self):
                return next(self.provider.anthill)

        class ChildrenFactory(Model.Factory.ChildrenFactory):
            def builders(self):
                yield EggThoughts
                yield EggShell
                yield SoftFlesh
                yield OrganicMatter


class Hive(Model):
    insects = AnimalBody.children_property(Insect)
    queen = AnimalBody.child_property(InsectQueen)
    eggs = AnimalBody.children_property(InsectEgg)
    hive = AnimalBody.children_property(Dirt, Paper)

    class Factory(Model.Factory):
        class ChildrenFactory(Model.Factory.ChildrenFactory):
            def builders(self):
                yield from SocialInsect.multiple(10, 30)
                yield InsectQueen
                yield from InsectEgg.multiple(2, 10)


class Anthill(Hive):
    class Factory(Model.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Model.Factory.BaseFactory):
            def __next__(self):
                return next(self.provider.anthill)

        class ChildrenFactory(Model.Factory.ChildrenFactory):
            def builders(self):
                yield from super().builders()
                yield Dirt


class Beehive(Model):
    class Factory(Model.Factory):
        data_provider_class = DataProvider

        class BaseFactory(Model.Factory.BaseFactory):
            def __next__(self):
                return next(self.provider.beehive)

        class ChildrenFactory(Model.Factory.ChildrenFactory):
            def builders(self):
                yield from super().builders()
                yield Paper
