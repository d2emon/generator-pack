import random
from .utils import generate_count
from .data.motivation import names


def generate(count=1):
    return generate_count(lambda: random.choice(names) + ".", count)
