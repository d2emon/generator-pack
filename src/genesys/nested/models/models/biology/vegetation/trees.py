from ...unknown import Insect, Worm, Wood, Sugar, Dirt, Bird, BirdEgg, EggShell
from genesys.nested.factories.thing_builder import ThingBuilder
from genesys.nested.models import Model
from .cells import PlantCell
from ..brain import Thoughts, Thought
from ...chemistry import Dew, OrganicMatter


class Twig(Model):
    cells = Model.child_property(PlantCell)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield PlantCell


class Nest(Model):
    bird = Model.child_property(Bird)
    eggs = Model.children_property(EggShell, BirdEgg)
    twigs = Model.children_property(Twig)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield Bird.probable(50)
                yield EggShell.probable(20)
                yield from BirdEgg.multiple(0, 6)
                yield from Twig.multiple(6, 12)


class TreeThought(Thought):
    class Factory(Thought.Factory):
        class DataProvider:
            grass_thought = [
                'Well. What is this all about.', 'So. What\'s the hurry?', 'Whoah. Slow down.',
                'Do like a tree. And go away.', 'I seen some things.', 'They\'re coming.', 'We know.',
                'We\'ve been watching you for hundreds of years.', 'Do you have any idea how old I am?',
                'Yes. I remember you. I remember all of you.'
            ]

        class BaseFactory(Thought.Factory.BaseFactory):
            data = property(lambda self: self.provider.grass_thought)

        class ChildrenFactory(Thought.Factory.ChildrenFactory):
            def builders(self):
                yield None


class TreeThoughts(Thoughts):
    default_name = 'thoughts'

    class Factory(Thoughts.Factory):
        class ChildrenFactory(Thoughts.Factory.ChildrenFactory):
            def builders(self):
                yield from TreeThought.multiple(1)


class TreePart(Model):
    dew = Model.child_property(Dew)
    worms = Model.children_property(Worm)
    insects = Model.children_property(Insect)

    class Factory(ThingBuilder):
        pass


class Bark(TreePart):
    wood = Model.child_property(Wood)

    class Factory(TreePart.Factory):
        class ChildrenFactory(TreePart.Factory.ChildrenFactory):
            def builders(self):
                yield Insect.probable(10)
                yield Worm.probable(10)
                yield Wood


class TreeTrunk(TreePart):
    bark = Model.child_property(Bark)
    wood = Model.child_property(Wood)

    class Factory(TreePart.Factory):
        class ChildrenFactory(TreePart.Factory.ChildrenFactory):
            def builders(self):
                yield Insect.probable(4)
                yield Wood
                yield Bark


class Leaf(TreePart):
    cells = Model.child_property(PlantCell)

    class Factory(TreePart.Factory):
        class ChildrenFactory(TreePart.Factory.ChildrenFactory):
            def builders(self):
                yield Dew.probable(6)
                yield Insect.probable(6)
                yield PlantCell


class Leaves(Model):
    leaves = Model.children_property(Leaf)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield from Leaf.multiple(50, 100)


class Branch(TreePart):
    cells = Model.child_property(PlantCell)
    leaves = Model.children_property(Leaf)

    class Factory(TreePart.Factory):
        class ChildrenFactory(TreePart.Factory.ChildrenFactory):
            def builders(self):
                yield Insect.probable(6)
                yield Leaf.probable(10)
                yield PlantCell


class Branches(Model):
    branches = Model.children_property(Branch)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield from Branch.multiple(10, 30)


class Fruits(TreePart):
    cells = Model.child_property(PlantCell)
    sugar = Model.child_property(Sugar)

    class Factory(TreePart.Factory):
        class ChildrenFactory(TreePart.Factory.ChildrenFactory):
            def builders(self):
                yield Worm.probable(5)
                yield PlantCell
                yield Sugar


class Pollen(Model):
    cells = Model.child_property(PlantCell)
    sugar = Model.child_property(Sugar)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield PlantCell
                yield Sugar


class Flowers(TreePart):
    cells = Model.child_property(PlantCell)
    pollen = Model.child_property(Pollen)

    class Factory(TreePart.Factory):
        class ChildrenFactory(TreePart.Factory.ChildrenFactory):
            def builders(self):
                yield Insect.probable(5)
                yield PlantCell
                yield Pollen


class Tree(Model):
    thoughts = Model.child_property(Thoughts)
    trunk = Model.child_property(TreeTrunk)
    branches = Model.child_property(Branches)
    leaves = Model.child_property(Leaves)
    nests = Model.children_property(Nest)
    fruits = Model.child_property(Fruits)
    flowers = Model.child_property(Flowers)

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
    trees = Model.children_property(Tree)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield from Tree.multiple(20, 50)


class JungleTree(Tree):
    default_name = 'tree'


class JungleTrees(Trees):
    default_name = 'trees'

    class Factory(Trees.Factory):
        class ChildrenFactory(Trees.Factory.ChildrenFactory):
            def builders(self):
                yield from JungleTree.multiple(20, 150)


class Humus(Model):
    insects = Model.children_property(Insect)
    worms = Model.children_property(Worm)
    twigs = Model.children_property(Twig)
    leaves = Model.children_property(Leaf)
    organic = Model.child_property(OrganicMatter)
    dirt = Model.child_property(Dirt)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield from Insect.multiple(0, 3)
                yield from Worm.multiple(0, 3)
                yield from Twig.multiple(0, 3)
                yield from Leaf.multiple(0, 6)
                yield OrganicMatter
                yield Dirt
