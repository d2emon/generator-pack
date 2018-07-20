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

    def __init__(self, name=None, namegen=None, **kwargs):
        self.__name = name

        child_data = kwargs.get('children_data') or self.child_data
        names_data = kwargs.get('children_names') or self.names_data

        self.generators = [] + self.child_generators
        self.generators += [ChildGenerator.from_str(child) for child in child_data]

        self.namegen = namegen or NameGenerator(names_data, default=self.name)

        self.generated_name = None
        self.generated_image = None

    @property
    def name(self):
        if self.__name is not None:
            return self.__name

        if self.type_name is not None:
            self.__name = self.type_name
        else:
            self.__name = camelCaseToSpaces(type(self).__name__)
        return self.__name

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
    def from_str(cls, name, children=None, names=None):
        t = cls(name, children_names=names, children_data=children)
        # t.namegen = NameGenerator(namegen, default=name)
        # t.generators += [ChildGenerator.from_str(child) for child in children]
        # t.add_generators(children)
        print("GENERATORS", t.name, t.generators)
        return t