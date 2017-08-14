import random


def load_lines(filename):
    lines = []
    with open(filename, "r") as f:
        lines = [line.strip() for line in f]
    return lines


class Generated():
    def __init__(self):
        self.generated_text = ""


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


class FileGenerator(ListGenerator):
    data_file = ""

    @classmethod
    def generate_text(cls):
        if len(cls.data_list) < 1:
            cls.data_list = load_lines(cls.data_file)
        return random.choice(cls.data_list)


class ParamGenerator(DataGenerator):
    @classmethod
    def generate(cls, **kwargs):
        generated = cls.generated_class()
        generated.generated_text = cls.generate_text(**kwargs)
        return generated
