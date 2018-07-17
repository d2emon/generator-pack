import random

from .data import get_thing


ITEMS = []


class Item:
    def __init__(self, what, parent=None):
        global ITEMS

        print("GENERATE", what)
        self.__name = None
        if get_thing(what) is None:
            self.type = get_thing("error")
        else:
            self.type = get_thing(what)

        self.children = []
        self.display = 0
        self.grown = False

        self.parent = parent
        if self.parent is not None:
            parent.children.append(self)

        ITEMS.append(self)

    @property
    def id(self):
        global ITEMS
        return ITEMS.index(self)

    @property
    def name(self):
        if self.__name is not None:
            return self.__name
        return self.generate_name()

    @property
    def image(self):
        return self.type.name

    def generate_name(self, *args, **kwargs):
        gen = self.type.namegen
        self.__name = gen.generate()
        return self.__name

    def get_generators(self):
        to_concat = []
        generators = []
        for i, g in enumerate(self.type.generators):
            if not isinstance(g.data, str):
                generators.append(g)
                continue
            if g.data[0] == ".":
                sub_name = g.data[1:]
                sub = get_thing(sub_name)
                if sub is not None:
                    to_concat += sub.generators
                # self.type.generators[i] = None
            else:
                generators.append(g)
        # return list(filter(lambda item: item is not None, self.type.generators + to_concat))
        return list(filter(lambda item: item is not None, generators + to_concat))

    def grow(self, *args, **kwargs):
        print("GROW", args, kwargs)
        if self.grown:
            return

        generators = self.get_generators()
        for g in generators:
            subthing = get_thing(g.value)
            if subthing is None:
                print("NO CHILD", g.value)
                continue

            if random.randrange(100) > g.probability:
                continue

            for i in range(*g.amount):
                new_item = Item(subthing.name, self)
                # self.children.append(new_item)
        random.shuffle(self.children)

        self.grown = True

    def __repr__(self):
        if self.parent is not None:
            desc = "{} \"{}\"\t-\t".format(self.parent.type.name, self.parent.name)
        else:
            desc = ""
        return "{}{} \"{}\"".format(desc, self.type.name, self.name)
