import random


class ChildGenerator:
    def __init__(self, value=None, amount=(1, ), probability=100):
        self.value = value
        self.amount = amount
        self.probability = probability

        # self.data = None
        self.generators = []

    def generator(self):
        if len(self.generators) < 1:
            return self
        return random.choice(self.generators)

    def test_probaility(self, probability=None):
        probability = probability or random.randrange(100)
        return probability <= self.probability

    def to_generate(self):
        if not self.test_probaility():
            return 0
        if len(self.amount) == 1:
            return self.amount[0]
        return random.randrange(*self.amount)

    def generate(self):
        return [self.generator().value for i in range(self.to_generate())]


    @classmethod
    def from_str(cls, data):
        g = cls()
        g.parse(data)
        return g

    def parse(self, data):
        # g.data = data

        if isinstance(data, list):
            self.generators = [cls.from_str(d) for d in data]
            return

        if data is None:
            return

        # value, probability, amount = get_data(data)
        data = data.split(",")
        self.amount = [1]

        if len(data) > 1:
            self.amount = self.get_amount(data[1])

        if len(data) > 1:
            probability = self.get_probability(data[1])
        else:
            probability = self.get_probability("1")

        if len(probability) > 1:
            self.probability = float(probability[0])
            self.amount = [1]
        else:
            self.probability = 100
        self.value = data[0]
        # print(self.value, self.amount, self.probability)

    def get_amount(self, amount):
        r = amount.split("-")
        if len(r) > 1:
            # return Rand(r[0], r[1])
            return int(r[0]), int(r[1])
        else:
            return int(amount[0:1]),

    def get_probability(self, probability):
        return (probability + "?").split("%")

    def __repr__(self):
        amount = "-".join([str(a) for a in self.amount])
        if self.probability != 100:
            amount += " ({}%)".format(self.probability)
        return "<Generator \"{}\" {}>".format(self.value, amount)
