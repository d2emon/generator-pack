import pytest
import random

from generator import generators, markov_street

from generator.demonym import Demonym
from fixtures.streets import streets


@pytest.fixture
def count():
    return random.randrange(255)


def test_street(count):
    for _ in range(count):
        assert markov_street(streets, 64) is None


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
