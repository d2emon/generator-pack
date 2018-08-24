import random

# from utils.loaders import load_lines
# from .generator_data import StaticData, ListData, FileData
from .generated import Generated
from .template import GeneratorTemplate


class Generator:
    generated_class = Generated
    default = "UNGENERATED"
    text_format = "%s"

    @classmethod
    def __iter__(cls):
        return cls

    @classmethod
    def __next__(cls):
        raise AttributeError("No value to generate")

    @classmethod
    def generate(cls, *args, **kwargs):
        generated = cls.generated_class(*args, **kwargs)
        return cls.populate(generated, *args, **kwargs)

    @classmethod
    def populate(cls, generated, *args, **kwargs):
        generated.value = cls.text_format % (next(cls))
        return generated


class ListGenerator(Generator):
    data = dict()
    template = "{name}"

    @classmethod
    def get_data(cls):
        return cls.data

    @classmethod
    def __iter__(cls):
        return cls

    @classmethod
    def __next__(cls):
        next_data = {key: next(d) for key, d in cls.get_data().items()}
        return cls.template.format(**next_data)


class FileGenerator(ListGenerator):
    filename = ""
    data = None

    @classmethod
    def get_data(cls):
        if cls.data:
            return cls.data
        return FileData(cls.filename)


class PercentGenerator(Generator):
    generators = dict()

    @classmethod
    def generator(cls, chance=0):
        for c in sorted(cls.generators.keys()):
            if c >= chance:
                return cls.generators[c]
        return None

    @classmethod
    def __next__(cls):
        chance = random.randint(0, 100)
        g = cls.generator(chance)
        if g is None:
            return cls.default
        return next(g)


class TemplateGenerator(Generator):
    template = "{c}{n}"

    @classmethod
    def __next__(cls):
        return GeneratorTemplate.generate(cls.template)
