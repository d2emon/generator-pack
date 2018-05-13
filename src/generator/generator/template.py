from utils import load_lines

import random


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
