from .names import Names, random_class


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


class AmazonNames(Names):
    pass


class Amazon1Names(AmazonNames):
    data = [
        names1,
        names2,
        names3,
        names5,
        names6,
    ]


class Amazon2Names(AmazonNames):
    data = [
        names1,
        names2,
        names4,
        names2,
        names6,
    ]


def amazon_selector(amazon_id):
    amazons = [
        Amazon1Names,
        Amazon2Names,
    ]
    if amazon_id < 5:
        return amazons[0]
    else:
        return amazons[1]


def generate():
    return random_class(amazon_selector).generate().title()
