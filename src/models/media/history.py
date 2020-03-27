import random
import math


class IncomeHistory:
    def __init__(self, starting=None):
        self._history = [0]
        self.starting = starting
        if starting is not None:
            self.append(starting)

    def generate(self, position=1):
        return None

    def __getitem__(self, item):
        if item < 0:
            return 0

        for p in range(len(self), item + 1):
            self.append(self.generate(p))
        return self._history[item]

    def __len__(self):
        return len(self._history)

    def append(self, value):
        self._history.append(value)

    @property
    def first(self):
        return self[1]

    @property
    def last(self):
        return self[len(self) - 1]

    def __next__(self):
        return self[len(self)]

    def total(self, position=None):
        position = position or len(self)
        return sum([self[i] for i in range(position)])


class BoxHistory(IncomeHistory):
    min_income = 100000000
    max_income = 500000000

    def __init__(self, starting=None):
        starting = starting or random.randrange(self.min_income, self.max_income)
        super().__init__(starting)

    def generate(self, position=1):
        if position < 1:
            return 0

        if position < len(self) - 1:
            return self[position]

        box = self.starting * math.pow(position, -3 / 4)
        adjust = random.randint(50, 150) / 100
        return int(box * adjust)
