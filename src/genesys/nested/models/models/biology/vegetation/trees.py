from ...unknown import Insect, Worm, Wood, Sugar, Dirt, Bird, BirdEgg, EggShell
from genesys.nested.factories.thing_builder import ThingBuilder
from genesys.nested.models import Model
from .cells import PlantCell
from ...chemistry import Dew, OrganicMatter


class Twig(Model):
    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield PlantCell


class TreeThought(Model):
    class Factory(ThingBuilder):
        class DataProvider:
            grass_thought = [
                'Well. What is this all about.', 'So. What\'s the hurry?', 'Whoah. Slow down.',
                'Do like a tree. And go away.', 'I seen some things.', 'They\'re coming.', 'We know.',
                'We\'ve been watching you for hundreds of years.', 'Do you have any idea how old I am?',
                'Yes. I remember you. I remember all of you.'
            ]

        class BaseFactory(ThingBuilder.BaseFactory):
            data = property(lambda self: self.provider.grass_thought)

        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield None


class TreeThoughts(Model):
    default_name = 'thoughts'

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield from TreeThought.multiple(1)


class Bark(Model):
    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield Insect.probable(10)
                yield Worm.probable(10)
                yield Wood


class TreeTrunk(Model):
    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield Insect.probable(4)
                yield Wood
                yield Bark


class Leaf(Model):
    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield Dew.probable(6)
                yield Insect.probable(6)
                yield PlantCell


class Leaves(Model):
    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield from Leaf.multiple(50, 100)


class Branch(Model):
    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield Insect.probable(6)
                yield Leaf.probable(10)
                yield PlantCell


class Branches(Model):
    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield from Branch.multiple(10, 30)


class Fruits(Model):
    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield Worm.probable(5)
                yield PlantCell
                yield Sugar


class Pollen(Model):
    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield PlantCell
                yield Sugar


class Flowers(Model):
    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield Insect.probable(5)
                yield PlantCell
                yield Pollen


class Tree(Model):
    class Factory(ThingBuilder):
        class DataProvider:
            tree = [
                'larch', 'fir', 'oak', 'birch', 'pine', 'sequoia', 'cedar', 'spruce', 'ash', 'poplar', 'elm',
                'sycamore',
                'willow', 'mahogany', 'laurel', 'orange tree', 'lemon tree', 'palm tree', 'coconut tree', 'pear tree',
                'apple tree', 'walnut tree', 'olive tree',
            ]

        class BaseFactory(ThingBuilder.BaseFactory):
            data = property(lambda self: self.provider.grass_thought)

        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield TreeThoughts.probable(2)
                yield TreeTrunk
                yield Branches
                yield Leaves
                yield Nest.probable(5)
                yield Nest.probable(2)
                yield Fruits.probable(20)
                yield Flowers.probable(20)


class Trees(Model):
    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield from Tree.multiple(20, 50)


class JungleTree(Model):
    default_name = 'tree'


class JungleTrees(Model):
    default_name = 'trees'

    class Factory(ThingBuilder):
        class ChildrenFactory(Trees.ChildrenFactory):
            def builders(self):
                yield from JungleTree.multiple(20, 150)


class Humus(Model):
    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield from Insect.multiple(0, 3)
                yield from Worm.multiple(0, 3)
                yield from Twig.multiple(0, 3)
                yield from Leaf.multiple(0, 6)
                yield OrganicMatter
                yield Dirt


class Nest(Model):
    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield Bird.probable(50)
                yield EggShell.probable(20)
                yield from BirdEgg.multiple(0, 6)
                yield from Twig.multiple(6, 12)
