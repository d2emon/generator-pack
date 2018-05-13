from .generator_data import ListData, FileData
from .generated import Generated
from .template import GeneratorTemplate


from utils import load_lines

import random


class DataGenerator():
    generated_class = Generated
    default_value = "UNGENERATED"

    @classmethod
    def generated(cls, *args, **kwargs):
        return cls.generated_class(*args, **kwargs)

    @classmethod
    def generate_value(cls):
        raise AttributeError("No value to generate")

    @classmethod
    def generate(cls):
        generated = cls.generated()
        return cls.fill_generated(generated)

    @classmethod
    def fill_generated(cls, generated):
        generated.value = cls.generate_value()
        return generated

    @classmethod
    def generate_count(cls, count=1):
        return [cls.generate() for c in count]

    @classmethod
    def generate_values(cls, count=1):
        return [cls.generate_value() for i in range(count)]


class TextGenerator(DataGenerator):
    text_format = "%s"

    @classmethod
    def generate(cls):
        generated = cls.generated()
        generated.generated_value = cls.text_format % (cls.generate_value())
        return generated


class ListGenerator(DataGenerator):
    data_list = ListData()

    @classmethod
    def generate_value(cls, data=None):
        if data is None:
            data_list = cls.data_list
        else:
            data_list = ListData(data)
        if not data_list:
            return None
        return data_list.select()

    @classmethod
    def generate_values(cls, count=1, data=None):
        if data is None:
            data_list = cls.data_list
        else:
            data_list = ListData(data)
        if not data_list:
            return None
        return data_list.select(count)

class FileGenerator(ListGenerator):
    data_file = ""
    data_list = FileData()

    @classmethod
    def generate_value(cls, count=1):
        cls.data_list.filename = cls.data_file
        return cls.data_list.select(count)


class ParamGenerator(DataGenerator):
    @classmethod
    def generate(cls, **kwargs):
        generated = cls.generated()
        generated.generated_text = cls.generate_value(**kwargs)
        return generated


class PercentedGenerator(DataGenerator):
    subgenerators = dict()

    @classmethod
    def generator_by_chance(cls, chance=0):
        for c in sorted(cls.subgenerators):
            if c >= chance:
                return cls.subgenerators[c]
        return None

    @classmethod
    def generate_value(cls):
        chance = random.randint(0, 100)
        g = cls.generator_by_chance(chance)
        if g is None:
            return cls.default_value
        return g.generate_value()

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
    def generate_value(cls):
        return GeneratorTemplate.pregenerate(cls.template)
