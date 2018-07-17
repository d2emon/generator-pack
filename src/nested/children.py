import random


class ChildGenerator:
    def __init__(self, value=None, amount=(1, ), probability=100):
        self.value = value
        self.amount = amount
        self.probability = probability
        self.data = None

    @classmethod
    def from_str(cls, data):
        g = cls()
        g.data = data
        g.parse(data)
        return g

    def parse(self, data):
        if not isinstance(data, str):
            data = random.choice(data)
        # value, probability, amount = get_data(data)
        self.get_value(data)
        # print(self.value, self.amount, self.probability)

    def get_value(self, value):
        data = value.split(",")
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
