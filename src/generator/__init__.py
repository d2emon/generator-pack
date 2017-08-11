import random


class Generated():
    def __init__(self):
        self.generated_text = ""


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
