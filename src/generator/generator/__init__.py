from .generator_data import ListData, FileData
from .generated import Generated
from .template import GeneratorTemplate


from utils import load_lines

import random


class DataGenerator():
    generated_class = Generated
    default_value = "UNGENERATED"
    text_format = "%s"

    @classmethod
    def generated(cls, *args, **kwargs):
        return cls.generated_class(*args, **kwargs)

    @classmethod
    def __next__(cls, **kwargs):
        raise AttributeError("No value to generate")

    @classmethod
    def generate(cls, *args, **kwargs):
        generated = cls.generated()
        return cls.fill_generated(generated, *args, **kwargs)

    @classmethod
    def fill_generated(cls, generated, *args, **kwargs):
        # generated.value = cls.generate_value()
        generated.value = cls.text_format % (cls.__next__(*args, **kwargs))
        return generated

    @classmethod
    def generate_values(cls, count=1):
        return [cls.__next__() for i in range(count)]


class ListGenerator(DataGenerator):
    data_list = ListData()

    @classmethod
    def __next__(cls):
        if cls.data_list is None:
            return None
        return cls.data_list.__next__()


class FileGenerator(ListGenerator):
    data_file = ""
    data_list = None

    @classmethod
    def __next__(cls):
        if cls.data_list is None:
            cls.data_list = FileData(cls.data_file)
        return cls.data_list.__next__()


class PercentedGenerator(DataGenerator):
    subgenerators = dict()

    @classmethod
    def generator_by_chance(cls, chance=0):
        for c in sorted(cls.subgenerators):
            if c >= chance:
                return cls.subgenerators[c]
        return None

    @classmethod
    def __next__(cls):
        chance = random.randint(0, 100)
        g = cls.generator_by_chance(chance)
        if g is None:
            return cls.default_value
        return g.__next__()

    @classmethod
    def generate(cls):
        chance = random.randint(0, 100)
        g = cls.generator_by_chance(chance)
        if g is None:
            return cls.default
        return g.generate()


class TemplatedGenerator(DataGenerator):
    template = "{c}{n}"

    @classmethod
    def __next__(cls):
        return GeneratorTemplate.generate(cls.template)
