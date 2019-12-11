import random

from utils.loaders import load_lines


class GeneratorTemplate:
    letters = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
    numbers = range(0, 9)
    text = ""

    @classmethod
    def formatter(cls):
        return {
            "{c}": cls.letters,
            "{n}": cls.numbers,
        }

    @classmethod
    def generate(cls, text=None):
        text = text or cls.text

        for k, v in cls.formatter().items():
            while k in text:
                text = text.replace(k, str(random.choice(v)), 1)
        return text

    @classmethod
    def strip(cls, filenames):
        return cls.generate().format(
            random.choice(load_lines(filenames[0])),
            random.choice(load_lines(filenames[1])),
        ).strip()


    @classmethod
    def glue(cls, parts, glue=""):
        return glue.join(
            [next(i) for i in parts]
        ).capitalize()
