from factories.nested_factory import NestedFactory
from generated import universe
from .galaxy import GalaxyFactory


class SuperclusterFactory(NestedFactory):
    default_model = universe.Supercluster

    def children(self):
        yield from GalaxyFactory().multiple(10, 30)


class UniverseFactory(NestedFactory):
    default_model = universe.Universe

    def children(self):
        yield from SuperclusterFactory().multiple(10, 30)


class MultiverseFactory(NestedFactory):
    default_model = universe.Multiverse
    names = [
        "multiverse", "lasagnaverse", "doughnutverse", "towelverse", "baconverse", "sharkverse", "nestedverse",
        "tastyverse", "upverse", "downverse", "layerverse", "clusterverse", "metaverse", "quantiverse", "paraverse",
        "epiverse", "alterverse", "hypoverse", "dimensioverse", "planiverse", "pluriverse", "polyverse", "maniverse",
        "stackoverse", "antiverse", "superverse", "upperverse", "maxiverse", "megaverse", "babyverse", "tinyverse",
        "retroverse", "ultraverse", "topoverse", "otherverse", "bubbleverse", "esreverse", "versiverse", "'verse",
        "cookieverse", "grandmaverse",
    ]

    def generate_name(self):
        return self.select_item(*self.names)

    def children(self):
        yield from UniverseFactory().multiple(10, 30)
