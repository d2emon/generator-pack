from .children import ChildGenerator
from .name import NameGenerator


class Thing:
    # things_n = 0

    def __init__(self, name, namegen=None):
        self.name = name
        self.generators = []
        if namegen is None:
            self.namegen = NameGenerator(self.name)
        else:
            self.namegen = namegen

        # THINGS[name] = self
        # self.things_n += 1

    @classmethod
    def from_str(cls, name, children, namegen=None):
        if (namegen is not None):
            namegen = NameGenerator.from_str(namegen)
        t = cls(name, namegen)

        t.generators = []
        for child in children:
            t.generators.append(ChildGenerator.from_str(child))
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
