from v1.fng.genesys.name_factory import NameFactory, ComplexNameFactory
from v1.fng.genesys.name import Name
from v1.fng.genesys.data_block import load_data
from v1.fng.genesys.validators import item_is_not_unique, item_equals, generate_while


# Models

class AlienName(Name):
    @property
    def value(self):
        return f"{self.items[1]}{self.items[2]}{self.items[3]}{self.items[4]}{self.items[5]}"


class AlienName1(AlienName):
    pass


class AlienName2(AlienName):
    pass


class AlienName3(AlienName):
    pass


# Factory

class AlienNameFactory(ComplexNameFactory):
    """Alien Species Name Factory"""

    class AlienNameFactory1(NameFactory):
        description = """The first 4 names have a much higher chance of having a more guttural sound to them, ideal for
            the stronger and brutish looking aliens."""
        name_class = AlienName1
        blocks_map = {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
        }

        def validate(self, items):
            items[3] = generate_while(
                items[3],
                item_is_not_unique([items[1], items[5]]),
                self.blocks[3],
            )
            items[4] = self.blocks[4][0] if str(items[3]) == '' else generate_while(
                items[4],
                item_equals(''),
                self.blocks[3],
            )

            return items

    class AlienNameFactory2(NameFactory):
        description = """The next 3 names have a much higher chance of having a more melodic sound to them, making them
            ideal for the softer and gentle looking aliens."""
        name_class = AlienName2
        blocks_map = {
            1: 6,
            2: 7,
            3: 8,
            4: 10,
            5: 11,
        }

        def validate(self, items):
            items[3] = generate_while(
                items[3],
                item_is_not_unique([items[1], items[5]]),
                self.blocks[8],
            )

            return items

    class AlienNameFactory3(NameFactory):
        description = """The last 3 names can sound both guttural and melodic and anything in between. These names are
            more randomized than the previous 2 types and unlike the other 2 types, these aren't always easy to
            pronounce in English."""
        name_class = AlienName3
        blocks_map = {
            1: 12,
            2: 13,
            3: 14,
            4: 15,
            5: 16,
        }

        def validate(self, items):
            items[3] = generate_while(
                items[3],
                item_is_not_unique([items[1], items[5]]),
                self.blocks[14],
            )
            items[4] = self.blocks[15][0] if str(items[3]) == '' else generate_while(
                items[4],
                item_equals(''),
                self.blocks[15],
            )

            return items

    description = """It's both easy and difficult to create alien names, as they can be anything in any language. But
        the names have to sound like a good fit for the species you've invented, so I've tried to make sure many
        different types of names can be generated, but they generally fit in 3 different categories."""
    factory_classes = {
        0: AlienNameFactory1,
        1: AlienNameFactory2,
        2: AlienNameFactory3,
    }
    default_blocks = load_data({
        1: ("br", "c", "cr", "dr", "g", "gh", "gr", "k", "kh", "kr", "n", "q", "qh", "sc", "scr", "str", "st", "t",
            "tr", "thr", "v", "vr", "x", "z", "", "", "", "", ""),
        2: ("ae", "aa", "ai", "au", "uu", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u",
            "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u"),
        3: ("c", "k", "n", "q", "t", "v", "x", "z", "c", "cc", "cr", "cz", "dr", "gr", "gn", "gm", "gv", "gz", "k",
            "kk", "kn", "kr", "kt", "kv", "kz", "lg", "lk", "lq", "lx", "lz", "nc", "ndr", "nkr", "ngr", "nk", "nq",
            "nqr", "nz", "q", "qr", "qn", "rc", "rg", "rk", "rkr", "rq", "rqr", "sc", "sq", "str", "t", "v", "vr", "x",
            "z", "q'", "k'", "rr", "r'", "t'", "tt", "vv", "v'", "x'", "z'", "", "", "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", ""),
        4: ("", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "oi", "ie", "ai", "ei", "eo",
            "ui"),
        5: ("d", "ds", "k", "ks", "l", "ls", "n", "ns", "ts", "x"),

        6: ("b", "bh", "ch", "d", "dh", "f", "h", "l", "m", "n", "ph", "r", "s", "sh", "th", "v", "y", "z", "", "", "",
            "", "", "", "", "", ""),
        7: ("ae", "ai", "ee", "ei", "ie", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u",
            "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u"),
        8: ("c", "d", "g", "h", "l", "m", "n", "r", "s", "v", "z", "c", "ch", "d", "dd", "dh", "g", "gn", "h", "hl",
            "hm", "hn", "hr", "l", "ld", "ldr", "lg", "lgr", "lk", "ll", "lm", "ln", "lph", "lt", "lv", "lz", "m", "mm",
            "mn", "mh", "mph", "n", "nd", "nn", "ng", "nk", "nph", "nz", "ph", "phr", "r", "rn", "rl", "rz", "s", "ss",
            "sl", "sn", "st", "v", "z", "s'", "l'", "n'", "m'", "f'", "h'"),
        10: ("a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "oi", "ie", "ai", "ea", "ae"),
        11: ("", "", "", "", "d", "ds", "h", "l", "ll", "n", "ns", "r", "rs", "s", "t", "th"),

        12: ("b", "bh", "br", "c", "ch", "cr", "d", "dh", "dr", "f", "g", "gh", "gr", "h", "k", "kh", "kr", "l", "m",
             "n", "q", "qh", "ph", "r", "s", "sc", "scr", "sh", "st", "str", "t", "th", "thr", "tr", "v", "vr", "y",
             "x", "z", "", "", "", "", "", "", ""),
        13: ("ae", "aa", "ai", "au", "ee", "ei", "ie", "uu", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e",
             "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u"),
        14: ("c", "d", "g", "h", "k", "l", "m", "n", "q", "r", "s", "t", "v", "z", "c", "d", "g", "h", "k", "l", "m",
             "n", "q", "r", "s", "t", "v", "z", "c", "cc", "ch", "cr", "cz", "d", "dd", "dh", "dr", "g", "gm", "gn",
             "gr", "gv", "gz", "h", "hl", "hm", "hn", "hr", "k", "k'", "kk", "kn", "kr", "kt", "kv", "kz", "l", "ld",
             "ldr", "lg", "lgr", "lk", "ll", "lm", "ln", "lph", "lq", "lt", "lv", "lx", "lz", "m", "mh", "mm", "mn",
             "mph", "n", "nc", "nd", "ndr", "ng", "ngr", "nk", "nkr", "nn", "nph", "nq", "nqr", "nz", "ph", "phr", "q",
             "q'", "qn", "qr", "r", "r'", "rc", "rg", "rk", "rkr", "rl", "rn", "rq", "rqr", "rr", "rz", "s", "sc", "sl",
             "sn", "sq", "ss", "st", "str", "t", "t'", "tt", "v", "v'", "vr", "vv", "x", "x'", "z", "z'", "", "", "",
             "", "", "", "", "", "", "", ""),
        15: ("", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "oi", "ie", "ai", "ea",
             "ae"),
        16: ("d", "ds", "k", "ks", "l", "ll", "ls", "n", "ns", "r", "rs", "s", "t", "ts", "th", "x", "", "", "", ""),
    })

    def get_factory(self, factory_id):
        if factory_id < 40:
            return self.factories[0]
        elif factory_id < 70:
            return self.factories[1]
        else:
            return self.factories[2]
