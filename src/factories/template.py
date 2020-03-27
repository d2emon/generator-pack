import random
from utils.loaders import load_lines


class FactoryTemplate:
    class LetterFactory:
        DATA = [chr(c) for c in range(ord('A'), ord('Z') + 1)]

        def __iter__(self):
            return self

        def __next__(self):
            return random.choice(self.DATA)

    class NumberFactory:
        DATA = [str(n) for n in range(0, 9)]

        def __iter__(self):
            return self

        def __next__(self):
            return random.choice(self.DATA)

    TEXT = ''

    def __init__(self, text=None):
        self.__text = text

    @property
    def text(self):
        if self.__text is None:
            self.__text = self.TEXT
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value

    @property
    def replacers(self):
        return {
            '{c}': self.LetterFactory(),
            '{n}': self.NumberFactory(),
        }

    def __iter__(self):
        return self

    def __next__(self):
        text = self.text
        for k, v in self.replacers.items():
            while k in text:
                text = text.replace(k, next(v), 1)
        return text

    def strip(self, filenames):
        return next(self).format(
            random.choice(load_lines(filenames[0])),
            random.choice(load_lines(filenames[1])),
        ).strip()

    @classmethod
    def glue(cls, parts, glue=""):
        return glue.join(next(i) for i in parts).capitalize()
