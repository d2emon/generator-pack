import random


class ChildFactory:
    def __init__(
        self,
        value=None,
        min_amount=1,
        max_amount=None,
        probability=100,
    ):
        self.value = value
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.probability = probability

        # self.data = None
        self.factories = []

    def factory(self):
        return random.choice(self.factories) if len(self.factories) > 0 else self

    def check_probability(self, probability=None):
        if probability is None:
            probability = random.uniform(0, 100)
        return probability <= self.probability

    def amount(self):
        if not self.check_probability():
            return 0
        if self.max_amount is None:
            return self.min_amount
        return random.randrange(self.min_amount, self.max_amount)

    def __call__(self, *args, **kwargs):
        return [self.factory().value for _ in range(self.amount())]

    def __iter__(self):
        return self

    def __next__(self):
        return self()

    def __repr__(self):
        text = ' '.join([
            '\"{}\"'.format(self.value),
            '-'.join(str(n) for n in [self.min_amount, self.max_amount] if n),
            '({}%)'.format(self.probability) if self.probability < 100 else '',
        ])
        return "<Generator {}>".format(text)

    @classmethod
    def from_str(cls, data):
        factory = cls()

        # factory.data = data

        if data is None:
            return factory

        if isinstance(data, list):
            factory.factories = [cls.from_str(f) for f in data]
            return factory

        # value, probability, amount = get_data(data)
        data = data.split(',')
        value = data[0]
        options = data[1] if len(data) > 1 else ''
        probabilities = options.split('%')
        amounts = options.split('-')

        factory.value = value
        if len(probabilities) > 1:
            factory.probability = float(probabilities[0])
            # factory.min_amount = 1
            # factory.max_amount = None
        elif len(amounts) > 1:
            # factory.probability = 100
            factory.min_amount = int(amounts[0])
            factory.max_amount = int(amounts[1])
        else:
            # factory.probability = 100
            # factory.min_amount = 1
            # factory.max_amount = None
            pass

        # print(factory.value, (factory.min_amount, factory.max_amount), factory.probability

        return factory
