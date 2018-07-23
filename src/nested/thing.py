import re
import random


from .children import ChildGenerator
from .name import NameGenerator


CAMEL_CASE = re.compile('([a-z0-9])([A-Z])')


def camelCaseToSpaces(s):
    return CAMEL_CASE.sub(r'\1 \2', s).lower()


class Generator:
    # things_n = 0
    type_name = None
    child_data = []
    child_generator = None
    child_generators = []

    names = None
    names_data = None

    positions = None

    def __init__(self, name=None, namegen=None, **kwargs):
        self.__name = name
        self.__children = None

        child_data = kwargs.get('children_data') or self.child_data
        names_data = kwargs.get('children_names') or self.names or self.names_data

        self.generators = [] + self.child_generators
        self.generators += [ChildGenerator.from_str(child) for child in child_data]
        if self.child_generator is not None:
            self.generators.append(ChildGenerator(*self.child_generator))

        self.namegen = namegen or NameGenerator(names_data, default=self.name)

        self.generated_name = None
        self.generated_image = None

    @property
    def name(self):
        if self.__name is not None:
            return self.__name

        self.__name = self.type_name or camelCaseToSpaces(type(self).__name__)
        return self.__name

    @property
    def children(self):
        if self.__children is not None:
            return self.__children

        self.__children = sum([g.generate() for g in self.generators])
        return self.__children

    def __call__(self, *args, **kwargs):
        return self

    def custom_generate(self):
        return None

    def generate_name(self):
        return self.namegen.generate()

    def generate_image(self):
        return self.name

    def generate_pos(self):
        if self.positions is None:
            return None
        return [random.randrange(*i) if len(i) > 1 else i[0] for i in self.positions]

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
    def from_str(cls, name, children=None, names=None):
        t = cls(name, children_names=names, children_data=children)
        # t.namegen = NameGenerator(namegen, default=name)
        # t.generators += [ChildGenerator.from_str(child) for child in children]
        # t.add_generators(children)
        print("GENERATORS", t.name, t.generators)
        return t