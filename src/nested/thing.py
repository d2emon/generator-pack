import re


from .children import ChildGenerator
from .name import NameGenerator


CAMEL_CASE = re.compile('([a-z0-9])([A-Z])')


def camelCaseToSpaces(s):
    return CAMEL_CASE.sub(r'\1 \2', s).lower()


class Generator:
    # things_n = 0
    type_name = None
    child_data = []
    child_generators = []
    names_data = None

    def __init__(self, name=None, namegen=None):
        self.__name = name

        self.generators = [] + self.child_generators
        self.add_generators(self.child_data)

        self.namegen = namegen
        if self.namegen is None:
            self.namegen = NameGenerator(self.names_data, default=self.name)

        self.generated_name = None
        self.generated_image = None

    @property
    def name(self):
        if self.__name is not None:
            return self.__name

        if self.type_name is not None:
            self.__name = self.type_name
            return self.__name

        print("CLASS", self.__class__.__name__)
        res = type(self).__name__
        print("CLASS", res)
        self.__name = camelCaseToSpaces(res)
        return self.__name

    def add_generators(self, children=[]):
        for child in children:
            self.generators.append(ChildGenerator.from_str(child))

    def __call__(self, *args, **kwargs):
        return self

    def generate_name(self):
        return self.namegen.generate()

    def generate_image(self):
        return self.name

    @classmethod
    def fill(cls, generated):
        t = cls.generate()
        generated.template = t
        generated.generated_name = t.generate_name()
        generated.generated_image = t.generate_image()
        return generated

    @classmethod
    def generate(cls):
        return cls()

    """
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
    """

class Thing(Generator):
    @classmethod
    def from_str(cls, name, children=None, namegen=None):
        if (namegen is not None):
            namegen = NameGenerator(namegen)

        if children is None:
            children = []

        t = cls(name, namegen)
        t.add_generators(children)
        print("GENERATORS", t.name, t.generators)
        return t