import random

from .data import get_thing, get_generators


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

    def grow(self, *args, **kwargs):
        print("GROW", args, kwargs)
        if self.grown:
            return

        generators = get_generators(self.type.type_name)
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
