from .children import ChildGenerator
from .name import NameGenerator


class Thing:
    # things_n = 0
    type_name = None
    children_data = []
    names_data = None

    def __init__(self, name=None, namegen=None):
        if name is None:
            name = self.type_name

        self.name = name

        self.generators = []
        self.add_generators(self.children_data)

        self.namegen = namegen
        if self.namegen is None:
            if self.names_data is not None:
                self.namegen = NameGenerator.from_str(self.names_data)
            else:
                self.namegen = NameGenerator(self.name)

        # THINGS[name] = self
        # self.things_n += 1

    def add_generators(self, children=[]):
        for child in children:
            self.generators.append(ChildGenerator.from_str(child))

    @classmethod
    def from_str(cls, name, children=None, namegen=None):
        if (namegen is not None):
            namegen = NameGenerator.from_str(namegen)

        if children is None:
            children = []

        t = cls(name, namegen)
        t.add_generators(children)
        print("GENERATORS", t.name, t.generators)
        return t

    def clear(self):
        to_concat = []
        for i, g in enumerate(self.generators):
            if not isinstance(g.data, str):
                continue
            if g.data[0] == ".":
                sub_name = g.data[1:]
                sub = self.get_thing(sub_name)
                if sub is not None:
                    to_concat += sub.generators
                self.generators[i] = None
        # f = filter(lambda item: item is not None, self.generators + to_concat)
        # print(self.name, self.generators, "+", to_concat)
        # print(list(f))
        self.generators = list(filter(lambda item: item is not None, self.generators + to_concat))
