import random

from .data import get_thing, get_generators


ITEMS = []


class Item:
    def __init__(self, template, parent=None):
        self.__name = None
        self.__children = None
        self.type = template
        self.setParent(parent)

        self.template = None
        self.generated_name = ""
        self.generated_image = ""

    @property
    def name(self):
        if self.__name is not None:
            return self.__name

        gen = self.type.namegen
        self.__name = gen.generate()
        return self.__name

    @property
    def image(self):
        return self.type.name

    def setParent(self, parent=None):
        self.parent = parent

    def addChild(self, child):
        if child is None:
            return

        if self.__children is None:
            self.__children = []

        self.__children.append(child)
        child.setParent(self)

    @property
    def children(self):
        if self.__children is not None:
            return self.__children

        self.generate_children()
        return self.__children

    def generate_children(self, *args, **kwargs):
        print("GROW", args, kwargs)

        self.__children = []
        generators = get_generators(self.type.name)
        if generators is None:
            return self.__children

        for generator in generators:
            for value in generator.generate():
                if value is None:
                    continue

                subthing = get_thing(value)
                if subthing is None:
                    print("NO CHILD", value)
                    continue

                new_item = Item.generate(subthing.name)
                self.addChild(new_item)

        random.shuffle(self.__children)
        return self.__children

    def __repr__(self):
        if self.parent is not None:
            desc = "{} \"{}\"\t-\t".format(self.parent.type.name, self.parent.name)
        else:
            desc = ""
        return "{}{} \"{}\"".format(desc, self.type.name, self.name)

    @classmethod
    def getTemplate(cls, template="error"):
        if get_thing(template) is None:
            return get_thing("error")
        return get_thing(template)

    @classmethod
    def generate(cls, template, parent=None):
        global ITEMS

        item = cls(cls.getTemplate(template), parent)

        ITEMS.append(item)
        return item