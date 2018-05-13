from utils import load_lines

import random


class GeneratorTemplate():
    letters = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
    numbers = range(0, 9)
    text = "%s %s"

    @classmethod
    def generate(cls, text=None):
        formatter = {
            "{c}": cls.letters,
            "{n}": cls.numbers,
        }

        if not text:
            text = cls.text

        for k, v in formatter.items():
            while k in text:
                text = text.replace(k, str(random.choice(v)), 1)
        return text

    @classmethod
    def strip(cls, filenames):
        return (cls.generate() % (
            random.choice(load_lines(filenames[0])),
            random.choice(load_lines(filenames[1])),
        )).strip()


    @classmethod
    def glue(cls, parts, glue=""):
        selected = [i.__next__() for i in parts]
        return glue.join(selected).capitalize()
