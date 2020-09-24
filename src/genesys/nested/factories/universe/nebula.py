from generated import universe
from ..factory import Factory
from ..materials import MoleculeFactory, SteamFactory, AmmoniaFactory
from .star import SingleStarFactory


class InterstellarCloudFactory(Factory):
    default_model = universe.InterstellarCloud

    # class DataProvider:
    #     interstellar_cloud = lookups.interstellar_clouds

    # name = property(lambda self: self.provider.interstellar_cloud)

    # ["a bright pink","a faint","a fading","a pale","a fluo","a glowing","a green","a bright green","a dark brown",
    # "a brooding","a magenta","a bright red","a dark red","a blueish","a deep blue","a turquoise","a teal","a golden",
    # "a multicolored","a silver","a dramatic","a luminous","a colossal","a purple","a gold-trimmed","an opaline",
    # "a silvery","a shimmering"],
    # [" "],
    # ["interstellar cloud"]

    def children(self):
        yield MoleculeFactory.from_elements('He')
        yield MoleculeFactory.from_elements('H')
        yield MoleculeFactory.from_elements('C').probable(80)
        yield SteamFactory().probable(5)
        yield AmmoniaFactory().probable(5)
        yield MoleculeFactory.from_elements('N').probable(5)
        yield MoleculeFactory.from_elements('Fe').probable(5)
        yield MoleculeFactory.from_elements('S').probable(5)
        yield MoleculeFactory.from_elements('O').probable(15)


class NebulaFactory(Factory):
    default_model = universe.Nebula

    @classmethod
    def life(cls):
        # "galactic life,15%"
        # yield NebulaLife
        yield None

    @classmethod
    def stars(cls):
        yield SingleStarFactory().probable(2)
        yield SingleStarFactory().probable(2)
        yield SingleStarFactory().probable(2)

    @classmethod
    def clouds(cls):
        yield from InterstellarCloudFactory().multiple(1, 6)

    def children(self):
        yield from self.life()
        yield from self.stars()
        yield from self.clouds()
