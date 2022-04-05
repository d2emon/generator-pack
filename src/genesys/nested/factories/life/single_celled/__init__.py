from models.v5 import life
from ...mind import ThoughtFactory, ThoughtsFactory, PsycheFactory
from ..cell import CellFactory
from ..animals.animal import AnimalFactory


class BacteriaBodyFactory(CellFactory):
    pass


class BacteriaThoughtFactory(ThoughtFactory):
    thoughts = [
        "#wow", "#wow okay", "#i can't even", "#okay", "#me", "#yes", "#what", "#how", "#delicious", "#seriously",
        "#but seriously tho", "#germ life", "#mitosis", "#meiosis", "#nucleus", "#cytoplasm",
        "#single-celled and ready to mingle", "#lame", "#meh", "#i don't wanna talk about it", "#eukaryote privilege",
        "#protist scum", "#squirm", "#protist patriarchy", "#osmosis", "#one cell of a guy",
    ]


class BacteriaThoughtsFactory(ThoughtsFactory):
    black_hole_probability = 0

    @classmethod
    def thoughts(cls):
        yield BacteriaThoughtFactory().multiple(1)


class BacteriaPsycheFactory(PsycheFactory):
    @property
    def thoughts_factory(self):
        return BacteriaThoughtsFactory()

    @property
    def memories_factory(self):
        return None


class BacteriaFactory(AnimalFactory):
    default_model = life.Bacteria
    names = [
        "pico", "nitro", "sulfuro", "oxy", "toxi", "micro", "nano", "proto", "archi", "ferro", "mono", "poly",
        "schizo", "myxo", "hydro", "noo", "zoo", "phyto", "aqui", "acido", "cyano", "chloro", "chromo", "fibro",
        "osteo", "spiro", "bacillo", "flagello", "helio", "anaero", "photo", "litho", "methano", "cerebro", "cephalo",
        "brachio", "plasmo", "ethylo",
    ]
    bacteria_types = ["amoeba", "bacteria", "virus"]

    def generate_name(self):
        return f'{self.select_item(*self.names)}{self.select_item(*self.bacteria_types)}'

    @property
    def body_factory(self):
        return BacteriaBodyFactory()

    @property
    def psyche_factory(self):
        return BacteriaPsycheFactory()
