from generated import life
from ...factory import Factory
from ...materials import DewFactory, OrganicFactory
from ...mind import ThoughtFactory, ThoughtsFactory
from .twig import TwigFactory


class BarkFactory(Factory):
    default_model = life.Bark

    def children(self):
        # "insect,10%"
        # "worm,10%"
        # "wood"
        yield None


class TreeTrunkFactory(Factory):
    default_model = life.TreeTrunk

    def children(self):
        # "insect,4%"
        # "wood"
        yield BarkFactory()


class FruitsFactory(TwigFactory):
    default_model = life.Fruits

    def children(self):
        # worm, 5%
        # sugar
        yield from super().children()


class PollenFactory(TwigFactory):
    default_model = life.Pollen

    def children(self):
        # sugar
        yield from super().children()


class FlowersFactory(TwigFactory):
    default_model = life.Flowers

    def children(self):
        # insect, 5%
        yield PollenFactory()
        yield from super().children()


class LeafFactory(TwigFactory):
    default_model = life.Leaf

    def children(self):
        yield DewFactory().probable(6)
        # insect, 6%
        yield from super().children()


class LeavesFactory(Factory):
    default_model = life.Leaves

    def children(self):
        yield from LeafFactory().multiple(50, 100)


class BranchFactory(TwigFactory):
    default_model = life.Branch

    def children(self):
        # insect, 6%
        yield LeafFactory().probable(10)
        yield from super().children()


class BranchesFactory(Factory):
    default_model = life.Branches

    def children(self):
        yield from BranchFactory().multiple(10, 30)


class TreeThoughtFactory(ThoughtFactory):
    names = [
        "Well. What is this all about.", "So. What's the hurry?", "Whoah. Slow down.", "Do like a tree. And go away.",
        "I seen some things.", "They're coming.", "We know.", "We've been watching you for hundreds of years.",
        "Do you have any idea how old I am?", "Yes. I remember you. I remember all of you.",
    ]

    def generate_name(self):
        return self.select_item(*self.names)


class TreeThoughtsFactory(ThoughtsFactory):
    def children(self):
        yield from TreeThoughtFactory().multiple(1)


class TreeFactory(Factory):
    default_model = life.Tree
    names = [
        "larch", "fir", "oak", "birch", "pine", "sequoia", "cedar", "spruce", "ash", "poplar", "elm", "sycamore",
        "willow", "mahogany", "laurel", "orange tree", "lemon tree", "palm tree", "coconut tree", "pear tree",
        "apple tree", "walnut tree", "olive tree",
    ]

    def generate_name(self):
        return self.select_item(*self.names)

    def children(self):
        yield TreeThoughtsFactory().probable(2)
        yield TreeTrunkFactory()
        yield BranchesFactory()
        yield LeavesFactory()
        # "nest,5%"
        # "nest,2%"
        yield FruitsFactory().probable(20)
        yield FlowersFactory().probable(20)


class TreesFactory(Factory):
    default_model = life.Trees

    def children(self):
        yield from TreeFactory().multiple(20, 50)


class JungleTreeFactory(TreeFactory):
    pass


class JungleTreesFactory(TreesFactory):
    default_model = life.Trees

    def children(self):
        yield from JungleTreeFactory().multiple(20, 150)


class HumusFactory(Factory):
    default_model = life.Humus

    def children(self):
        # "insect,0-3"
        # "worm,0-3"
        yield from TwigFactory().multiple(0, 3)
        yield from LeafFactory().multiple(0, 6)
        yield from OrganicFactory()
        # "dirt"
        yield from JungleTreeFactory().multiple(20, 150)


class NestFactory(Factory):
    default_model = life.Humus

    def children(self):
        # "bird,50%"
        # "egg shell,20%"
        # "bird egg,0-6"
        yield from TwigFactory().multiple(6, 12)
