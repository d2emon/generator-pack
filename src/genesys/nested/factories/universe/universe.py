from generated import universe
from ..factory import Factory
from .galaxy import GalaxyFactory


class SuperclusterFactory(Factory):
    default_model = universe.Supercluster

    def children(self):
        yield from GalaxyFactory().multiple(10, 30)


class UniverseFactory(Factory):
    default_model = universe.Universe

    def children(self):
        yield from SuperclusterFactory().multiple(10, 30)


class MultiverseFactory(Factory):
    default_model = universe.Multiverse

    # ["multiverse","lasagnaverse","doughnutverse","towelverse","baconverse","sharkverse","nestedverse","tastyverse",
    # "upverse","downverse","layerverse","clusterverse","metaverse","quantiverse","paraverse","epiverse","alterverse",
    # "hypoverse","dimensioverse","planiverse","pluriverse","polyverse","maniverse","stackoverse","antiverse",
    # "superverse","upperverse","maxiverse","megaverse","babyverse","tinyverse","retroverse","ultraverse","topoverse",
    # "otherverse","bubbleverse","esreverse","versiverse","'verse","cookieverse","grandmaverse"]

    # class DataProvider:
    #     multiverse = lookups.multiverses

    # name = property(lambda self: self.provider.multiverse)

    def children(self):
        yield from UniverseFactory().multiple(10, 30)
