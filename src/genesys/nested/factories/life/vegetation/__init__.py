from .twig import PlantCellFactory, TwigFactory
from .grass import GrassFactory, GrassBladeFactory, GrassThoughtsFactory, GrassThoughtFactory
from .trees import TreesFactory, TreeFactory, TreeThoughtsFactory, TreeThoughtFactory, LeavesFactory, LeafFactory, \
    BranchesFactory, BranchFactory, FruitsFactory, FlowersFactory, PollenFactory, TreeTrunkFactory, BarkFactory, \
    JungleTreesFactory, JungleTreeFactory, HumusFactory, NestFactory


FACTORIES = {
    'plant cell': PlantCellFactory(),
    'grass': GrassFactory(),
    'grass blade': GrassBladeFactory(),
    'grass thoughts': GrassThoughtsFactory(),
    'grass thought': GrassThoughtFactory(),
    'trees': TreesFactory(),
    'tree': TreeFactory(),
    'tree thoughts': TreeThoughtsFactory(),
    'tree thought': TreeThoughtFactory(),
    'leaves': LeavesFactory(),
    'leaf': LeafFactory(),
    'branches': BranchesFactory(),
    'branch': BranchFactory(),
    'twig': TwigFactory(),
    'fruits': FruitsFactory(),
    'flowers': FlowersFactory(),
    'pollen': PollenFactory(),
    'tree trunk': TreeTrunkFactory(),
    'bark': BarkFactory(),
    'jungle trees': JungleTreesFactory(),
    'jungle tree': JungleTreeFactory(),
    'humus': HumusFactory(),
    'nest': NestFactory(),
}