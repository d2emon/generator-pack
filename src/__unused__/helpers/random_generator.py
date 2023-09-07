import random


def random_generator(selector, generator_id=None, max_value=10):
    return selector(generator_id or random.randrange(max_value))
