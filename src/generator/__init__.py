import random
from utils import load_lines


class Generated():
    title = None

    def __init__(self, value=""):
        self.value = value

    def __repr__(self):
        if self.title is None:
            return str(self.value)
        return "{}:\t\"{}\"".format(self.title, self.value)

    @property
    def generated_value(self):
        return self.value


class GeneratorTemplate():
    letters = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
    numbers = range(0, 9)
    text_format = "%s %s"

    @classmethod
    def letter(cls):
        return random.choice(cls.letters)

    @classmethod
    def number(cls):
        return str(random.choice(cls.numbers))

    @classmethod
    def pregenerate(cls, text_format=None):
        if not text_format:
            text_format = cls.text_format
        formatter = {
            "{c}": cls.letter,
            "{n}": cls.number,
        }
        for k, v in formatter.items():
            while k in text_format:
                text_format = text_format.replace(k, v(), 1)
        return text_format

    @classmethod
    def generate(cls, filenames):
        return (cls.pregenerate() % (
            random.choice(load_lines(filenames[0])),
            random.choice(load_lines(filenames[1])),
        )).strip()


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


class TextGenerator(DataGenerator):
    text_format = "%s"

    @classmethod
    def generate(cls):
        generated = cls.generated()
        generated.generated_value = cls.text_format % (cls.generate_value())
        return generated


class ListGenerator(DataGenerator):
    data_list = []

    @classmethod
    def generate_value(cls, data_list=None, count=1):
        if data_list is None:
            data_list = cls.data_list
        if not data_list:
            return None #  ""
        if count > 1:
            random.shuffle(data_list)
            return data_list[0:count]
        return random.choice(data_list)


class FileGenerator(ListGenerator):
    data_file = ""

    @classmethod
    def generate_value(cls):
        if len(cls.data_list) < 1:
            cls.data_list = load_lines(cls.data_file)
        return random.choice(cls.data_list)


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


class TemplatedGenerator(DataGenerator):
    template = "{c}{n}"

    @classmethod
    def generate_value(cls):
        return GeneratorTemplate.pregenerate(cls.template)
