import random
from .utils import generate_count
from .data.band import names1, names2, names3, names4, names5


def generate1():
    return " ".join([
        random.choice(names1),
        random.choice(names2),
    ])


def generate2():
    return random.choice(names5)


def generate3():
    return " of ".join([
        random.choice(names3),
        random.choice(names4),
    ])


def generate(count=1):
    chance = random.randint(0, 100)
    if chance < 30:
        return generate_count(generate1, count)
    elif chance < 70:
        return generate_count(generate2, count)
    else:
        return generate_count(generate3, count)
