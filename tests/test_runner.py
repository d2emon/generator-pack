import pytest
import random

from generator import generators

from generator.other.demonym import Demonym


@pytest.fixture
def count():
    return random.randrange(255)


def test_lugansk(count):
    for _ in range(count):
        assert str(Demonym('Lugansk'))[:4] == "Luga"


def test_all(count):
    for name, g in generators.items():
        print(name)
        for _ in range(count):
            assert g.generate() is not None


def test_other(count):
    name = random.choice(generators.keys())
    g = generators.get(name)
    for _ in range(count):
        assert g.generate() is None
