from v1.fng.genesys.name_factory import NameFactory, ComplexNameFactory
from v1.fng.genesys.name import Name
from v1.fng.genesys.data_block import load_data


names1 = ["b", "bl", "br", "c", "chr", "cl", "cr", "d", "dr", "f", "g", "gl", "gr", "h", "j", "k", "kl", "kr", "m", "n",
          "p", "ph", "ps", "pr", "r", "rh", "s", "sm", "sc", "t", "th", "v", "x", "", "", "", "", "", "", ""]
names2 = ["a", "e", "i", "o", "u", "y", "ou", "ei", "oe", "ao", "io", "eo", "a", "e", "i", "o", "u"]
names3 = ["c", "d", "k", "l", "m", "r", "s", "t", "x", "", "", "", "", "", "", "", "", "", "", ""]
names4 = ["c", "d", "k", "l", "m", "r", "s", "t", "x", "nd", "nt", "lk", "lc", "ll", "ndr", "br", "st", "ch", "br",
          "cl", "ph", "rm", "pp", "pt", "rp", "nth", "th", "rg", "thr", "dm", "lth", "lc", "chr", "phn", "dr", "mn",
          "rr", "rrh"]
names5 = ["a", "e", "i", "o", "u", "y", "", "", "", "", "", "", "", "", ""]
names6 = ["adia", "ameia", "anta", "asca", "cabe", "ce", "cleia", "cyone", "cyra", "da", "dae", "dia", "dice", "dora",
          "enice", "esia", "estra", "estris", "gea", "gone", "haedra", "hyia", "ippe", "isbe", "ises", "leia", "lene",
          "lete", "liope", "lipe", "lyte", "mache", "meia", "nache", "nara", "neira", "nestra", "nia", "nippe", "noe",
          "nousa", "ope", "padia", "pedo", "peia", "pesia", "phale", "pyle", "pyte", "rera", "reto", "roe", "scyra",
          "ses", "sippe", "sose", "tane", "thippe", "thoe", "thya", "thye", "thyia", "ybe", "yche", "yle", "yme", "yne",
          "yope", "yrbe", "ytie"]


# Models

class AmazonName(Name):
    @property
    def value(self):
        return f"{self.items[1]}{self.items[2]}{self.items[3]}{self.items[4]}{self.items[5]}"


class AmazonName1(AmazonName):
    pass


class AmazonName2(AmazonName):
    pass


# Factory

class AmazonNameFactory(ComplexNameFactory):
    """Amazon Name Factory"""

    class AmazonNameFactory1(NameFactory):
        name_class = AmazonName1
        blocks_map = {
            1: 1,
            2: 2,
            3: 3,
            4: 5,
            5: 6,
        }

    class AmazonNameFactory2(NameFactory):
        name_class = AmazonName2
        blocks_map = {
            1: 1,
            2: 2,
            3: 3,
            4: 2,
            5: 6,
        }

    description = """The names are heavily based on the Amazons of ancient Greece, so while most names will have various
        melodic sounds, most names do tend to have a Greek feel to it.

        The Amazons are female warriors who lived in an all-female society. They're known for their strength and power,
        their way of life, and their victories gave them a legendary status. The term Amazon was soon synonymous with
        female warrior.
        Men weren't allowed in the Amazon towns, with the exception of once a year to make sure their tribe didn't go
        extinct.
        
        The Amazons have been depicted in many modern works of fiction, and their legendary status usually accompanies
        them, like Wonder Woman.
        Even in these modern versions, the Amazon women tend to have Greek or Greek sounding names, like Hippolyta, the
        queen of the Amazons and mother of Diana, otherwise known as Wonder Woman."""
    factory_classes = {
        0: AmazonNameFactory1,
        1: AmazonNameFactory2,
    }
    default_blocks = load_data({
        1: names1,
        2: names2,
        3: names3,
        4: names4,
        5: names5,
        6: names6,
    })

    def get_factory(self, factory_id):
        if factory_id < 50:
            return self.factories[0]
        else:
            return self.factories[1]
