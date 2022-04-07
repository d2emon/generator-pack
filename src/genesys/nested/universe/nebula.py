from models.universe.nebula import Nebula, InterstellarCloud
from factories.nested_factory import NestedFactory
# from ..life import NebulaLifeFactory
# from ..materials import MoleculeFactory, SteamFactory, AmmoniaFactory
from .star import StarFactory


# Nebula
# InterstellarCloud


class NebulaFactory(NestedFactory):
    default_model = Nebula

    def life(self):
        # yield NebulaLifeFactory()
        yield None

    def stars(self):
        yield StarFactory.probable(2)
        yield StarFactory.probable(2)
        yield StarFactory.probable(2)
        yield None

    def clouds(self):
        yield InterstellarCloudFactory.multiple(1, 6)

    def children(self):
        yield from self.life()
        yield from self.stars()
        yield from self.clouds()


class InterstellarCloudFactory(NestedFactory):
    default_model = InterstellarCloud

    def children(self):
        # yield MoleculeFactory.from_elements('He')
        # yield MoleculeFactory.from_elements('H')
        # yield MoleculeFactory.from_elements('C').probable(80)
        # yield SteamFactory.probable(5)
        # yield AmmoniaFactory.probable(5)
        # yield MoleculeFactory.from_elements('N').probable(5)
        # yield MoleculeFactory.from_elements('Fe').probable(5)
        # yield MoleculeFactory.from_elements('S').probable(5)
        # yield MoleculeFactory.from_elements('O').probable(15)
        yield None

    def name_factory(self):
        return f"{self.select_item(*self.provider.interstellar_cloud)} interstellar cloud"


"""
new Thing("nebula",[
    "galactic life,15%",
    ####
    "star,2%",
    "star,2%",
    "star,2%",
    ####
    "interstellar cloud,1-6"
]);
new Thing("interstellar cloud",[
    "helium",
    "hydrogen",
    "carbon,80%",
    "water,5%",
    "ammonia,5%",
    "nitrogen,5%",
    "iron,5%",
    "sulfur,5%",
    "oxygen,15%"
],[
    [
        "a bright pink","a faint","a fading","a pale","a fluo","a glowing","a green","a bright green",
        "a dark brown","a brooding","a magenta","a bright red","a dark red","a blueish","a deep blue",
        "a turquoise","a teal","a golden","a multicolored","a silver","a dramatic","a luminous","a colossal",
        "a purple","a gold-trimmed","an opaline","a silvery","a shimmering"
    ],
    [" "],
    ["interstellar cloud"]
]);
"""