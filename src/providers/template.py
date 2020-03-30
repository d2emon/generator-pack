import random


class StaticListProvider:
    data = []

    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(self.data) if  len(self.data) > 0 else None


class LetterProvider(StaticListProvider):
    data = [chr(c) for c in range(ord('A'), ord('Z') + 1)]


class NumberProvider(StaticListProvider):
    data = [str(n) for n in range(0, 9)]
