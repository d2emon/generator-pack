import random
from .utils import generate_count
from .data.artConcept import names1, names2, names3, names4


def generate_place():
    return " ".join([
        random.choice(names3),
        random.choice(names4),
    ])


def generate_being():
    return " ".join([
        random.choice(names1),
        random.choice(names2),
    ])


def generate(count=1, being=True):
    if being:
        return generate_count(generate_being, count)
    else:
        return generate_count(generate_place, count)
