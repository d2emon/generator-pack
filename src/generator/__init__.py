import random


def load_lines(cls, filename):
    lines = []
    with open(filename, "r") as f:
        lines = [line.strip() for line in f]
    return lines


class Generated():
    def __init__(self):
        self.generated_text = ""


class GeneratorTemplate():
    text_format = "%s %s"

    @classmethod
    def generate(cls, filenames):
        return cls.text_format % (
            random.choice(load_lines(filenames[0])),
            random.choice(load_lines(filenames[1])),
        )


class DataGenerator():
    generated_class = Generated
    text_format = "%s"

    @classmethod
    def generate_text(cls):
        raise AttributeError("No text to generate")

    @classmethod
    def generate(cls):
        generated = cls.generated_class()
        generated.generated_text = cls.text_format % (cls.generate_text())
        return generated

    @classmethod
    def generate_count(cls, count=1):
        return [cls.generate() for c in count]


class ListGenerator(DataGenerator):
    data_list = []

    @classmethod
    def generate_text(cls):
        return random.choice(cls.data_list)


class ParamGenerator(DataGenerator):
    @classmethod
    def generate(cls, **kwargs):
        generated = cls.generated_class()
        generated.generated_text = cls.generate_text(**kwargs)
        return generated
